#!/usr/bin/env python3
"""
SIGNALING-GAME EXTENSION of the alert-prioritisation model.

Plain-English summary
---------------------
* Nature secretly draws an attacker TYPE (e.g. "noisy" or "stealthy") at the
  start of every episode, using a prior such as 50/50.
* The attacker knows its type. Each type has its own alert "signature": for the
  same attack action it triggers different numbers/kinds of alerts. Loss, gain
  and cost of every attack action are identical across types.
* The defender only sees the alert counts N (the "signal"). It keeps a BELIEF
  b = P(type | all alerts seen so far) and updates it with Bayes' rule after
  every time step. Observing alerts is free; only investigating costs budget.
* Payoffs are computed by the unchanged Model.next_state() of model.py.

Nothing in model.py / test.py is changed. Every attacker type is simply a
separate Model object (same alert types, same budgets, different AttackType
alert probabilities). Each episode uses the Model of the type Nature drew.

All type parameters live in the [signaling] section of the config file
(see signaling_toy.conf / signaling_full.conf) and are turned into AttackType
objects by build_type_models() below.
"""

import itertools
import math
import os

import numpy as np
from scipy.special import gammaln, logsumexp

from model import Model, AttackType, PoissonDistribution
from listutils import flatten_lists, unflatten_list
import test as base_instances

# --------------------------------------------------------------------------
# 1. Datasets (the existing instances in test.py) and attacker types
# --------------------------------------------------------------------------

def base_model(dataset, def_budget, adv_budget):
    """Return the ORIGINAL (single attacker) model of test.py for a dataset."""
    if dataset == 'snort':
        return base_instances.test_model_snort(def_budget, adv_budget)
    if dataset == 'suricata':
        return base_instances.test_model_suricata(def_budget, adv_budget)
    if dataset == 'fraud':
        return base_instances.test_model_fraud(def_budget, adv_budget)
    raise ValueError('unknown dataset ' + dataset)


def _type_pr_alert(base_pr, fp_means, kind, scale, spread, separability):
    """
    Turn the base alert-trigger vector of ONE attack action into the vector of
    one attacker type.

    base_pr  : list, base_pr[t] = trigger value of alert type t (test.py).
               Values > 1 mean "this many alerts are raised" (snort/suricata),
               values <= 1 mean "probability of one alert" (fraud).
    fp_means : mean number of false alerts of every alert type.
    kind     : 'noisy'    -> more alerts, spread over ALL alert types
                            (a flooding / distraction attacker)
               'stealthy' -> fewer alerts, all on the alert type with the
                            HIGHEST false-alert rate (hides in the noise)
               'base'     -> unchanged
    scale    : total alert mass multiplier of this type.
    spread   : (noisy only) fraction of the mass spread uniformly over types.
    separability : 0 = type identical to base, 1 = full type definition.
                   Used only by the sensitivity study (linear interpolation).
    """
    base = np.array(base_pr, dtype=float)
    T = len(base)
    prob_mode = base.max() <= 1.0          # fraud-style probabilities
    if kind == 'base' or base.sum() == 0:
        new = base.copy()
    elif kind == 'noisy':
        if prob_mode:
            level = base.mean()
            new = scale * ((1 - spread) * base + spread * level)
        else:
            mass = base.sum()
            new = scale * ((1 - spread) * base + spread * mass / T)
    elif kind == 'stealthy':
        t_star = int(np.argmax(fp_means))      # noisiest alert type
        new = np.zeros(T)
        if prob_mode:
            new[t_star] = scale * base.max()
        else:
            new[t_star] = scale * base.sum()
    else:
        raise ValueError('unknown type kind ' + kind)
    new = (1 - separability) * base + separability * new
    if prob_mode:
        new = np.clip(new, 0.0, 0.95)
    else:
        new = np.round(new)                    # whole numbers of alerts
    return [float(x) for x in new]


