#!/usr/bin/env python3
"""
Experiment driver for the SIGNALING-GAME extension.

Usage (from src/):
    IDS_CONFIG=signaling_toy.conf  ../venv/bin/python -u signaling_do.py main
    IDS_CONFIG=signaling_toy.conf  ../venv/bin/python -u signaling_do.py sensitivity

One "job" = one (dataset, defender budget, seed). Each job runs:
  A. Fixed-attacker study: defenders BLIND / INFORMED / BELIEF trained by the RL
     oracle against fixed type-based attackers, plus the existing heuristic
     baselines (uniform, newest, proportion, snort/suricata rules, aics, icde).
  B. Double oracle for the three main games
       ZS_BLIND : zero-sum payoffs, defender sees alerts only (original approach)
       GS_BLIND : dataset payoffs (general-sum where test.py has a gain), alerts only
                  (skipped where identical to ZS_BLIND, i.e. suricata and fraud)
       SIG      : dataset payoffs, belief defender, type-conditioned attacker
  C. Cross-evaluation of every final defender against every final attacker,
     with common random numbers.
  D. Belief diagnostics (calibration / Bayes consistency / off-path) for SIG.
Results are written as JSON/CSV under runs/<tag>/ and summarised by
signaling_analysis.py.
"""

import os
os.environ.setdefault('CUDA_VISIBLE_DEVICES', '')
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import json
import logging
import multiprocessing
import sys
import time
import traceback
import warnings

warnings.filterwarnings('ignore')
import numpy as np
import tensorflow as tf

from config import config
import signaling as S
from listutils import unflatten_list
import test as T

# Each worker process uses ONE TensorFlow thread, otherwise 10 parallel
# workers would each start 12 threads and slow each other down. This wraps
# tf.Session without editing ddpg.py / sac.py / td3_v3_1.py.
_orig_session = tf.Session


def _single_thread_session(*args, **kwargs):
    kwargs.setdefault('config', tf.ConfigProto(intra_op_parallelism_threads=1,
                                               inter_op_parallelism_threads=1))
    return _orig_session(*args, **kwargs)


tf.Session = _single_thread_session

from double_oracle import find_mixed_NE as _find_mixed_NE   # unchanged solver (nashpy)


def find_mixed_NE(payoff_def, payoff_atk, selection):
    """Unchanged double_oracle.find_mixed_NE; only clips tiny negative round-off."""
    att_s, def_s, u = _find_mixed_NE(payoff_def, payoff_atk, selection=selection)
    fix = lambda p: list(np.clip(np.array(p, dtype=float), 0, None) / np.clip(np.array(p, dtype=float), 0, None).sum())
    return fix(att_s), fix(def_s), float(u)

# ----------------------------- configuration ------------------------------
SG = config['signaling']
ALGO = SG.get('oracle_algo', 'ddpg')
GAMMA = config.getfloat('parameter', 'gamma')
MAX_EP_STEPS = config.getint('parameter', 'max_ep_steps')
MAX_ITER = config.getint('double-oracle', 'max_iteration')
N_TRIAL = config.getint('double-oracle', 'n_trial')
SELECTION = config.get('game', 'equilibrium_selection', fallback='defender_max')
PAYOFF_EPISODES = SG.getint('payoff_episodes')
FINAL_EPISODES = SG.getint('final_eval_episodes')
EVAL_SEED = SG.getint('eval_seed', 12345)
TAG = SG.get('tag')
OUT = os.path.join('..', 'runs', TAG)


def oracle_module():
    """The existing RL oracle code path, chosen by config (oracle_algo)."""
    if ALGO == 'ddpg':
        import ddpg as m
    elif ALGO == 'sac':
        import sac as m
    elif ALGO == 'td3':
        import td3_v3_1 as m
    else:
        raise ValueError(ALGO)
    return m

# ------------------------------- oracles ----------------------------------


