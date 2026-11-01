#!/usr/bin/env python3
"""
Summarise the signaling-game experiments: tables (CSV + Markdown) and figures (PNG).

Usage (from src/):  ../venv/bin/python signaling_analysis.py full     (or toy)
Reads  ../runs/<mode>/*.json   Writes ../results/<mode>/

Statistics
* Unit of replication = one random seed (one complete, independent training run).
  "n" in every table is the number of seeds.
* mean, standard deviation (ddof=1) and 95% confidence interval of the mean
  (Student t) of the DEFENDER LOSS = expected discounted loss per episode
  (gamma from the config), lower is better.
* Paired tests between conditions over seeds (same seed = same evaluation
  episodes): two-sided Wilcoxon signed-rank and paired t-test. Holm-Bonferroni
  adjusted p-values are given over all tests of a table.
"""
import glob
import json
import os
import sys

import numpy as np
from scipy import stats

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

MODE = sys.argv[1] if len(sys.argv) > 1 else 'full'
RUNS = os.path.join('..', 'runs', MODE)
OUT = os.path.join('..', 'results', MODE)
os.makedirs(OUT, exist_ok=True)
MD = []        # markdown report lines

COLORS = {'BLIND': '#4C72B0', 'INFORMED': '#55A868', 'BELIEF': '#C44E52',
          'ZS_BLIND': '#4C72B0', 'GS_BLIND': '#8172B2', 'SIG': '#C44E52'}


def ci(x):
    x = np.asarray(x, dtype=float)
    n = len(x)
    m = x.mean()
    if n < 2:
        return m, float('nan'), m, m
    sd = x.std(ddof=1)
    h = stats.t.ppf(0.975, n - 1) * sd / np.sqrt(n)
    return m, sd, m - h, m + h


def paired(a, b):
    """Two-sided paired tests of a vs b (arrays over the same seeds)."""
    a, b = np.asarray(a, float), np.asarray(b, float)
    d = a - b
    if len(d) < 2 or np.allclose(d, 0):
        return float('nan'), float('nan')
    try:
        w = stats.wilcoxon(a, b).pvalue
    except ValueError:
        w = float('nan')
    t = stats.ttest_rel(a, b).pvalue
    return float(w), float(t)


def holm(ps):
    ps = np.array(ps, dtype=float)
    out = np.full(len(ps), np.nan)
    ok = ~np.isnan(ps)
    idx = np.argsort(ps[ok])
    vals = ps[ok][idx]
    m = len(vals)
    adj = np.minimum(1, np.maximum.accumulate(vals * (m - np.arange(m))))
    tmp = np.empty(m)
    tmp[idx] = adj
    out[ok] = tmp
    return out


def write_csv(path, header, rows):
    with open(path, 'w') as f:
        f.write(','.join(header) + '\n')
        for r in rows:
            f.write(','.join(str(x) if not isinstance(x, float) else '{:.6g}'.format(x) for x in r) + '\n')


def md_table(header, rows):
    MD.append('| ' + ' | '.join(header) + ' |')
    MD.append('|' + '---|' * len(header))
    for r in rows:
        MD.append('| ' + ' | '.join('{:.3f}'.format(x) if isinstance(x, float) else str(x) for x in r) + ' |')
    MD.append('')

# --------------------------------------------------------------------------
jobs = [json.load(open(f)) for f in sorted(glob.glob(os.path.join(RUNS, '*.json')))
        if not os.path.basename(f).startswith('sens_')]
sens = [json.load(open(f)) for f in sorted(glob.glob(os.path.join(RUNS, 'sens_*.json')))]
datasets = [d for d in ['fraud', 'suricata', 'snort'] if any(j['dataset'] == d for j in jobs)]
MD.append('# Signaling-game results ({} mode)'.format(MODE))
MD.append('')
MD.append('Completed jobs: {} (dataset x budget x seed). Oracle: {}. '
          'Defender loss = expected discounted loss per episode, lower is better. '
          'n = number of independent seeds.'.format(len(jobs), jobs[0]['algo'] if jobs else '?'))
MD.append('')


def budgets(ds):
    return sorted({j['budget'] for j in jobs if j['dataset'] == ds})


def values(rows, ds, b, key_fn):
    """dict seed -> value for rows of dataset ds and budget b."""
    return {r['seed']: r['def_loss'] for r in rows if r['dataset'] == ds and r['budget'] == b and key_fn(r)}