class SignalingGame:
    """
    Container for one signaling-game instance.

    type_models[k] is a model.Model whose attack actions have the alert
    signature of attacker type k. prior[k] = P(type k).
    payoff = 'dataset'   -> loss/gain exactly as in test.py (general-sum where
                            test.py defines a separate gain, i.e. snort)
             'zero_sum'  -> attacker gain := defender loss (classic zero-sum)
    """

    def __init__(self, dataset, def_budget, adv_budget, type_cfg, payoff='dataset',
                 separability=1.0):
        self.dataset = dataset
        self.base = base_model(dataset, def_budget, adv_budget)
        self.alert_types = self.base.alert_types
        self.T = len(self.alert_types)
        self.A = len(self.base.attack_types)
        self.H = self.base.horizon
        assert self.H == 1, 'signaling extension assumes horizon 1 (true for all datasets)'
        for at in self.alert_types:
            assert isinstance(at.false_alerts, PoissonDistribution), 'Bayes filter needs Poisson false alerts'
        self.fp_means = np.array([at.false_alerts.mean for at in self.alert_types], dtype=float)
        self.type_names = type_cfg['types']
        self.K = len(self.type_names)
        assert 2 <= self.K <= 3
        self.prior = np.array(type_cfg['prior'], dtype=float)
        self.prior = self.prior / self.prior.sum()
        self.payoff = payoff
        self.type_models = []
        for name in self.type_names:
            kind = type_cfg['kind'][name]
            attacks = []
            for a in self.base.attack_types:
                pr = _type_pr_alert(a.pr_alert, self.fp_means, kind,
                                    type_cfg['scale'][name], type_cfg['spread'],
                                    separability)
                gain = list(a.loss) if payoff == 'zero_sum' else list(a.gain)
                # SAME loss, cost (and gain) for every type; only pr_alert differs.
                attacks.append(AttackType(list(a.loss), a.cost, pr, a.name + '_' + name, gain=gain))
            self.type_models.append(Model(self.H, self.alert_types, attacks,
                                          self.base.def_budget, self.base.adv_budget))

    def describe(self):
        lines = []
        for k, m in enumerate(self.type_models):
            lines.append('type {} ({}), prior {:.2f}:'.format(k, self.type_names[k], self.prior[k]))
            for a in m.attack_types:
                lines.append('   {:10s} loss={} gain={} cost={} pr_alert={}'.format(
                    a.name, a.loss, a.gain, a.cost, a.pr_alert))
        return '\n'.join(lines)


def read_type_cfg(config):
    """Read the [signaling] type parameters from the config file."""
    s = config['signaling']
    types = [x.strip() for x in s.get('types', 'noisy,stealthy').split(',')]
    prior = [float(x) for x in s.get('prior', '0.5,0.5').split(',')]
    assert len(prior) == len(types)
    cfg = {'types': types, 'prior': prior, 'kind': {}, 'scale': {},
           'spread': float(s.get('noisy_spread', '0.5'))}
    for name in types:
        cfg['kind'][name] = s.get(name + '_kind', name)
        cfg['scale'][name] = float(s.get(name + '_scale', '1.0'))
    return cfg

# --------------------------------------------------------------------------
# 2. Exact Bayes belief update
# --------------------------------------------------------------------------

BELIEF_FLOOR = 1e-9   # numerical floor so a belief never becomes exactly 0
ALPHA_TREMBLE = 1e-3  # see BeliefFilter.__init__


def poisson_logpmf(k, lam):
    """log P(K = k) for K ~ Poisson(lam); -inf for impossible k (k<0, or k>0 when lam=0)."""
    k = np.asarray(k, dtype=float)
    out = np.full(k.shape, -np.inf)
    ok = k >= 0
    if lam <= 0:
        out[ok & (k == 0)] = 0.0
        return out
    kk = k[ok]
    out[ok] = kk * math.log(lam) - lam - gammaln(kk + 1)
    return out