def train_defender(game, kind, atk_policies, atk_probs, alpha_hat, seed):
    """
    RL best response of the defender against a mixed attacker strategy.
    kind = 'blind' (alerts only), 'informed' (alerts + true type) or
    'belief' (alerts + Bayes belief computed with conjectured attack rates alpha_hat).
    Uses DDPGlearning.learn_from_mix / evaluate of the chosen algorithm file.
    """
    mod = oracle_module()
    filt = S.BeliefFilter(game, alpha_hat) if kind == 'belief' else None
    graph = tf.Graph()
    with graph.as_default():
        tf.set_random_seed(seed)
        agent = mod.DDPGlearning('defend', S.defender_obs_dim(game, kind), game.T)

        def observe(s):
            b = S.belief_of(game, s, filt) if kind == 'belief' else None
            return S.defender_obs(game, s, kind, b)

        def update(mode, s, action, atk):
            delta = game.base.make_investigation_feasible(s.N, unflatten_list(action, game.T))
            nxt = S.step(game, mode, s, delta, atk)
            return nxt, nxt.U_defender - s.U_defender

        start = lambda: S.initial_state(game)
        agent.learn_from_mix(game.base, start, observe, update, list(atk_policies), list(atk_probs))
        agent.evaluate(game.base, start, observe, update, list(atk_policies), list(atk_probs))
    agent.ddpg.memory = None      # replay buffer no longer needed: free RAM
    return S.DefenderPolicy(game, agent, kind, filt, label=kind), agent.utility


def train_attacker(game, def_policies, def_probs, seed):
    """RL best response of the type-conditioned attacker against a mixed defender strategy."""
    mod = oracle_module()
    graph = tf.Graph()
    with graph.as_default():
        tf.set_random_seed(seed)
        agent = mod.DDPGlearning('attack', S.attacker_obs_dim(game), game.A)

        def observe(s):
            return S.attacker_obs(game, s)

        def update(mode, s, action, dpol):
            alpha = game.base.make_attack_feasible(list(action))
            nxt = S.step(game, mode, s, dpol, alpha)
            return nxt, -1.0 * (nxt.U_attacker - s.U_attacker)

        start = lambda: S.initial_state(game)
        agent.learn_from_mix(game.base, start, observe, update, list(def_policies), list(def_probs))
        agent.evaluate(game.base, start, observe, update, list(def_policies), list(def_probs))
    agent.ddpg.memory = None      # replay buffer no longer needed: free RAM
    return S.AttackerPolicy(game, agent, label='rl'), agent.utility


def evaluate_pair(game, d, a, n):
    r = S.play(game, d, a, n, MAX_EP_STEPS, GAMMA, EVAL_SEED)
    return -r['def_loss'].mean(), r['atk_util'].mean(), r['alpha_mean']

def close_policy(p):
    """Release the TensorFlow session of a trained policy (RAM)."""
    if hasattr(p, 'agent'):
        p.agent.ddpg.sess.close()


# ---------------------------- double oracle --------------------------------


