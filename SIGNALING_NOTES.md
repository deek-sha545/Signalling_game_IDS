# SIGNALING_NOTES.md: files changed and decisions made

This file records every file added or changed for the signaling-game extension, and every
design decision, with the reason. Decisions were made *before* looking at FULL results and
apply identically to all conditions unless stated otherwise.

## Files changed (existing code)

| File | Change | Why |
|---|---|---|
| `src/config.py` | Reads the file named by the `IDS_CONFIG` environment variable; falls back to `project.conf`. | Lets toy/full configs live in separate files without overwriting `project.conf`. Original behaviour unchanged when the variable is unset. |
| `src/ddpg.py`, `src/sac.py`, `src/td3_v3_1.py` | `global_state = initial_state() if callable(initial_state) else initial_state` (3 places each, commented). | Lets Nature draw a fresh hidden attacker type at the start of every training/evaluation episode. The original code passes a `Model.State`, which is not callable, so its behaviour is unchanged (re-verified with the toy double-oracle run). |
| `.gitignore` | Ignores `logs/`, `runs/`, `papers/`, scratch files and the smoke-test checkpoint folders. | Keeps raw outputs and the (copyrighted) SAC-AP PDF out of git. |

No other existing file was modified. `project.conf` is untouched; a backup is in `src/project.conf.bak`.
`model.py`, `test.py` and `double_oracle.py` are unchanged; the signaling code imports
`Model`, the dataset instances and baselines from `test.py`, and `find_mixed_NE` from `double_oracle.py`.

## Files added

| File | Purpose |
|---|---|
| `src/signaling.py` | Attacker types, `SignalingGame`, exact Bayes `BeliefFilter`, observation functions, belief bookkeeping, policy wrappers, simulation (`play`). |
| `src/signaling_do.py` | RL oracles for belief/blind/informed defenders and type-conditioned attackers (reusing `DDPGlearning` of ddpg/sac/td3), signaling double oracle, experiment jobs, belief diagnostics, type check, sensitivity study. |
| `src/signaling_analysis.py` | Tables (mean, std, 95% CI), paired Wilcoxon + t-tests with Holm correction, all figures, `RESULTS.md`. |
| `src/test_signaling_belief.py` | Unit tests of the Bayes update (likelihood vs Monte-Carlo of `model.py`, Bayes rule, identical types, off-path, numerical stability with 10^7 counts, type definitions). |
| `src/signaling_toy.conf`, `src/signaling_full.conf` | TOY (minutes) and FULL configs. All type parameters are in their `[signaling]` section. |
| `run_signaling.sh` | One command to reproduce everything: `./run_signaling.sh toy` or `./run_signaling.sh full`. |
| `README_SIGNALING.md` | Plain-English explanation, reproduction commands, results. |
| `results/full/` | Final CSV tables, PNG figures, `RESULTS.md` (force-added to git). |

## Decisions

### Environment
1. **New venv `venv/` in the repo**, Python 3.7.17 from pyenv, exactly the pinned versions (TF 1.13.1, protobuf 3.20.3, numpy 1.21.6, scipy 1.7.3, nashpy 0.0.17). **matplotlib 3.5.3** was added for the figures, installed with a constraints file so it could not change any pinned package. No library crashes occurred, so no compatibility fixes were needed.
2. **Smoke test**: `python -u double_oracle.py snort 1000 125 1` at toy settings ran for ddpg, sac and td3 before and after the edits.