class BeliefFilter:
    """
    Exact Bayes filter over the attacker type.

    The likelihood of one step's alert counts N given type k is
        P(N | k) = sum over attack subsets S of P(S | k) * prod_t P(N_t | S, k)
    where
        P(S | k)        = prod_a alpha_hat[k][a]^[a in S] (1-alpha_hat[k][a])^[a not in S]
        N_t | S, k      = (false alerts ~ Poisson(lambda_t)) + (true alerts),
        true alerts     = sum over a in S of ceil(p_kat) with probability min(p_kat, 1)
    exactly as model.py generates them. alpha_hat[k] is the defender's
    conjecture about how often type k mounts each attack (for a fixed attacker
    it is exact; inside the double oracle it is the attack rate of the current
    equilibrium attacker mixture, see README). Everything is done in log space.
    """

    _next_id = 0

    def __init__(self, game, alpha_hat):
        self.game = game
        # "trembling hand": the conjectured attack rates are kept inside
        # [0.001, 0.999] so that no signal becomes impossible just because the
        # conjecture says an attack is mounted with probability exactly 0 or 1.
        self.alpha_hat = np.clip(np.array(alpha_hat, dtype=float), ALPHA_TREMBLE, 1 - ALPHA_TREMBLE)
        assert self.alpha_hat.shape == (game.K, game.A)
        self.id = BeliefFilter._next_id
        BeliefFilter._next_id += 1
        subsets = np.array(list(itertools.product([0, 1], repeat=game.A)), dtype=float)
        self.tables = []      # per type: (logPS, [per t: (row_index, support, logP_unique)])
        with np.errstate(divide='ignore'):
            for k, m in enumerate(game.type_models):
                al = self.alpha_hat[k]
                # log P(subset); np.where avoids 0*log(0)=NaN when alpha is exactly 0 or 1
                logPS = np.where(subsets == 1, np.log(al)[None, :], np.log(1 - al)[None, :]).sum(axis=1)
                per_t = []
                for t in range(game.T):
                    dists = []
                    for S in subsets:
                        d = {0: 1.0}
                        for a in range(game.A):
                            p = m.attack_types[a].pr_alert[t]
                            if S[a] == 0 or p <= 0:
                                continue
                            q, c = min(p, 1.0), int(math.ceil(p))
                            nd = {}
                            for v, pv in d.items():
                                nd[v] = nd.get(v, 0.0) + pv * (1 - q)
                                nd[v + c] = nd.get(v + c, 0.0) + pv * q
                            d = nd
                        dists.append(tuple(sorted(d.items())))
                    uniq = sorted(set(dists))
                    index = np.array([uniq.index(d) for d in dists])
                    support = np.array(sorted({v for d in uniq for v, _ in d}), dtype=float)
                    logP = np.full((len(uniq), len(support)), -np.inf)
                    for i, d in enumerate(uniq):
                        for v, pv in d:
                            if pv > 0:
                                logP[i, int(np.searchsorted(support, v))] = math.log(pv)
                    per_t.append((index, support, logP))
                self.tables.append((logPS, per_t))

    def loglik(self, N_now):
        """log P(alert counts of one step | type k) for every type k."""
        ll = np.zeros(self.game.K)
        for k, (logPS, per_t) in enumerate(self.tables):
            tot = logPS.copy()
            for t, (index, support, logP) in enumerate(per_t):
                lp = poisson_logpmf(N_now[t] - support, self.game.fp_means[t])
                tot = tot + logsumexp(logP + lp[None, :], axis=1)[index]
            ll[k] = logsumexp(tot)
        return ll

    def update(self, belief, N_now):
        """
        One Bayes step. Returns (new_belief, off_path).
        off_path is True when the observed alerts are impossible under EVERY
        type (zero likelihood). Bayes' rule is then undefined; we keep the
        previous belief (a common PBE off-path convention) and report it.
        """
        ll = self.loglik(N_now)
        with np.errstate(divide='ignore'):
            logpost = np.log(np.maximum(belief, 0.0)) + ll
        if not np.isfinite(logpost).any():
            return np.array(belief, dtype=float), True
        post = np.exp(logpost - logsumexp(logpost))
        post = np.maximum(post, BELIEF_FLOOR)
        return post / post.sum(), False