def double_oracle(game, kind, seed, label, log):
    """
    Same loop structure as double_oracle.py, but the pools contain
    type-conditioned attacker policies and (for kind='belief') belief-conditioned
    defender policies. Returns final mixed strategies + per-iteration diagnostics.
    """
    uniform_atk = S.FixedTypedAttacker([T.test_attack_action] * game.K, 'uniform')
    def_pool = [T.test_defense_newest]
    atk_pool = [uniform_atk]
    u_d, u_a, al = evaluate_pair(game, def_pool[0], atk_pool[0], PAYOFF_EPISODES)
    payoff_def = np.array([[u_d]])
    payoff_atk = np.array([[u_a]])
    atk_alpha = [al]                         # per attacker policy: mean attack prob per type
    diag = []
    for it in range(MAX_ITER):
        t0 = time.time()
        att_s, def_s, util_d = find_mixed_NE(payoff_def, payoff_atk, selection=SELECTION)
        util_a = float(np.dot(np.dot(def_s, payoff_atk), att_s))
        # defender's conjecture of type-conditioned attack rates = equilibrium mixture
        alpha_hat = sum(p * atk_alpha[j] for j, p in enumerate(att_s))
        best_d = best_a = None
        for k in range(N_TRIAL):
            s_k = seed * 1000 + it * 10 + k
            np.random.seed(s_k)
            a_pol, a_u = train_attacker(game, def_pool, def_s, s_k)
            np.random.seed(s_k + 500)
            d_pol, d_u = train_defender(game, kind, atk_pool, att_s, alpha_hat, s_k + 500)
            if best_a is None or a_u > best_a[1]:
                best_a = (a_pol, a_u)
            if best_d is None or d_u > best_d[1]:
                best_d = (d_pol, d_u)
        a_pol, d_pol = best_a[0], best_d[0]
        # new column: new attacker vs all old defenders
        col_d, col_a = [], []
        for dp in def_pool:
            x, y, al = evaluate_pair(game, dp, a_pol, PAYOFF_EPISODES)
            col_d.append(x); col_a.append(y)
        atk_pool.append(a_pol); atk_alpha.append(al)
        payoff_def = np.hstack([payoff_def, np.array(col_d)[:, None]])
        payoff_atk = np.hstack([payoff_atk, np.array(col_a)[:, None]])
        # new row: new defender vs all attackers (incl. the new one)
        row_d, row_a = [], []
        for ap in atk_pool:
            x, y, _ = evaluate_pair(game, d_pol, ap, PAYOFF_EPISODES)
            row_d.append(x); row_a.append(y)
        def_pool.append(d_pol)
        payoff_def = np.vstack([payoff_def, np.array(row_d)[None, :]])
        payoff_atk = np.vstack([payoff_atk, np.array(row_a)[None, :]])
        # best-response improvement (exploitability proxy), as in double_oracle.py
        d_gain = float(np.dot(payoff_def[-1, :-1], att_s) - util_d)
        a_gain = float(np.dot(payoff_atk[:-1, -1], def_s) - util_a)
        diag.append({'iteration': it, 'eq_def_utility': float(util_d), 'eq_atk_utility': util_a,
                     'def_br_gain': d_gain, 'atk_br_gain': a_gain,
                     'exploitability': max(d_gain, 0) + max(a_gain, 0),
                     'seconds': time.time() - t0})
        log('{} it {}: eq def loss {:.3f}  def BR gain {:.3f}  atk BR gain {:.3f}  ({:.0f}s)'.format(
            label, it, -util_d, d_gain, a_gain, time.time() - t0))
        if d_gain <= 0 and a_gain <= 0:
            break
    att_s, def_s, util_d = find_mixed_NE(payoff_def, payoff_atk, selection=SELECTION)
    # policies outside the final equilibrium support are never used again
    for p, w in list(zip(def_pool, def_s)) + list(zip(atk_pool, att_s)):
        if w < 1e-9:
            close_policy(p)
    return {'def_pool': def_pool, 'atk_pool': atk_pool, 'def_s': list(def_s), 'att_s': list(att_s),
            'atk_alpha': atk_alpha, 'payoff_def': payoff_def.tolist(),
            'payoff_atk': payoff_atk.tolist(), 'final_eq_def_loss': -float(util_d), 'diag': diag}

# ------------------------------- baselines ---------------------------------


def baseline_defenders(dataset, budget):
    """Existing non-learning defenders of test.py that apply to this dataset/budget."""
    b = {'uniform': T.test_defense_action, 'newest': T.test_defense_newest,
         'proportion': T.test_defense_proportion}
    if dataset == 'snort':
        b['snort_rule'] = T.test_defense_snort
    if dataset == 'suricata':
        b['suricata_rule'] = T.test_defense_suricata
    if dataset == 'fraud':
        b['fraud_rule'] = T.test_defense_fraud
        if budget in (5, 10, 15, 20, 30, 40):
            b['aics'] = T.test_defense_aics
            b['icde'] = T.test_defense_icde
    return b

# -------------------------- belief diagnostics -----------------------------


