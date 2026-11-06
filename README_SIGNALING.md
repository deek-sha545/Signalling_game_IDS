# Alert prioritisation as a SIGNALING GAME

This branch (`signaling`) extends the general-sum alert-prioritisation code (Tong et al. 2019
"AlertPrioritization", SAC-AP) into a **signaling game**. In it, the attacker has a hidden
*type* and the defender has to infer that type from the alerts. Everything in the original
code still runs unchanged. The new code is in separate files (see `SIGNALING_NOTES.md`).

---

## 1. The model in plain English

**The setting.** An intrusion-detection system raises thousands of alerts per time step,
mostly false. A security team (the *defender*) can only investigate a limited number per
step (budget B). An *attacker* mounts attacks that trigger some of these alerts. An attack
that is not investigated causes a loss.

**Players and what they know.**

| | Attacker | Defender |
|---|---|---|
| Knows its own type? | yes | **no** |
| Sees | the full system state (alerts, which attacks are live, which alerts are real) and its type | only the **alert counts per alert type** (the *signal*) |
| Chooses each step | probability of mounting each attack (within attack budget D) | how many alerts of each type to investigate (within budget B) |

**Types (who the attacker is).** At the start of every episode, *Nature* secretly draws
the attacker's type from a prior (default 50% / 50%; up to 3 types are supported):

* **Noisy / flooding.** Each attack raises *twice as many* alerts as in the original data,
  and half of them are spread across *all* alert types. Loud, and it acts as a distraction.
* **Stealthy.** Each attack raises *half as many* alerts, all of them in the alert type that
  already has the *most false alarms*. It hides in the noise.

Both types have exactly the same attack actions, losses, gains and costs. Only *which and
how many alerts* their attacks trigger differs. All type parameters are in the `[signaling]`
section of `src/signaling_toy.conf` / `src/signaling_full.conf`.

**Belief.** After every step the defender updates its belief
b = P(type | all alert counts seen so far) with **Bayes' rule**:

    b_new(type) ∝ b_old(type) × P(alert counts this step | type)

The likelihood P(alert counts | type) is computed *exactly* from the model's own rules:
false alerts are Poisson, and each attack adds alerts with the type's trigger probabilities.
That means summing over every combination of attacks that could be live. It is computed in
log space so the 10-million-alert snort counts don't overflow. Observing alerts is free;
only investigating costs budget.

**Payoffs.** Unchanged from the existing code (`Model.next_state`). The defender loses
L_a for every step an attack a stays undetected. The attacker gets gain_a minus the cost
of the attacks it mounts. In **zero-sum** mode gain = loss. In **general-sum** mode the
gains from `test.py` are used (only snort has separate gains; for suricata and fraud the
two modes coincide).

**Policies (learned by deep RL).**
* Defender network input: alert counts + belief (BELIEF/SIG), alert counts only (BLIND),
  or alert counts + the *true* type (INFORMED, a cheating upper bound).
* Attacker network input: system state + one-hot of its own type. It can therefore behave
  differently per type, for example imitate the other type's alert signature ("pooling").

**Equilibrium concept and how it is approximated.** The right solution concept for a
signaling game is a *perfect Bayesian equilibrium* (PBE). In a PBE, each type's strategy is a
best response, the defender's strategy is a best response given its beliefs, and the beliefs
follow Bayes' rule from the attacker's strategy wherever possible. We approximate it with the
existing **double-oracle** loop:

1. Keep a pool of attacker policies (type-conditioned) and defender policies (belief-conditioned).
2. Compute a mixed Nash equilibrium of the small matrix game between the pools (nashpy,
   same `defender_max` / `welfare_max` options as before).
3. Train a new attacker best response and a new defender best response with RL against the
   current mixture and add them to the pools. The defender's Bayes filter uses the attack rates
   of the current equilibrium attacker mixture (its "conjecture").
4. Repeat until neither new best response improves on the equilibrium, or a maximum number of iterations.