# --------------------------------------------------------------------------
# 3. Observations given to the neural networks
# --------------------------------------------------------------------------
# The same normalisation is used for EVERY condition (zero-sum, general-sum,
# signaling, blind, informed, belief), so it cannot create a gap by itself.
# Raw counts in snort are ~10 million which saturates the tanh layer; we use
# z-scores of the alert counts w.r.t. the false-alert distribution, clipped.

def norm_N(game, N_now):
    z = (np.asarray(N_now, dtype=float) - game.fp_means) / np.sqrt(game.fp_means + 1.0)
    return np.clip(z, -10.0, 10.0)


def defender_obs(game, state, kind, belief=None):
    """kind: 'blind' -> N only; 'belief' -> N + belief; 'informed' -> N + one-hot TRUE type."""
    obs = list(norm_N(game, state.N[0]))
    if kind == 'belief':
        obs += list(belief)
    elif kind == 'informed':
        obs += list(np.eye(game.K)[state.theta])
    return obs


def defender_obs_dim(game, kind):
    return game.T + (game.K if kind in ('belief', 'informed') else 0)


def attacker_obs(game, state):
    """System state (N, M, R) + one-hot of the attacker's own type."""
    obs = list(norm_N(game, state.N[0]))
    obs += [float(x) for x in flatten_lists(state.M)]
    obs += [float(np.sign(x)) for x in flatten_lists(flatten_lists(state.R))]
    obs += list(np.eye(game.K)[state.theta])
    return obs


def attacker_obs_dim(game):
    return game.T + game.A + game.A * game.T + game.K

# --------------------------------------------------------------------------
# 4. Episode mechanics (Nature draws the type; belief bookkeeping)
# --------------------------------------------------------------------------

def initial_state(game, theta=None):
    """Fresh state. Nature draws the hidden type unless theta is given."""
    s = Model.State(game.base)
    s.theta = int(np.random.choice(game.K, p=game.prior)) if theta is None else int(theta)
    s.is_initial = True        # alerts are all 0 here; not a real signal
    s.bcache = {}              # filter id -> belief at this state
    s.parent_bcache = None
    s.offpath = {}
    return s


def belief_of(game, state, filt):
    """Belief of filter `filt` at `state`, computed incrementally from the parent state."""
    if filt.id in state.bcache:
        return state.bcache[filt.id]
    if state.is_initial:
        b = game.prior.copy()
    else:
        prev = state.parent_bcache.get(filt.id) if state.parent_bcache is not None else None
        if prev is None:
            prev = game.prior.copy()     # only happens if a filter joins mid-episode
        b, off = filt.update(prev, state.N[0])
        state.offpath[filt.id] = off
    state.bcache[filt.id] = b
    return b


def step(game, mode, state, delta, alpha):
    """Advance one step using the Model of the hidden type (unchanged model.py dynamics)."""
    nxt = game.type_models[state.theta].next_state(mode, state, delta, alpha)
    nxt.theta = state.theta
    nxt.is_initial = False
    nxt.parent_bcache = state.bcache
    nxt.bcache = {}
    nxt.offpath = {}
    return nxt

# --------------------------------------------------------------------------
# 5. Policies
# --------------------------------------------------------------------------

class DefenderPolicy:
    """A trained defender network wrapped as a policy(model, state) -> delta."""

    def __init__(self, game, agent, kind, filt=None, label=''):
        self.game, self.agent, self.kind, self.filt, self.label = game, agent, kind, filt, label

    def obs(self, state):
        b = belief_of(self.game, state, self.filt) if self.kind == 'belief' else None
        return np.array(defender_obs(self.game, state, self.kind, b), dtype=np.float32)

    def action(self, state):
        return list(self.agent.ddpg.choose_action(self.obs(state)))

    def __call__(self, model, state):
        return model.make_investigation_feasible(state.N, unflatten_list(self.action(state), self.game.T))