def belief_diagnostics(game, sig, n_episodes, out_prefix):
    """
    (1) Bayes consistency: the defender's belief uses CONJECTURED attack rates.
        Compare it with the belief computed by exact Bayes using the attack
        rates the final attacker mixture ACTUALLY realised in these episodes.
    (2) Calibration: P(true type = k | belief bin) vs the belief itself.
    (3) Off-path: how often the signal had zero likelihood under every type.
    (4) Behaviour at all beliefs (incl. ones never reached on path): the
        investigation split of the main belief policy at typical alert counts.
    """
    def_mix = S.Mix(sig['def_pool'], sig['def_s'])
    atk_mix = S.Mix(sig['atk_pool'], sig['att_s'])
    r = S.play(game, def_mix, atk_mix, n_episodes, MAX_EP_STEPS, GAMMA, EVAL_SEED + 1, record=True)
    belief_pols = [(p, w) for p, w in zip(sig['def_pool'], sig['def_s'])
                   if isinstance(p, S.DefenderPolicy) and p.kind == 'belief' and w > 1e-9]
    if not belief_pols:
        return {'note': 'no belief policy in final defender support'}
    main = max(belief_pols, key=lambda x: x[1])[0]
    consistent = S.BeliefFilter(game, r['alpha_mean'])
    rows, diffs, off_def, off_true, nsteps = [], [], 0, 0, 0
    for e, ep in enumerate(r['traj']):
        b_def, b_true = game.prior.copy(), game.prior.copy()
        for j, st in enumerate(ep['steps']):
            b_def, o1 = main.filt.update(b_def, st['N'])
            b_true, o2 = consistent.update(b_true, st['N'])
            off_def += o1; off_true += o2; nsteps += 1
            diffs.append(np.abs(b_def - b_true).max())
            rows.append([e, j, ep['theta']] + list(b_def) + list(b_true))
    rows = np.array(rows)
    np.savetxt(out_prefix + '_belief_traj.csv', rows, delimiter=',', fmt='%.6g',
               header='episode,step,true_type,' + ','.join('def_b{}'.format(k) for k in range(game.K))
               + ',' + ','.join('bayes_b{}'.format(k) for k in range(game.K)), comments='')
    # calibration of the defender belief for type 0
    b0 = rows[:, 3]
    is0 = (rows[:, 2] == 0).astype(float)
    bins = np.linspace(0, 1, 11)
    calib = []
    for lo, hi in zip(bins[:-1], bins[1:]):
        m = (b0 >= lo) & (b0 < hi if hi < 1 else b0 <= hi)
        if m.sum() > 0:
            calib.append([float(lo), float(hi), int(m.sum()), float(b0[m].mean()), float(is0[m].mean())])
    # behaviour at different beliefs, at the average alert counts of each type
    behaviour = []
    for k in range(game.K):
        Nk = (game.fp_means + np.array([sum(a.pr_alert[t] * r['alpha_mean'][k][i]
              for i, a in enumerate(game.type_models[k].attack_types)) for t in range(game.T)]))
        for name, b in [('prior', game.prior)] + [('certain_' + game.type_names[j], np.eye(game.K)[j]) for j in range(game.K)]:
            s = S.initial_state(game, k)
            s.N = [list(np.round(Nk))]
            obs = np.array(S.defender_obs(game, s, 'belief', b), dtype=np.float32)
            act = np.array(main.agent.ddpg.choose_action(obs))
            behaviour.append({'alerts_like_type': game.type_names[k], 'belief': name,
                              'investigation_share': list(act / max(act.sum(), 1e-12))})
    final_correct = [rows[(rows[:, 0] == e)][-1, 3 + int(ep['theta'])] for e, ep in enumerate(r['traj'])]
    return {'mean_abs_belief_diff_vs_exact_bayes': float(np.mean(diffs)),
            'max_abs_belief_diff_vs_exact_bayes': float(np.max(diffs)),
            'conjectured_alpha': main.filt.alpha_hat.tolist(), 'realised_alpha': r['alpha_mean'].tolist(),
            'offpath_rate_defender_filter': off_def / nsteps, 'offpath_rate_exact_filter': off_true / nsteps,
            'calibration_type0': calib, 'behaviour_at_beliefs': behaviour,
            'mean_final_belief_on_true_type': float(np.mean(final_correct))}


def type_check(game, n_episodes):
    """
    Verify that the two types call for DIFFERENT investigation patterns:
    for each type (attacking with the fixed uniform attacker) find the best
    static budget split among a candidate set, then cross-apply it.
    """
    Tn = game.T
    cands = [('one_hot_t{}'.format(t), np.eye(Tn)[t]) for t in range(Tn)]
    cands.append(('uniform', np.ones(Tn) / Tn))
    cands.append(('false_alert_proportional', game.fp_means / game.fp_means.sum()))
    if Tn <= 3:
        g = np.arange(0, 1.0001, 0.1)
        for x in itertools.product(g, repeat=Tn):
            if abs(sum(x) - 1) < 1e-6:
                cands.append(('grid_' + '_'.join('{:.1f}'.format(v) for v in x), np.array(x)))
    res = {}
    for k in range(game.K):
        atk = S.FixedTypedAttacker([T.test_attack_action] * game.K)
        thetas = np.full(n_episodes, k)
        out = []
        for name, w in cands:
            def pol(model, state, w=w):
                return model.make_investigation_feasible(state.N, [list(w * model.def_budget)])
            r = S.play(game, pol, atk, n_episodes, MAX_EP_STEPS, GAMMA, EVAL_SEED + 2, thetas=thetas)
            out.append((name, float(r['def_loss'].mean())))
        out.sort(key=lambda x: x[1])
        res[game.type_names[k]] = out
    summary = {}
    for k, name in enumerate(game.type_names):
        best = res[name][0]
        summary[name] = {'best_split': best[0], 'best_loss': best[1],
                         'loss_using_other_types_best_split': {
                             o: dict(res[name])[res[o][0][0]] for o in game.type_names if o != name}}
    return summary