# ------------------------- A. fixed-attacker study --------------------------
fixed = [r for j in jobs for r in j['fixed_attacker']]
defenders_fixed = []
for r in fixed:
    if r['defender'] not in defenders_fixed:
        defenders_fixed.append(r['defender'])
rows = []
for ds in datasets:
    for b in budgets(ds):
        for dn in defenders_fixed:
            v = values(fixed, ds, b, lambda r: r['defender'] == dn)
            if v:
                m, sd, lo, hi = ci(list(v.values()))
                rows.append([ds, b, dn, len(v), m, sd, lo, hi])
write_csv(os.path.join(OUT, 'fixed_attacker_summary.csv'),
          ['dataset', 'budget', 'defender', 'n', 'mean_loss', 'std', 'ci95_lo', 'ci95_hi'], rows)
MD.append('## A. Defenders against FIXED type-based attackers (conditions a, b, c + baselines)')
MD.append('')
md_table(['dataset', 'budget', 'defender', 'n', 'mean loss', 'std', 'CI low', 'CI high'], rows)

tests = []
for ds in datasets:
    for b in budgets(ds):
        for x, y in [('BELIEF', 'BLIND'), ('INFORMED', 'BLIND'), ('BELIEF', 'INFORMED')]:
            vx = values(fixed, ds, b, lambda r: r['defender'] == x)
            vy = values(fixed, ds, b, lambda r: r['defender'] == y)
            s = sorted(set(vx) & set(vy))
            a, c = [vx[k] for k in s], [vy[k] for k in s]
            w, t = paired(a, c)
            tests.append([ds, b, x + ' - ' + y, len(s), float(np.mean(np.subtract(a, c))) if s else float('nan'), w, t])
adj = holm([t[5] for t in tests])
tests = [t + [float(a)] for t, a in zip(tests, adj)]
write_csv(os.path.join(OUT, 'fixed_attacker_tests.csv'),
          ['dataset', 'budget', 'comparison', 'n', 'mean_diff_loss', 'wilcoxon_p', 'paired_t_p', 'wilcoxon_p_holm'], tests)
MD.append('Paired tests (negative mean difference = first defender has LOWER loss):')
MD.append('')
md_table(['dataset', 'budget', 'comparison', 'n', 'mean diff', 'Wilcoxon p', 't-test p', 'Wilcoxon p (Holm)'], tests)

for ds in datasets:
    fig, ax = plt.subplots(figsize=(6, 4))
    for dn in defenders_fixed:
        pts = [(r[1], r[4], r[4] - r[6], r[7] - r[4]) for r in rows if r[0] == ds and r[2] == dn]
        if not pts:
            continue
        pts = np.array(pts)
        ls = '-' if dn in COLORS else ':'
        ax.errorbar(pts[:, 0], pts[:, 1], yerr=[pts[:, 2], pts[:, 3]], label=dn.replace('baseline_', ''),
                    color=COLORS.get(dn), ls=ls, marker='o', capsize=3, lw=2 if dn in COLORS else 1)
    ax.set_xlabel('defender budget'); ax.set_ylabel('defender loss (lower is better)')
    ax.set_title('{}: fixed type-based attackers (95% CI over seeds)'.format(ds))
    ax.legend(fontsize=7); fig.tight_layout()
    fig.savefig(os.path.join(OUT, 'fixed_loss_vs_budget_{}.png'.format(ds)), dpi=150); plt.close(fig)

# ------------------------- B/C. double-oracle games ------------------------
cross = [r for j in jobs for r in j['cross']]
conds = [c for c in ['ZS_BLIND', 'GS_BLIND', 'SIG'] if any(c in j['do'] for j in jobs)]
attackers = []
for r in cross:
    if r['attacker'] not in attackers:
        attackers.append(r['attacker'])
defs_cross = []
for r in cross:
    if r['defender'] not in defs_cross:
        defs_cross.append(r['defender'])

MD.append('## B. Equilibrium (double oracle) results: zero-sum vs general-sum vs signaling')
MD.append('')
MD.append('For suricata and fraud test.py defines no separate attacker gain, so the general-sum '
          'game equals the zero-sum game and GS_BLIND is not run separately; there SIG differs '
          'from ZS_BLIND ONLY by the belief/types. Snort has distinct gains.')