**This is an approximation, not a proof of a PBE.** (i) RL best responses are approximate.
(ii) The double oracle is stopped after a few iterations. (iii) The defender's Bayes filter
uses each type's *average* attack rate, because the attacker reacts to state the defender
cannot see. (iv) Off-path beliefs follow a fixed convention (keep the previous belief) with
a small "trembling hand" (attack rates conjectured in [0.001, 0.999]). We check (iii) and
(iv) empirically: the belief diagnostics compare the defender's belief with exact Bayes on
the attacker's realised behaviour, and report calibration and off-path frequencies.

---

## 2. Experimental conditions

All conditions use the same datasets, budgets, seeds, evaluation episodes, network sizes and
training length (`src/signaling_full.conf`).

| Name | What it is |
|---|---|
| **BLIND** (a) | Existing general-sum style defender: sees alert counts only. |
| **INFORMED** (b) | Defender is told the true type (cheating upper bound). |
| **BELIEF** (c) | Defender sees alert counts + Bayes belief; attackers are fixed. |
| **ZS_BLIND** | Double oracle, **zero-sum** payoffs, blind defender: the SAC-AP zero-sum approach re-run in the two-type world. |
| **GS_BLIND** | Double oracle, general-sum payoffs, blind defender (snort only; identical to ZS_BLIND elsewhere). |
| **SIG** (d) | Double oracle, full **signaling game**: type-conditioned learning attacker vs belief defender. |
| Baselines | uniform, newest, proportion, Snort/Suricata priority rules, fraud rule, aics, icde (where `test.py` supports them). |

In (a)–(c) each type plays the existing uniform attacker, so the types differ only in their
alert signature.

