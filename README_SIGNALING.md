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
* Raw per-job outputs: `runs/full/` (JSON, logs, belief trajectories).
  Tables and figures: `results/full/` (`RESULTS.md` has every table).

---

## 4. Results

RESULTS_PLACEHOLDER