MD.append('')
eqrows = []
for ds in datasets:
    for b in budgets(ds):
        for c in conds:
            v = {j['seed']: j['do'][c]['final_eq_def_loss'] for j in jobs
                 if j['dataset'] == ds and j['budget'] == b and c in j['do']}
            if v:
                m, sd, lo, hi = ci(list(v.values()))
                its = [len(j['do'][c]['diag']) for j in jobs if j['dataset'] == ds and j['budget'] == b and c in j['do']]
                eqrows.append([ds, b, c, len(v), m, sd, lo, hi, float(np.mean(its))])
write_csv(os.path.join(OUT, 'equilibrium_value_summary.csv'),
          ['dataset', 'budget', 'game', 'n', 'mean_eq_def_loss', 'std', 'ci95_lo', 'ci95_hi', 'mean_iterations'], eqrows)
MD.append('### B1. Defender loss at the restricted-game equilibrium (each game against its OWN attacker)')
MD.append('')
MD.append('Caution: these are values of DIFFERENT games (the attacker objective differs between '
          'zero-sum and general-sum), so they are not a like-for-like comparison of defenders; see B2.')
MD.append('')
md_table(['dataset', 'budget', 'game', 'n', 'mean loss', 'std', 'CI low', 'CI high', 'DO iterations'], eqrows)

crows = []
for ds in datasets:
    for b in budgets(ds):
        for dn in defs_cross:
            for an in attackers:
                v = values(cross, ds, b, lambda r: r['defender'] == dn and r['attacker'] == an)
                if v:
                    m, sd, lo, hi = ci(list(v.values()))
                    crows.append([ds, b, dn, an, len(v), m, sd, lo, hi])
write_csv(os.path.join(OUT, 'cross_evaluation_summary.csv'),
          ['dataset', 'budget', 'defender', 'attacker', 'n', 'mean_loss', 'std', 'ci95_lo', 'ci95_hi'], crows)
MD.append('### B2. Cross-evaluation: every final defender against the SAME attackers')
MD.append('')
MD.append('Defender = final equilibrium defender mixture of each game (or a baseline). '
          'Attacker = final equilibrium attacker mixture of each game, or the fixed uniform attacker. '
          'Same evaluation episodes for all (common random numbers). "worst" = max over the attackers.')
MD.append('')
# compact table: rows (ds,b,defender), columns attackers + worst
hdr = ['dataset', 'budget', 'defender'] + attackers + ['worst']
compact = []
worst_vals = {}
for ds in datasets:
    for b in budgets(ds):
        for dn in defs_cross:
            line = [ds, b, dn]
            per_seed_worst = {}
            for an in attackers:
                v = values(cross, ds, b, lambda r: r['defender'] == dn and r['attacker'] == an)
                line.append(float(np.mean(list(v.values()))) if v else '')
                for s_, x in v.items():
                    per_seed_worst[s_] = max(per_seed_worst.get(s_, -np.inf), x)
            worst_vals[(ds, b, dn)] = per_seed_worst
            line.append(float(np.mean(list(per_seed_worst.values()))) if per_seed_worst else '')
            compact.append(line)
md_table(hdr, compact)

ctests = []
for ds in datasets:
    for b in budgets(ds):
        for other in [c for c in conds if c != 'SIG'] + [d for d in defs_cross if d.startswith('baseline_')]:
            for an in attackers + ['worst']:
                if an == 'worst':
                    vx, vy = worst_vals.get((ds, b, 'SIG'), {}), worst_vals.get((ds, b, other), {})
                else:
                    vx = values(cross, ds, b, lambda r: r['defender'] == 'SIG' and r['attacker'] == an)
                    vy = values(cross, ds, b, lambda r: r['defender'] == other and r['attacker'] == an)
                s = sorted(set(vx) & set(vy))
                if not s:
                    continue
                a, c = [vx[k] for k in s], [vy[k] for k in s]
                w, t = paired(a, c)
                ctests.append([ds, b, 'SIG - ' + other, an, len(s), float(np.mean(np.subtract(a, c))),
                               float(np.mean(np.subtract(a, c)) / np.mean(c) * 100) if np.mean(c) != 0 else float('nan'), w, t])