import itertools  # noqa: E402  (used by type_check)

# --------------------------------- jobs ------------------------------------


def adv_budget_of(dataset):
    return {'snort': 125.0, 'suricata': 120.0, 'fraud': 2.0}[dataset]


def fixed_attacker_study(game, dataset, budget, seed, log, extra=None):
    """Condition (a)-(c): BLIND, INFORMED, BELIEF defenders vs fixed type-based attackers."""
    fixed = S.FixedTypedAttacker([T.test_attack_action] * game.K, 'fixed_uniform')
    alpha = S.play(game, T.test_defense_newest, fixed, 20, MAX_EP_STEPS, GAMMA, EVAL_SEED)['alpha_mean']
    rows, pols = [], {}
    for kind in ['blind', 'informed', 'belief']:
        t0 = time.time()
        np.random.seed(seed * 7 + 1)      # same seed for all three kinds
        pol, _ = train_defender(game, kind, [fixed], [1.0], alpha, seed * 7 + 1)
        pols[kind.upper()] = pol
        log('fixed-attacker {} trained in {:.0f}s'.format(kind, time.time() - t0))
    for name, f in baseline_defenders(dataset, budget).items():
        pols['baseline_' + name] = f
    for name, pol in pols.items():
        r = S.play(game, pol, fixed, FINAL_EPISODES, MAX_EP_STEPS, GAMMA, EVAL_SEED + 100)
        row = {'dataset': dataset, 'budget': budget, 'seed': seed, 'defender': name,
               'attacker': 'fixed_uniform', 'def_loss': float(r['def_loss'].mean()),
               'def_loss_by_type': [float(r['def_loss'][r['thetas'] == k].mean()) for k in range(game.K)]}
        if extra:
            row.update(extra)
        rows.append(row)
    return rows, pols


def run_job(job):
    dataset, budget, seed = job
    name = '{}_{}_s{}'.format(dataset, int(budget), seed)
    os.makedirs(OUT, exist_ok=True)
    done_file = os.path.join(OUT, name + '.json')
    if os.path.exists(done_file):
        return name + ' (already done)'
    # optional helper pool (SIG_SKIP_STARTED=1): skip jobs another pool has started
    if os.environ.get('SIG_SKIP_STARTED') and os.path.exists(os.path.join(OUT, name + '.log')):
        return name + ' (started by another pool)'
    logf = open(os.path.join(OUT, name + '.log'), 'a')

    def log(msg):
        logf.write(time.strftime('%H:%M:%S ') + msg + '\n'); logf.flush()

    try:
        t_start = time.time()
        np.random.seed(seed)
        cfg = S.read_type_cfg(config)
        adv = adv_budget_of(dataset)
        g_ds = S.SignalingGame(dataset, budget, adv, cfg, payoff='dataset')
        g_zs = S.SignalingGame(dataset, budget, adv, cfg, payoff='zero_sum')
        general_sum = any(a.gain != a.loss for a in g_ds.type_models[0].attack_types)
        log(g_ds.describe())
        result = {'dataset': dataset, 'budget': budget, 'seed': seed, 'algo': ALGO,
                  'general_sum_distinct': general_sum, 'types': g_ds.describe()}

        if seed == 0:
            result['type_check'] = type_check(g_ds, FINAL_EPISODES)
            log('type check: ' + json.dumps(result['type_check']))

        fixed_rows, fixed_pols = fixed_attacker_study(g_ds, dataset, budget, seed, log)
        result['fixed_attacker'] = fixed_rows
        for p in fixed_pols.values():
            close_policy(p)

        runs = {'ZS_BLIND': (g_zs, 'blind')}
        if general_sum:
            runs['GS_BLIND'] = (g_ds, 'blind')
        runs['SIG'] = (g_ds, 'belief')
        do = {}
        for label, (g, kind) in runs.items():
            do[label] = double_oracle(g, kind, seed, label, log)
        result['do'] = {k: {kk: v[kk] for kk in ['def_s', 'att_s', 'payoff_def', 'payoff_atk',
                                                 'final_eq_def_loss', 'diag']} for k, v in do.items()}

        # C. cross evaluation on the dataset-payoff game (defender loss is the
        # same function in both games; only the attacker's gain differs)
        defenders = {k: S.Mix(v['def_pool'], v['def_s']) for k, v in do.items()}
        for bname, f in baseline_defenders(dataset, budget).items():
            defenders['baseline_' + bname] = f
        attackers = {k + '_attacker': S.Mix(v['atk_pool'], v['att_s']) for k, v in do.items()}
        attackers['fixed_uniform'] = S.FixedTypedAttacker([T.test_attack_action] * g_ds.K)
        cross = []
        for dn, d in defenders.items():
            for an, a in attackers.items():
                r = S.play(g_ds, d, a, FINAL_EPISODES, MAX_EP_STEPS, GAMMA, EVAL_SEED + 100)
                cross.append({'dataset': dataset, 'budget': budget, 'seed': seed, 'defender': dn,
                              'attacker': an, 'def_loss': float(r['def_loss'].mean()),
                              'def_loss_by_type': [float(r['def_loss'][r['thetas'] == k].mean()) for k in range(g_ds.K)],
                              'atk_util_dataset_payoff': float(r['atk_util'].mean())})
        result['cross'] = cross

        # D. belief diagnostics
        result['belief_diag'] = belief_diagnostics(g_ds, do['SIG'], FINAL_EPISODES,
                                                   os.path.join(OUT, name))
        result['seconds'] = time.time() - t_start
        json.dump(result, open(done_file + '.tmp', 'w'), indent=1, default=float)
        os.replace(done_file + '.tmp', done_file)
        log('DONE in {:.0f}s'.format(result['seconds']))
        return name + ' done in {:.0f}s'.format(result['seconds'])
    except Exception:
        log(traceback.format_exc())
        return name + ' FAILED:\n' + traceback.format_exc()