### Game model
3. **Types are separate `Model` objects** sharing alert types, budgets, loss, cost and gain; only `AttackType.pr_alert` differs. That reuses `Model.next_state` unchanged, so payoffs are computed exactly as before.
4. **Type definitions** (config `[signaling]`, applied to each attack action's base signature from `test.py`):
   * *noisy*: alert mass x2 (`noisy_scale = 2.0`), half of it (`noisy_spread = 0.5`) spread uniformly across all alert types (flooding/distraction).
   * *stealthy*: alert mass x0.5 (`stealthy_scale = 0.5`), all of it placed on the alert type with the highest false-alert rate (hides in noise).
   * For probability-style datasets (fraud, values <= 1) the same idea is applied to probabilities, capped at 0.95. For count-style datasets (snort, suricata) counts are rounded to whole alerts.
   * The values 2.0 / 0.5 / 0.5 were chosen once, a priori, as "clearly different but same order of magnitude". **They were not tuned on results.**
   * Prior 50/50; the code supports 2 or 3 types (`types`, `prior`, `<name>_kind`, `<name>_scale`).
5. **Horizon = 1** in all three datasets, so the signal at each step is the new alert-count vector `N[0]`. The belief filter asserts this.
6. **Zero-sum vs general-sum.** "Zero-sum" means attacker gain := defender loss (the existing default of `AttackType`; the attacker still pays its attack cost, exactly as the existing code does). "Dataset payoffs" uses the gains in `test.py`. **Only snort defines separate gains**, so on suricata and fraud the general-sum game *is* the zero-sum game. There, GS_BLIND is identical to ZS_BLIND and is not run twice, and SIG vs ZS_BLIND differs only by the hidden types and the belief.

### Belief
7. **Exact Bayes over attacker types** with the likelihood built from the trigger probabilities and Poisson false-alert rates of `model.py` (enumerating all attack subsets; verified against Monte-Carlo simulation of `model.py` in the unit tests). Computed in log space with `logsumexp`.
8. **The defender's conjecture of type-conditioned attack rates (`alpha_hat`)**. Exact Bayes needs to know how often each type attacks. The learned attacker's action depends on state it can see but the defender cannot (M, R), so an exact likelihood is intractable. We use the **stationary mean attack probability of each type**. For fixed attackers it is exact (they are constant). In the double oracle it is the mean attack rate of the *current equilibrium attacker mixture* (measured during payoff evaluation), frozen into each new belief defender. This is the standard "beliefs consistent with the equilibrium strategy" idea, but approximate. `belief_diagnostics` measures the gap against exact Bayes with the attack rates actually realised.
9. **Trembling hand**: conjectured attack rates are clipped to [0.001, 0.999]. Without it, a conjecture of exactly 1.0 (which the uniform attacker produces on snort) made ordinary signals "impossible" (0.6% of steps in the toy run). Applied to all belief filters.
10. **Off-path signals** (zero likelihood under every type) keep the previous belief and are counted. **Belief floor** 1e-9 avoids a belief locking at exactly 0.

### Learning
11. **Observation normalisation for ALL conditions in the suite**: alert counts are given to the networks as z-scores w.r.t. the false-alert distribution, clipped to [-10, 10]. Raw snort counts (~10^7) saturate the tanh layer and would make every network output a constant, which would make any belief/type input useless *by artefact*. The same normalisation is used for ZS_BLIND, GS_BLIND, SIG, BLIND, INFORMED and BELIEF, so it cannot create a gap between them. Consequently our ZS_BLIND is the original *approach* re-run in the same pipeline, not byte-identical to the original code. The original `double_oracle.py` path is untouched and still runnable.
12. **Attacker observation** = z-scored N + M + sign(R) + one-hot type.
13. **Oracle for FULL = DDPG** (`oracle_algo = ddpg`), for all conditions. DDPG and TD3 run through the same code paths (all three verified in TOY).
    *History, recorded for honesty:* the first FULL launch used SAC, to match the SAC-AP paper. The sensitivity stage showed that **every SAC-trained defender had exactly the uniform defender's loss, with zero spread across seeds**. Diagnosis (fraud, B = 20, full settings, one training run each): the SAC actor in the existing `sac.py` outputs the clip floor (about 1e-6) for every input, because its actor loss contains `+0.5*log(a)`, whose gradient always pushes outputs to the floor. Equal outputs mean a uniform budget split. DDPG and TD3 trained the same way did learn (loss 177.7 and 173.7 vs uniform 191.9). The SAC run was stopped, its outputs (`runs/full/`) are not used, and the suite was restarted with DDPG. `sac.py` was not modified (fixing it would change the existing algorithm). **Anyone using results produced with this `sac.py` should check for the same collapse.**
14. **Hyperparameters**: the SAC-AP / `project.conf` values (lr 0.001/0.002, gamma 0.95, tau 0.01, epsilon 1.0 decaying 0.99, hidden 32/64). Scaled down for runtime, equally for all conditions: 200 training episodes x 100 steps (original 500 x 400; with gamma = 0.95, steps beyond 100 carry <0.6% of the discounted weight), replay memory 20000 (holds every transition of a 20k-step training run), memory_init 2000, 20 oracle test episodes, `test_episodes_ns = 0` (the existing "non-strategic" printout is not used).
15. **Double oracle**: `max_iteration = 8`, `n_trial = 1` (original 100 and 2) for runtime; the same for all three games. Stopping rule unchanged (stop when neither new best response improves on the restricted equilibrium). Equilibrium selection `defender_max` (the existing default; `welfare_max` available via config). Initial pools as in `double_oracle.py`: `test_defense_newest` and the uniform attacker `test_attack_action` (for every type).
16. **Payoff matrix entries**: 40 episodes each, with a fixed evaluation seed (common random numbers). **Final evaluation**: 100 episodes, separate seed, identical for all defenders. Defender loss = expected discounted (gamma = 0.95) loss over 100 steps.
17. **One TF thread per worker**, by wrapping `tf.Session` in `signaling_do.py` (no edits to the oracle files). 8 parallel workers (12 cores, ~6.7 GB free RAM; each network uses ~17 MB). Replay buffers are freed after training and sessions of policies outside the final equilibrium support are closed.
18. **Checkpoints** are not written for the signaling runs (policies stay in memory within a job). Results are fully re-computable from the seed and config.

### Experiments
19. **Datasets/budgets** follow SAC-AP where possible: fraud B in {10, 20, 30} with attacker budget 2; suricata B in {500, 1000, 1500} with attacker budget 120; snort B in {500, 1000, 1500} with attacker budget 125 (repo default). **10 seeds** per setting, run seed-major so complete seeds finish first.
20. **Fixed-attacker study** (conditions a, b, c): each type plays the existing uniform attacker `test_attack_action` (so types differ only in their signatures). BLIND / INFORMED / BELIEF are trained with the same seed and settings. Baselines evaluated where `test.py` supports them: uniform, newest, proportion, snort rule (snort), suricata rule (suricata), fraud rule, aics, icde (fraud; budgets 10/20/30 are supported).
21. **Main ("3 full runs", as agreed with the user)**: double oracle for ZS_BLIND, GS_BLIND (snort only, see 6) and SIG. INFORMED is *not* run through the double oracle (only in the fixed-attacker study), to stay inside the one-day budget.
22. **Headline comparison = cross-evaluation**: every final defender mixture against every final attacker mixture (plus the fixed attacker), same episodes. Comparing equilibrium values across games is not like-for-like, because the attacker's objective differs (zero-sum attackers maximise defender loss). Both are reported.
23. **Statistics**: seed = unit of replication; mean, std, 95% t-CI; two-sided Wilcoxon signed-rank and paired t-tests over seeds; Holm correction over each table.
24. **Sensitivity study**: fraud, B = 20, separability in {0, 0.25, 0.5, 0.75, 1} (linear interpolation between the base signature and the full type definition), 5 seeds, fixed attackers, BLIND/INFORMED/BELIEF.
25. **Type check**: best static budget split per type (candidate set: one alert type only, uniform, proportional to false alerts, plus a 0.1 grid when there are 3 or fewer alert types) against the fixed attacker, and the loss when using the other type's best split.
26. **Comparison with the SAC-AP paper**: its numbers are only in figures, without seeds or confidence intervals, and come from the single-attacker environment. They are therefore *not* used as a head-to-head comparison; zero-sum is re-run in the same pipeline instead (ZS_BLIND).