adj = holm([t[7] for t in ctests])
ctests = [t + [float(a)] for t, a in zip(ctests, adj)]
write_csv(os.path.join(OUT, 'cross_evaluation_tests.csv'),
          ['dataset', 'budget', 'comparison', 'attacker', 'n', 'mean_diff_loss', 'pct_diff', 'wilcoxon_p', 'paired_t_p', 'wilcoxon_p_holm'], ctests)
MD.append('Paired tests SIG defender vs other defenders (negative = SIG has LOWER loss). '
          'Only comparisons against the learned defenders are shown here; all (incl. baselines) are in cross_evaluation_tests.csv.')
MD.append('')
md_table(['dataset', 'budget', 'comparison', 'attacker', 'n', 'mean diff', '% diff', 'Wilcoxon p', 't p', 'Wilcoxon p (Holm)'],
         [t for t in ctests if 'baseline' not in t[2]])

# loss vs budget plots for the DO games: own-equilibrium value and vs SIG attacker
for ds in datasets:
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))
    for c in conds:
        pts = np.array([(r[1], r[4], r[4] - r[6], r[7] - r[4]) for r in eqrows if r[0] == ds and r[2] == c])
        if len(pts):
            axes[0].errorbar(pts[:, 0], pts[:, 1], yerr=[pts[:, 2], pts[:, 3]], label=c, color=COLORS[c], marker='o', capsize=3)
    axes[0].set_title('{}: equilibrium defender loss\n(each game vs its own attacker)'.format(ds))
    for ax, an, title in [(axes[1], 'SIG_attacker', 'vs signaling-game attacker'), (axes[2], 'worst', 'worst case over all attackers')]:
        for dn in defs_cross:
            if an == 'worst':
                pts = []
                for b in budgets(ds):
                    v = list(worst_vals.get((ds, b, dn), {}).values())
                    if v:
                        m, sd, lo, hi = ci(v); pts.append((b, m, m - lo, hi - m))
                pts = np.array(pts)
            else:
                pts = np.array([(r[1], r[5], r[5] - r[7], r[8] - r[5]) for r in crows if r[0] == ds and r[2] == dn and r[3] == an])
            if len(pts):
                ax.errorbar(pts[:, 0], pts[:, 1], yerr=[np.nan_to_num(pts[:, 2]), np.nan_to_num(pts[:, 3])],
                            label=dn.replace('baseline_', ''), color=COLORS.get(dn),
                            ls='-' if dn in COLORS else ':', marker='o', capsize=3, lw=2 if dn in COLORS else 1)
        ax.set_title('{}: defender loss {}'.format(ds, title))
    for ax in axes:
        ax.set_xlabel('defender budget'); ax.set_ylabel('defender loss (lower is better)'); ax.legend(fontsize=7)
    fig.tight_layout(); fig.savefig(os.path.join(OUT, 'do_loss_vs_budget_{}.png'.format(ds)), dpi=150); plt.close(fig)

# convergence diagnostics
fig, axes = plt.subplots(1, len(datasets), figsize=(5 * len(datasets), 4), squeeze=False)
convrows = []
for i, ds in enumerate(datasets):
    ax = axes[0][i]
    for c in conds:
        series = [[d['exploitability'] for d in j['do'][c]['diag']] for j in jobs if j['dataset'] == ds and c in j['do']]
        if not series:
            continue
        L = max(len(s) for s in series)
        mean, lo, hi = [], [], []
        for it in range(L):
            v = [s[it] for s in series if len(s) > it]
            m, sd, l, h = ci(v)
            mean.append(m); lo.append(l if len(v) > 1 else m); hi.append(h if len(v) > 1 else m)
            convrows.append([ds, c, it, len(v), m, sd])
        ax.plot(range(L), mean, marker='o', label=c, color=COLORS[c])
        ax.fill_between(range(L), lo, hi, color=COLORS[c], alpha=0.15)
    ax.set_title('{}: double-oracle convergence (all budgets)'.format(ds))
    ax.set_xlabel('iteration'); ax.set_ylabel('best-response improvement\n(def gain+ + atk gain+)'); ax.legend()
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'do_convergence.png'), dpi=150); plt.close(fig)
write_csv(os.path.join(OUT, 'do_convergence.csv'), ['dataset', 'game', 'iteration', 'n_runs', 'mean_exploitability', 'std'], convrows)