The **headline comparison** is the *cross-evaluation*: the final defender of each game is
played against the *same* attackers (each game's final attacker and the fixed attacker),
on identical episodes. Comparing the equilibrium values of different games directly is not
fair, because a zero-sum attacker tries harder to hurt the defender than a general-sum one.

---

## 3. How to reproduce

```bash
git clone https://github.com/deek-sha545/Signalling_game_IDS.git ids-signaling
cd ids-signaling && git checkout signaling
~/.pyenv/versions/3.7.17/bin/python -m venv venv
venv/bin/pip install tensorflow==1.13.1 "protobuf<3.21" numpy==1.21.6 scipy==1.7.3 nashpy==0.0.17
venv/bin/pip freeze > /tmp/c.txt && venv/bin/pip install matplotlib==3.5.3 -c /tmp/c.txt

./run_signaling.sh toy      # a few minutes: unit tests + whole pipeline at tiny scale
./run_signaling.sh full     # the paper results (about 12-15 h on 8 cores)
```

To run it in the background with a log, as was done for the results below:

```bash
nohup ./run_signaling.sh full > logs/full_run.log 2>&1 & disown
```

* Unit tests only: `cd src && IDS_CONFIG=signaling_toy.conf ../venv/bin/python -m unittest test_signaling_belief -v`
* Choose the RL algorithm: `oracle_algo = ddpg | sac | td3` in the config.
* The original (non-signaling) pipeline is unchanged: `cd src && python -u double_oracle.py snort 1000 125 1`
  (reads `project.conf`; `IDS_CONFIG=<file>` selects another config).
* Raw per-job outputs: `runs/full_v2/` (not in git) (JSON, logs, belief trajectories).
  Tables and figures: `results/full_v2/` (`RESULTS.md` has every table).

---

## 4. Results

> **Status: FINAL results, all 90 main jobs (3 datasets x 3 budgets x 10 seeds) and the sensitivity study finished on 2026-11-01.**

Loss = expected discounted defender loss per episode (lower is better). Mean ± std over independent seeds (n). Full tables with 95% CIs: [`results/full_v2/RESULTS.md`](results/full_v2/RESULTS.md); raw CSVs and figures are in `results/full_v2/`.

### 4.1 Does the belief help against FIXED type-based attackers? (conditions a, b, c)

| dataset | B | n | BLIND | BELIEF | INFORMED (upper bound) | best rule baseline | BELIEF−BLIND | paired t p | Wilcoxon p |
|---|---|---|---|---|---|---|---|---|---|
| suricata | 500 | 10 | 70.6 ± 2.2 | 62.4 ± 1.4 | 61.3 ± 0.9 | 88.5 (suricata_rule) | -8.2 | <0.001 | 0.002 |
| suricata | 1000 | 10 | 55.6 ± 2.1 | 45.4 ± 0.8 | 44.3 ± 1.1 | 76.8 (suricata_rule) | -10.2 | <0.001 | 0.002 |
| suricata | 1500 | 10 | 48.6 ± 1.6 | 38.9 ± 1.3 | 37.4 ± 1.4 | 69.2 (suricata_rule) | -9.7 | <0.001 | 0.002 |
| fraud | 10 | 10 | 198.9 ± 5.8 | 197.7 ± 1.9 | 190.6 ± 4.5 | 229.8 (uniform) | -1.1 | 0.604 | 0.779 |
| fraud | 20 | 10 | 179.2 ± 2.2 | 173.4 ± 5.3 | 154.8 ± 2.3 | 194.5 (fraud_rule) | -5.8 | 0.004 | 0.010 |
| fraud | 30 | 10 | 156.8 ± 8.3 | 149.2 ± 3.2 | 134.3 ± 2.5 | 157.0 (fraud_rule) | -7.5 | 0.010 | 0.014 |
| snort | 500 | 10 | 33.0 ± 1.6 | 32.4 ± 0.2 | 32.4 ± 0.0 | 32.3 (uniform) | -0.5 | 0.319 | 0.770 |
| snort | 1000 | 10 | 30.0 ± 2.8 | 28.9 ± 0.0 | 29.3 ± 1.1 | 28.9 (uniform) | -1.1 | 0.246 | 0.036 |
| snort | 1500 | 10 | 26.8 ± 0.6 | 26.6 ± 0.0 | 27.0 ± 1.3 | 26.6 (uniform) | -0.2 | 0.353 | 0.593 |

### 4.2 Signaling game vs zero-sum game (double oracle, cross-evaluation)

Each game's final defender is played against the same attackers on identical episodes. "worst" = the defender's worst loss over the three attackers. Negative difference = the signaling defender loses less.

| dataset | B | n | attacker | ZS_BLIND defender | SIG defender | SIG − ZS | % | paired t p | Wilcoxon p |
|---|---|---|---|---|---|---|---|---|---|
| suricata | 500 | 10 | SIG_attacker | 40.1 | 38.2 | -1.87 | -4.7% | 0.391 | 0.515 |
| suricata | 500 | 10 | ZS_BLIND_attacker | 38.5 | 40.4 | +1.91 | +5.0% | 0.295 | 0.678 |
| suricata | 500 | 10 | fixed_uniform | 88.3 | 86.2 | -2.13 | -2.4% | 0.317 | 0.232 |
| suricata | 500 | 10 | worst | – | – | -2.13 | -2.4% | 0.317 | 0.232 |
| suricata | 1000 | 10 | SIG_attacker | 34.3 | 34.6 | +0.29 | +0.9% | 0.176 | 0.322 |
| suricata | 1000 | 10 | ZS_BLIND_attacker | 34.3 | 34.6 | +0.29 | +0.9% | 0.176 | 0.322 |
| suricata | 1000 | 10 | fixed_uniform | 76.3 | 70.2 | -6.11 | -8.0% | 0.136 | 0.160 |
| suricata | 1000 | 10 | worst | – | – | -6.11 | -8.0% | 0.136 | 0.160 |
| suricata | 1500 | 10 | SIG_attacker | 33.0 | 31.0 | -1.92 | -5.8% | 0.510 | 0.432 |
| suricata | 1500 | 10 | ZS_BLIND_attacker | 33.3 | 36.5 | +3.24 | +9.7% | 0.217 | 0.064 |
| suricata | 1500 | 10 | fixed_uniform | 68.1 | 62.4 | -5.69 | -8.4% | 0.325 | 0.275 |
| suricata | 1500 | 10 | worst | – | – | -4.87 | -7.2% | 0.402 | 0.375 |
| fraud | 10 | 10 | SIG_attacker | 254.1 | 253.1 | -0.98 | -0.4% | 0.060 | 0.086 |
| fraud | 10 | 10 | ZS_BLIND_attacker | 255.2 | 254.1 | -1.13 | -0.4% | 0.045 | 0.038 |
| fraud | 10 | 10 | fixed_uniform | 197.1 | 198.1 | +0.98 | +0.5% | 0.461 | 0.953 |
| fraud | 10 | 10 | worst | – | – | -1.09 | -0.4% | 0.053 | 0.051 |
| fraud | 20 | 10 | SIG_attacker | 225.5 | 220.1 | -5.39 | -2.4% | 0.008 | 0.014 |
| fraud | 20 | 10 | ZS_BLIND_attacker | 224.1 | 218.2 | -5.90 | -2.6% | 0.006 | 0.010 |
| fraud | 20 | 10 | fixed_uniform | 180.8 | 174.3 | -6.46 | -3.6% | 0.068 | 0.084 |
| fraud | 20 | 10 | worst | – | – | -5.43 | -2.4% | 0.007 | 0.010 |
| fraud | 30 | 10 | SIG_attacker | 188.0 | 184.8 | -3.16 | -1.7% | 0.040 | 0.064 |
| fraud | 30 | 10 | ZS_BLIND_attacker | 187.8 | 185.2 | -2.54 | -1.4% | 0.061 | 0.084 |
| fraud | 30 | 10 | fixed_uniform | 156.0 | 156.8 | +0.77 | +0.5% | 0.647 | 0.492 |
| fraud | 30 | 10 | worst | – | – | -3.01 | -1.6% | 0.042 | 0.064 |
| snort | 500 | 10 | SIG_attacker | 8.2 | 8.2 | +0.00 | +0.0% | nan | nan |
| snort | 500 | 10 | ZS_BLIND_attacker | 8.2 | 8.2 | +0.00 | +0.0% | nan | nan |
| snort | 500 | 10 | fixed_uniform | 32.3 | 32.3 | +0.00 | +0.0% | nan | nan |
| snort | 500 | 10 | worst | – | – | +0.00 | +0.0% | nan | nan |
| snort | 1000 | 10 | SIG_attacker | 5.3 | 5.3 | +0.00 | +0.0% | nan | nan |
| snort | 1000 | 10 | ZS_BLIND_attacker | 5.3 | 5.3 | +0.00 | +0.0% | nan | nan |
| snort | 1000 | 10 | fixed_uniform | 28.9 | 28.9 | +0.00 | +0.0% | nan | nan |
| snort | 1000 | 10 | worst | – | – | +0.00 | +0.0% | nan | nan |
| snort | 1500 | 10 | SIG_attacker | 3.4 | 3.4 | +0.00 | +0.0% | nan | nan |
| snort | 1500 | 10 | ZS_BLIND_attacker | 3.4 | 3.4 | +0.00 | +0.0% | nan | nan |
| snort | 1500 | 10 | fixed_uniform | 26.6 | 26.6 | +0.00 | +0.0% | nan | nan |
| snort | 1500 | 10 | worst | – | – | +0.00 | +0.0% | nan | nan |

### 4.3 Equilibrium values (expected defender loss at the final restricted equilibrium)

| dataset | B | game | n | eq. defender loss | std | mean DO iterations |
|---|---|---|---|---|---|---|
| fraud | 10 | ZS_BLIND | 10 | 255.0 | 1.6 | 3.9 |
| fraud | 10 | SIG | 10 | 253.8 | 1.6 | 4.2 |
| fraud | 20 | ZS_BLIND | 10 | 223.3 | 6.3 | 3.5 |
| fraud | 20 | SIG | 10 | 220.9 | 2.8 | 3.5 |
| fraud | 30 | ZS_BLIND | 10 | 186.9 | 2.3 | 3.5 |
| fraud | 30 | SIG | 10 | 183.7 | 4.3 | 4.5 |
| suricata | 500 | ZS_BLIND | 10 | 37.4 | 1.7 | 4.8 |
| suricata | 500 | SIG | 10 | 36.9 | 0.2 | 4.9 |
| suricata | 1000 | ZS_BLIND | 10 | 34.1 | 0.2 | 3.8 |
| suricata | 1000 | SIG | 10 | 34.1 | 0.4 | 4.8 |
| suricata | 1500 | ZS_BLIND | 10 | 33.1 | 0.8 | 5.4 |
| suricata | 1500 | SIG | 10 | 30.7 | 9.7 | 4.2 |
| snort | 500 | ZS_BLIND | 10 | 8.1 | 0.0 | 3.2 |
| snort | 500 | GS_BLIND | 10 | 8.1 | 0.0 | 3.0 |
| snort | 500 | SIG | 10 | 8.1 | 0.0 | 3.2 |
| snort | 1000 | ZS_BLIND | 10 | 4.8 | 0.0 | 3.2 |
| snort | 1000 | GS_BLIND | 10 | 4.8 | 0.0 | 3.2 |
| snort | 1000 | SIG | 10 | 4.8 | 0.0 | 3.2 |
| snort | 1500 | ZS_BLIND | 10 | 3.1 | 0.0 | 3.3 |
| snort | 1500 | GS_BLIND | 10 | 3.1 | 0.0 | 3.0 |
| snort | 1500 | SIG | 10 | 3.1 | 0.0 | 3.0 |

Equilibrium values of different games are not directly comparable (different attacker objectives); 4.2 is the fair comparison. For suricata and fraud the zero-sum and general-sum payoffs coincide in the original data (only snort sets separate gains), so GS_BLIND is run only on snort.

### 4.4 Sensitivity: how distinguishable the types are vs the value of the belief (fraud, B = 20, fixed attackers)

separability 0 = both types identical, 1 = the default types.

| separability | comparison | n | mean loss reduction | std | paired t p |
|---|---|---|---|---|---|
| 0 | BLIND - BELIEF | 5 | -0.5 | 8.1 | 0.897 |
| 0.25 | BLIND - BELIEF | 5 | 2.6 | 9.3 | 0.561 |
| 0.5 | BLIND - BELIEF | 5 | 0.1 | 7.6 | 0.983 |
| 0.75 | BLIND - BELIEF | 5 | 0.1 | 5.5 | 0.962 |
| 1 | BLIND - BELIEF | 5 | 5.3 | 4.7 | 0.066 |
| 0 | BLIND - INFORMED | 5 | -1.8 | 6.4 | 0.558 |
| 0.25 | BLIND - INFORMED | 5 | -0.0 | 5.4 | 0.988 |
| 0.5 | BLIND - INFORMED | 5 | 0.7 | 8.6 | 0.869 |
| 0.75 | BLIND - INFORMED | 5 | 9.8 | 6.0 | 0.022 |
| 1 | BLIND - INFORMED | 5 | 25.0 | 3.4 | <0.001 |

### Figures

![fixed_loss_vs_budget_suricata](results/full_v2/fixed_loss_vs_budget_suricata.png)
![fixed_loss_vs_budget_fraud](results/full_v2/fixed_loss_vs_budget_fraud.png)
![do_loss_vs_budget_suricata](results/full_v2/do_loss_vs_budget_suricata.png)
![do_loss_vs_budget_fraud](results/full_v2/do_loss_vs_budget_fraud.png)
![belief_trajectories](results/full_v2/belief_trajectories.png)
![do_convergence](results/full_v2/do_convergence.png)
![sensitivity_separability](results/full_v2/sensitivity_separability.png)

### 4.5 What the numbers say (final, 10 seeds per row)

1. **Against fixed type-based attackers the Bayes belief clearly helps on suricata.** BELIEF reduces the
   loss of BLIND by 8.2-10.2 (12-20%) at every budget (paired t p < 1e-5), and is within 1.1-1.5 of the
   cheating INFORMED defender (table 4.1). On fraud the gain is smaller: significant at B = 20 and 30
   (5.8 and 7.5 lower, p about 0.004-0.01) but not at B = 10. INFORMED is far better than BELIEF on fraud,
   because the fraud alerts reveal the type only slowly (mean belief on the true type 0.51 / 0.56 / 0.67
   after steps 1 / 5 / 20, versus 0.79 / 0.99 / 1.00 on suricata).
2. **At equilibrium, against an adaptive learned attacker, the advantage largely disappears.**
   * **Fraud:** the signaling defender has a lower loss than the zero-sum (= original general-sum) defender
     at every budget, against the learned attackers and in the worst case, by 0.4-2.6%. Uncorrected p-values:
     B = 20 p about 0.006-0.014, B = 30 p about 0.04-0.08, B = 10 p about 0.04-0.09. Against the fixed
     attacker it is not better at B = 10 and 30 (+0.5%).
   * **Suricata:** tied. Against the learned attackers the difference ranges from -5.8% to +9.7% with no
     consistent sign, and against the fixed attacker the signaling defender is 2-8% better; nothing is
     significant (p >= 0.06).
   * None of the equilibrium differences survives a Holm correction over all comparisons.
     **Overall this is a small, consistent but weak advantage for the signaling game on fraud and a tie
     on suricata, reported as such.**
3. **Snort does not discriminate.** The zero-sum, general-sum and signaling games give exactly the same
   loss at every budget, and in the fixed-attacker study all defenders are within noise of the uniform
   baseline. Alert type 2 has no false alerts and the existing budget-feasibility rule sends the whole
   budget to the alert types that have alerts, so the simple heuristics are already optimal (see
   `SIGNALING_NOTES.md`, decision 29).
4. **Sensitivity (4.4):** the more distinguishable the types, the more INFORMED gains (25.0 at
   separability 1, p < 1e-4); BELIEF gains little on fraud at any separability (at most 5.3, p = 0.07),
   consistent with point 1.
5. **Against rule-based baselines:** on suricata the signaling defender beats every rule baseline by
   13.5-39% against the learned attackers and by 2.7-15.7% against the fixed attacker (the worst case for
   every defender there). On fraud it beats them by up to about 12.5%, except that the fraud-specific rule
   ties with it at B = 30 (difference 0.2-0.7%, not significant). See `results/full_v2/cross_evaluation_tests.csv`.
6. **Belief consistency check:** on suricata the defender's belief equals exact Bayes on the attacker's
   realised behaviour (mean absolute difference 0.000); on fraud the difference is 0.02-0.07, because the
   defender's conjecture uses each type's average attack rate (`results/full_v2/belief_diagnostics.csv`).

**Statistics note.** With 10 seeds the smallest possible two-sided Wilcoxon p-value is 0.002, so after a
Holm correction over the whole family of comparisons even the strongest effects (paired t p < 1e-5) only
reach about 0.053. Both corrected and uncorrected values are in the CSVs.

**Limitations.** The double oracle with RL best responses approximates a perfect Bayesian equilibrium; it
does not prove one (section 1). Oracles are DDPG: the existing SAC implementation collapsed to a uniform
split in this setting (`SIGNALING_NOTES.md`). Training lengths are reduced (200 episodes per oracle,
up to 8 DO iterations) to fit the compute budget, identically for all conditions.