def run_sensitivity_job(job):
    """Sensitivity: how type separability changes the value of the belief (fixed attackers)."""
    dataset, budget, seed, sep = job
    name = 'sens_{}_{}_sep{}_s{}'.format(dataset, int(budget), sep, seed)
    os.makedirs(OUT, exist_ok=True)
    done_file = os.path.join(OUT, name + '.json')
    if os.path.exists(done_file):
        return name + ' (already done)'
    logf = open(os.path.join(OUT, name + '.log'), 'a')

    def log(msg):
        logf.write(time.strftime('%H:%M:%S ') + msg + '\n'); logf.flush()
    try:
        np.random.seed(seed)
        g = S.SignalingGame(dataset, budget, adv_budget_of(dataset), S.read_type_cfg(config),
                            payoff='dataset', separability=sep)
        rows, _ = fixed_attacker_study(g, dataset, budget, seed, log, extra={'separability': sep})
        json.dump({'rows': rows}, open(done_file, 'w'), indent=1)
        return name + ' done'
    except Exception:
        log(traceback.format_exc())
        return name + ' FAILED:\n' + traceback.format_exc()


def parse_list(key, cast=str):
    return [cast(x.strip()) for x in SG.get(key).split(',') if x.strip()]


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.WARNING)
    what = sys.argv[1] if len(sys.argv) > 1 else 'main'
    workers = int(os.environ.get('SIG_WORKERS', SG.getint('workers')))   # optional override
    seeds = list(range(SG.getint('n_seeds')))
    if what == 'main':
        jobs = []
        for s in seeds:                       # seed-major: whole seeds finish first
            for ds in parse_list('datasets'):
                for b in parse_list('budgets_' + ds, float):
                    jobs.append((ds, b, s))
        fn = run_job
    elif what == 'sensitivity':
        ds = SG.get('sens_dataset'); b = SG.getfloat('sens_budget')
        jobs = [(ds, b, s, sep) for sep in parse_list('sens_separability', float)
                for s in range(SG.getint('sens_seeds'))]
        fn = run_sensitivity_job
    else:
        raise SystemExit('usage: signaling_do.py [main|sensitivity]')
    if os.environ.get('SIG_REVERSE'):        # helper pool works from the end of the queue
        jobs = jobs[::-1]
    print('{} jobs, {} workers, oracle={}, out={}'.format(len(jobs), workers, ALGO, OUT), flush=True)
    with multiprocessing.Pool(workers, maxtasksperchild=1) as pool:
        for msg in pool.imap_unordered(fn, jobs):
            print(time.strftime('%Y-%m-%d %H:%M:%S'), msg, flush=True)
    print('ALL JOBS FINISHED', flush=True)