# ------------------------------ D. beliefs ---------------------------------
MD.append('## C. Belief diagnostics (signaling game, final equilibrium)')
MD.append('')
brows = []
for ds in datasets:
    for b in budgets(ds):
        d = [j['belief_diag'] for j in jobs if j['dataset'] == ds and j['budget'] == b and 'mean_abs_belief_diff_vs_exact_bayes' in j['belief_diag']]
        nb = sum(1 for j in jobs if j['dataset'] == ds and j['budget'] == b and 'note' in j['belief_diag'])
        if d:
            brows.append([ds, b, len(d), nb,
                          float(np.mean([x['mean_abs_belief_diff_vs_exact_bayes'] for x in d])),
                          float(np.mean([x['offpath_rate_defender_filter'] for x in d])),
                          float(np.mean([x['offpath_rate_exact_filter'] for x in d])),
                          float(np.mean([x['mean_final_belief_on_true_type'] for x in d]))])
        elif nb:
            brows.append([ds, b, 0, nb, '', '', '', ''])
write_csv(os.path.join(OUT, 'belief_diagnostics.csv'),
          ['dataset', 'budget', 'n_with_belief_policy', 'n_without_belief_policy_in_support', 'mean_abs_diff_vs_exact_bayes',
           'offpath_rate_defender', 'offpath_rate_exact', 'final_belief_on_true_type'], brows)
md_table(['dataset', 'budget', 'n (belief policy in support)', 'n (no belief policy in support)',
          '|b_def - b_exactBayes|', 'off-path rate (def. conjecture)', 'off-path rate (exact)', 'final belief on true type'], brows)

# calibration plot + belief trajectories
fig, axes = plt.subplots(1, len(datasets), figsize=(5 * len(datasets), 4), squeeze=False)
for i, ds in enumerate(datasets):
    ax = axes[0][i]
    cal = [c for j in jobs if j['dataset'] == ds for c in j['belief_diag'].get('calibration_type0', [])]
    if cal:
        cal = np.array(cal)
        bins = sorted(set(cal[:, 0]))
        xs, ys, ns = [], [], []
        for lo in bins:
            m = cal[:, 0] == lo
            w = cal[m, 2]
            xs.append(np.average(cal[m, 3], weights=w)); ys.append(np.average(cal[m, 4], weights=w)); ns.append(w.sum())
        ax.scatter(xs, ys, s=10 + 90 * np.array(ns) / max(ns), color='#C44E52')
    ax.plot([0, 1], [0, 1], 'k--', lw=1)
    ax.set_xlabel('defender belief P(type = {})'.format('noisy')); ax.set_ylabel('empirical frequency of that type')
    ax.set_title('{}: belief calibration (all runs)'.format(ds))
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'belief_calibration.png'), dpi=150); plt.close(fig)