class AttackerPolicy:
    """A trained type-conditioned attacker network wrapped as policy(model, state) -> alpha."""

    def __init__(self, game, agent, label=''):
        self.game, self.agent, self.label = game, agent, label

    def __call__(self, model, state):
        obs = np.array(attacker_obs(self.game, state), dtype=np.float32)
        return model.make_attack_feasible(list(self.agent.ddpg.choose_action(obs)))


class FixedTypedAttacker:
    """A non-learning attacker: type k plays fixed function fns[k](model, state)."""

    def __init__(self, fns, label='fixed'):
        self.fns, self.label = fns, label

    def __call__(self, model, state):
        return self.fns[state.theta](model, state)

# --------------------------------------------------------------------------
# 6. Simulation / evaluation
# --------------------------------------------------------------------------

def play(game, def_policy, atk_policy, n_episodes, n_steps, gamma, seed, mode='old',
         thetas=None, record=False):
    """
    Play n_episodes with the SAME random seed for every caller (common random
    numbers, so different defenders face identical type draws and noise).
    Returns dict with per-episode discounted defender LOSS, attacker utility,
    the mean attack probabilities per type, and optional trajectories.
    """
    rs = np.random.get_state()
    np.random.seed(seed)
    if thetas is None:
        # STRATIFIED type draws: exactly round(n * prior) episodes of each type,
        # in random order. An unstratified draw of 40 episodes can easily be
        # 65/35 instead of 50/50, which would evaluate a different game.
        counts = np.floor(n_episodes * game.prior).astype(int)
        for k in np.argsort(-(n_episodes * game.prior - counts))[:n_episodes - counts.sum()]:
            counts[k] += 1
        thetas = np.repeat(np.arange(game.K), counts)
        np.random.RandomState(seed + 104729).shuffle(thetas)
    def_loss, atk_util = np.zeros(n_episodes), np.zeros(n_episodes)
    alpha_sum = np.zeros((game.K, game.A))
    alpha_cnt = np.zeros(game.K)
    traj = []
    # mixed strategies are sampled per episode with a SEPARATE generator, so the
    # environment noise stays identical whichever policies are evaluated
    pick = np.random.RandomState(seed + 7919)
    for e in range(n_episodes):
        s = initial_state(game, thetas[e])
        dp = def_policy.policies[pick.choice(len(def_policy.policies), p=def_policy.probs)] \
            if isinstance(def_policy, Mix) else def_policy
        ap = atk_policy.policies[pick.choice(len(atk_policy.policies), p=atk_policy.probs)] \
            if isinstance(atk_policy, Mix) else atk_policy
        dl = au = 0.0
        rec = []
        for j in range(n_steps):
            # wrap the attacker so we can record the attack probabilities it chose
            box = {}

            def atk(model, state, _box=box):
                a = ap(model, state) if callable(ap) else list(ap)
                a = model.make_attack_feasible(a)
                _box['a'] = a
                return a
            nxt = step(game, mode, s, dp, atk)
            alpha_sum[s.theta] += np.array(box['a'])
            alpha_cnt[s.theta] += 1
            dl += gamma ** j * (nxt.U_defender - s.U_defender)
            au += gamma ** j * (nxt.U_attacker - s.U_attacker)
            if record:
                rec.append({'N': list(nxt.N[0]), 'alpha': box['a']})
            s = nxt
        def_loss[e], atk_util[e] = dl, au
        if record:
            traj.append({'theta': int(thetas[e]), 'steps': rec})
    np.random.set_state(rs)
    alpha_mean = alpha_sum / np.maximum(alpha_cnt[:, None], 1)
    return {'def_loss': def_loss, 'atk_util': atk_util, 'alpha_mean': alpha_mean,
            'thetas': np.array(thetas), 'traj': traj}


class Mix:
    """A mixed strategy: one pure policy is drawn per EPISODE with these probabilities."""

    def __init__(self, policies, probs):
        self.policies = list(policies)
        p = np.maximum(np.array(probs, dtype=float), 0)
        self.probs = p / p.sum()