fig, axes = plt.subplots(1, len(datasets), figsize=(5 * len(datasets), 4), squeeze=False)
for i, ds in enumerate(datasets):
    ax = axes[0][i]
    bs = budgets(ds)
    if not bs:
        continue
    b = bs[len(bs) // 2]
    f = os.path.join(RUNS, '{}_{}_s0_belief_traj.csv'.format(ds, int(b)))
    if not os.path.exists(f):
        continue
    t = np.genfromtxt(f, delimiter=',', names=True)
    for e in range(6):
        m = t['episode'] == e
        if m.sum() == 0:
            continue
        th = int(t['true_type'][m][0])
        p_true = t['def_b{}'.format(th)][m]
        ax.plot(t['step'][m], p_true, color=['#E17C05', '#5F4690'][th % 2], alpha=0.8,
                label='true type = {}'.format(['noisy', 'stealthy', 'type2'][th]))
    h, l = ax.get_legend_handles_labels()
    uniq = dict(zip(l, h))
    ax.legend(uniq.values(), uniq.keys(), fontsize=8)
    ax.set_ylim(-0.02, 1.02); ax.set_xlabel('time step'); ax.set_ylabel('defender belief in the TRUE type')
    ax.set_title('{} (budget {}): belief trajectories, seed 0'.format(ds, int(b)))
fig.tight_layout(); fig.savefig(os.path.join(OUT, 'belief_trajectories.png'), dpi=150); plt.close(fig)

# behaviour at beliefs (off-path behaviour), seed 0 middle budget
MD.append('### Investigation split of the main belief policy at different beliefs (seed 0, middle budget)')
MD.append('')
MD.append('Shows how the learned defender reacts to its belief, including beliefs it rarely or never '
          'reaches on the equilibrium path (off-path behaviour).')
MD.append('')
for ds in datasets:
    bs = budgets(ds)
    j0 = [j for j in jobs if j['dataset'] == ds and j['seed'] == 0 and j['budget'] == bs[len(bs) // 2]]
    if j0 and 'behaviour_at_beliefs' in j0[0]['belief_diag']:
        rows_b = [[ds, x['alerts_like_type'], x['belief'], ' / '.join('{:.2f}'.format(v) for v in x['investigation_share'])]
                  for x in j0[0]['belief_diag']['behaviour_at_beliefs']]
        md_table(['dataset', 'alert counts typical of', 'belief', 'budget share per alert type'], rows_b)

# ------------------------------ type check ---------------------------------
MD.append('## D. Do the types call for different investigation patterns?')
MD.append('')
MD.append('Best static budget split per type against the fixed uniform attacker (seed-0 jobs), '
          'and the loss when the OTHER type\'s best split is used instead.')
MD.append('')
trows = []
for j in jobs:
    if 'type_check' in j:
        for tname, v in j['type_check'].items():
            for o, l in v['loss_using_other_types_best_split'].items():
                trows.append([j['dataset'], j['budget'], tname, v['best_split'], v['best_loss'], o, l])
write_csv(os.path.join(OUT, 'type_check.csv'), ['dataset', 'budget', 'type', 'best_split', 'best_loss', 'other_type', 'loss_with_other_types_split'], trows)
md_table(['dataset', 'budget', 'type', 'best split', 'loss', 'other type', "loss with other type's split"], trows)

# ------------------------------ sensitivity ---------------------------------
if sens:
    MD.append('## E. Sensitivity: type separability vs value of the belief (fixed attackers)')
    MD.append('')
    srows_all = [r for s in sens for r in s['rows']]
    seps = sorted({r['separability'] for r in srows_all})
    srows = []
    fig, ax = plt.subplots(figsize=(6, 4))
    for x in ['BELIEF', 'INFORMED']:
        pts = []
        for sp in seps:
            vb = {r['seed']: r['def_loss'] for r in srows_all if r['separability'] == sp and r['defender'] == 'BLIND'}
            vx = {r['seed']: r['def_loss'] for r in srows_all if r['separability'] == sp and r['defender'] == x}
            s_ = sorted(set(vb) & set(vx))
            gain = [vb[k] - vx[k] for k in s_]
            m, sd, lo, hi = ci(gain)
            w, t = paired([vx[k] for k in s_], [vb[k] for k in s_])
            srows.append([sens[0]['rows'][0]['dataset'], sens[0]['rows'][0]['budget'], sp, 'BLIND - ' + x, len(s_), m, sd, lo, hi, w, t])
            pts.append((sp, m, m - lo if len(s_) > 1 else 0, hi - m if len(s_) > 1 else 0))
        pts = np.array(pts)
        ax.errorbar(pts[:, 0], pts[:, 1], yerr=[pts[:, 2], pts[:, 3]], label='loss reduction of ' + x + ' vs BLIND',
                    color=COLORS[x], marker='o', capsize=3)
    ax.axhline(0, color='k', lw=1)
    ax.set_xlabel('type separability (0 = identical types, 1 = full definition)')
    ax.set_ylabel('BLIND loss - other loss (higher = better)')
    ax.set_title('Sensitivity ({}, budget {})'.format(sens[0]['rows'][0]['dataset'], int(sens[0]['rows'][0]['budget'])))
    ax.legend(fontsize=8); fig.tight_layout()
    fig.savefig(os.path.join(OUT, 'sensitivity_separability.png'), dpi=150); plt.close(fig)
    write_csv(os.path.join(OUT, 'sensitivity_separability.csv'),
              ['dataset', 'budget', 'separability', 'difference', 'n', 'mean', 'std', 'ci95_lo', 'ci95_hi', 'wilcoxon_p', 'paired_t_p'], srows)
    md_table(['dataset', 'budget', 'separability', 'difference', 'n', 'mean', 'std', 'CI low', 'CI high', 'Wilcoxon p', 't p'], srows)

open(os.path.join(OUT, 'RESULTS.md'), 'w').write('\n'.join(MD) + '\n')
print('wrote', OUT)
