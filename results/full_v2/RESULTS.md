# Signaling-game results (full_v2 mode)

Completed jobs: 74 (dataset x budget x seed). Oracle: ddpg. Defender loss = expected discounted loss per episode, lower is better. n = number of independent seeds.

## A. Defenders against FIXED type-based attackers (conditions a, b, c + baselines)

| dataset | budget | defender | n | mean loss | std | CI low | CI high |
|---|---|---|---|---|---|---|---|
| fraud | 10.000 | BLIND | 9 | 199.012 | 6.116 | 194.311 | 203.714 |
| fraud | 10.000 | INFORMED | 9 | 190.768 | 4.711 | 187.147 | 194.389 |
| fraud | 10.000 | BELIEF | 9 | 197.846 | 1.957 | 196.341 | 199.350 |
| fraud | 10.000 | baseline_uniform | 9 | 229.750 | 0.000 | 229.750 | 229.750 |
| fraud | 10.000 | baseline_newest | 9 | 229.750 | 0.000 | 229.750 | 229.750 |
| fraud | 10.000 | baseline_proportion | 9 | 241.640 | 0.000 | 241.640 | 241.640 |
| fraud | 10.000 | baseline_fraud_rule | 9 | 234.159 | 0.000 | 234.159 | 234.159 |
| fraud | 10.000 | baseline_aics | 9 | 246.618 | 0.000 | 246.618 | 246.618 |
| fraud | 10.000 | baseline_icde | 9 | 246.618 | 0.000 | 246.618 | 246.618 |
| fraud | 20.000 | BLIND | 9 | 179.266 | 2.366 | 177.447 | 181.084 |
| fraud | 20.000 | INFORMED | 9 | 154.902 | 2.444 | 153.023 | 156.781 |
| fraud | 20.000 | BELIEF | 9 | 173.233 | 5.570 | 168.952 | 177.514 |
| fraud | 20.000 | baseline_uniform | 9 | 196.967 | 0.000 | 196.967 | 196.967 |
| fraud | 20.000 | baseline_newest | 9 | 196.967 | 0.000 | 196.967 | 196.967 |
| fraud | 20.000 | baseline_proportion | 9 | 211.342 | 0.000 | 211.342 | 211.342 |
| fraud | 20.000 | baseline_fraud_rule | 9 | 194.526 | 0.000 | 194.526 | 194.526 |
| fraud | 20.000 | baseline_aics | 9 | 215.838 | 0.000 | 215.838 | 215.838 |
| fraud | 20.000 | baseline_icde | 9 | 216.548 | 0.000 | 216.548 | 216.548 |
| fraud | 30.000 | BLIND | 8 | 158.212 | 8.509 | 151.099 | 165.326 |
| fraud | 30.000 | INFORMED | 8 | 134.481 | 2.438 | 132.443 | 136.520 |
| fraud | 30.000 | BELIEF | 8 | 149.686 | 2.445 | 147.642 | 151.730 |
| fraud | 30.000 | baseline_uniform | 8 | 165.351 | 0.000 | 165.351 | 165.351 |
| fraud | 30.000 | baseline_newest | 8 | 165.351 | 0.000 | 165.351 | 165.351 |
| fraud | 30.000 | baseline_proportion | 8 | 184.536 | 0.000 | 184.536 | 184.536 |
| fraud | 30.000 | baseline_fraud_rule | 8 | 157.033 | 0.000 | 157.033 | 157.033 |
| fraud | 30.000 | baseline_aics | 8 | 172.658 | 0.000 | 172.658 | 172.658 |
| fraud | 30.000 | baseline_icde | 8 | 193.422 | 0.000 | 193.422 | 193.422 |
| suricata | 500.000 | BLIND | 8 | 70.443 | 1.766 | 68.967 | 71.920 |
| suricata | 500.000 | INFORMED | 8 | 61.278 | 0.989 | 60.451 | 62.105 |
| suricata | 500.000 | BELIEF | 8 | 62.320 | 1.194 | 61.323 | 63.318 |
| suricata | 500.000 | baseline_uniform | 8 | 94.380 | 0.000 | 94.380 | 94.380 |
| suricata | 500.000 | baseline_newest | 8 | 94.380 | 0.000 | 94.380 | 94.380 |
| suricata | 500.000 | baseline_proportion | 8 | 96.349 | 0.000 | 96.349 | 96.349 |
| suricata | 500.000 | baseline_suricata_rule | 8 | 88.549 | 0.000 | 88.549 | 88.549 |
| suricata | 1000.000 | BLIND | 7 | 55.954 | 2.152 | 53.964 | 57.944 |
| suricata | 1000.000 | INFORMED | 7 | 44.461 | 1.287 | 43.271 | 45.651 |
| suricata | 1000.000 | BELIEF | 7 | 45.097 | 0.525 | 44.612 | 45.583 |
| suricata | 1000.000 | baseline_uniform | 7 | 79.490 | 0.000 | 79.490 | 79.490 |
| suricata | 1000.000 | baseline_newest | 7 | 79.490 | 0.000 | 79.490 | 79.490 |
| suricata | 1000.000 | baseline_proportion | 7 | 82.549 | 0.000 | 82.549 | 82.549 |
| suricata | 1000.000 | baseline_suricata_rule | 7 | 76.844 | 0.000 | 76.844 | 76.844 |
| suricata | 1500.000 | BLIND | 7 | 48.958 | 1.541 | 47.533 | 50.384 |
| suricata | 1500.000 | INFORMED | 7 | 37.584 | 1.585 | 36.118 | 39.049 |
| suricata | 1500.000 | BELIEF | 7 | 38.388 | 0.634 | 37.802 | 38.974 |
| suricata | 1500.000 | baseline_uniform | 7 | 69.908 | 0.000 | 69.908 | 69.908 |
| suricata | 1500.000 | baseline_newest | 7 | 69.908 | 0.000 | 69.908 | 69.908 |
| suricata | 1500.000 | baseline_proportion | 7 | 73.941 | 0.000 | 73.941 | 73.941 |
| suricata | 1500.000 | baseline_suricata_rule | 7 | 69.176 | 0.000 | 69.176 | 69.176 |
| snort | 500.000 | BLIND | 9 | 33.046 | 1.640 | 31.785 | 34.306 |
| snort | 500.000 | INFORMED | 9 | 32.367 | 0.039 | 32.336 | 32.397 |
| snort | 500.000 | BELIEF | 9 | 32.445 | 0.256 | 32.249 | 32.642 |
| snort | 500.000 | baseline_uniform | 9 | 32.349 | 0.000 | 32.349 | 32.349 |
| snort | 500.000 | baseline_newest | 9 | 32.349 | 0.000 | 32.349 | 32.349 |
| snort | 500.000 | baseline_proportion | 9 | 59.072 | 0.000 | 59.072 | 59.072 |
| snort | 500.000 | baseline_snort_rule | 9 | 38.004 | 0.000 | 38.004 | 38.004 |
| snort | 1000.000 | BLIND | 9 | 30.116 | 2.893 | 27.893 | 32.340 |
| snort | 1000.000 | INFORMED | 9 | 29.394 | 1.155 | 28.507 | 30.282 |
| snort | 1000.000 | BELIEF | 9 | 28.917 | 0.002 | 28.916 | 28.919 |
| snort | 1000.000 | baseline_uniform | 9 | 28.916 | 0.000 | 28.916 | 28.916 |
| snort | 1000.000 | baseline_newest | 9 | 28.916 | 0.000 | 28.916 | 28.916 |
| snort | 1000.000 | baseline_proportion | 9 | 51.322 | 0.000 | 51.322 | 51.322 |
| snort | 1000.000 | baseline_snort_rule | 9 | 38.004 | 0.000 | 38.004 | 38.004 |
| snort | 1500.000 | BLIND | 8 | 26.837 | 0.705 | 26.247 | 27.427 |
| snort | 1500.000 | INFORMED | 8 | 26.588 | 0.000 | 26.588 | 26.588 |
| snort | 1500.000 | BELIEF | 8 | 26.588 | 0.000 | 26.588 | 26.588 |
| snort | 1500.000 | baseline_uniform | 8 | 26.588 | 0.000 | 26.588 | 26.588 |
| snort | 1500.000 | baseline_newest | 8 | 26.588 | 0.000 | 26.588 | 26.588 |
| snort | 1500.000 | baseline_proportion | 8 | 45.903 | 0.000 | 45.903 | 45.903 |
| snort | 1500.000 | baseline_snort_rule | 8 | 38.004 | 0.000 | 38.004 | 38.004 |

Paired tests (negative mean difference = first defender has LOWER loss):

| dataset | budget | comparison | n | mean diff | Wilcoxon p | t-test p | Wilcoxon p (Holm) |
|---|---|---|---|---|---|---|---|
| fraud | 10.000 | BELIEF - BLIND | 9 | -1.167 | 0.612 | 0.637 | 1.000 |
| fraud | 10.000 | INFORMED - BLIND | 9 | -8.244 | 0.025 | 0.028 | 0.326 |
| fraud | 10.000 | BELIEF - INFORMED | 9 | 7.078 | 0.017 | 0.002 | 0.297 |
| fraud | 20.000 | BELIEF - BLIND | 9 | -6.033 | 0.020 | 0.007 | 0.297 |
| fraud | 20.000 | INFORMED - BLIND | 9 | -24.364 | 0.004 | 0.000 | 0.102 |
| fraud | 20.000 | BELIEF - INFORMED | 9 | 18.331 | 0.004 | 0.000 | 0.102 |
| fraud | 30.000 | BELIEF - BLIND | 8 | -8.526 | 0.008 | 0.008 | 0.188 |
| fraud | 30.000 | INFORMED - BLIND | 8 | -23.731 | 0.008 | 0.000 | 0.188 |
| fraud | 30.000 | BELIEF - INFORMED | 8 | 15.205 | 0.008 | 0.000 | 0.188 |
| suricata | 500.000 | BELIEF - BLIND | 8 | -8.123 | 0.008 | 0.000 | 0.188 |
| suricata | 500.000 | INFORMED - BLIND | 8 | -9.165 | 0.008 | 0.000 | 0.188 |
| suricata | 500.000 | BELIEF - INFORMED | 8 | 1.042 | 0.148 | 0.080 | 1.000 |
| suricata | 1000.000 | BELIEF - BLIND | 7 | -10.857 | 0.016 | 0.000 | 0.297 |
| suricata | 1000.000 | INFORMED - BLIND | 7 | -11.493 | 0.016 | 0.000 | 0.297 |
| suricata | 1000.000 | BELIEF - INFORMED | 7 | 0.636 | 0.297 | 0.268 | 1.000 |
| suricata | 1500.000 | BELIEF - BLIND | 7 | -10.571 | 0.016 | 0.000 | 0.297 |
| suricata | 1500.000 | INFORMED - BLIND | 7 | -11.375 | 0.016 | 0.000 | 0.297 |
| suricata | 1500.000 | BELIEF - INFORMED | 7 | 0.804 | 0.375 | 0.296 | 1.000 |
| snort | 500.000 | BELIEF - BLIND | 9 | -0.600 | 0.652 | 0.322 | 1.000 |
| snort | 500.000 | INFORMED - BLIND | 9 | -0.679 | 0.055 | 0.249 | 0.656 |
| snort | 500.000 | BELIEF - INFORMED | 9 | 0.079 | 0.484 | 0.394 | 1.000 |
| snort | 1000.000 | BELIEF - BLIND | 9 | -1.199 | 0.063 | 0.249 | 0.693 |
| snort | 1000.000 | INFORMED - BLIND | 9 | -0.722 | 0.499 | 0.532 | 1.000 |
| snort | 1000.000 | BELIEF - INFORMED | 9 | -0.477 | 0.416 | 0.250 | 1.000 |
| snort | 1500.000 | BELIEF - BLIND | 8 | -0.249 | 0.317 | 0.351 | 1.000 |
| snort | 1500.000 | INFORMED - BLIND | 8 | -0.249 | 0.317 | 0.351 | 1.000 |
| snort | 1500.000 | BELIEF - INFORMED | 8 | 0.000 | nan | nan | nan |

## B. Equilibrium (double oracle) results: zero-sum vs general-sum vs signaling

For suricata and fraud test.py defines no separate attacker gain, so the general-sum game equals the zero-sum game and GS_BLIND is not run separately; there SIG differs from ZS_BLIND ONLY by the belief/types. Snort has distinct gains.

### B1. Defender loss at the restricted-game equilibrium (each game against its OWN attacker)

Caution: these are values of DIFFERENT games (the attacker objective differs between zero-sum and general-sum), so they are not a like-for-like comparison of defenders; see B2.

"weight newest" = average equilibrium probability on the initial non-learned `newest` defender; a value near 1 means the RL best responses never beat that heuristic in the restricted game.

| dataset | budget | game | n | mean loss | std | CI low | CI high | DO iterations | weight newest |
|---|---|---|---|---|---|---|---|---|---|
| fraud | 10.000 | ZS_BLIND | 9 | 254.592 | 0.715 | 254.043 | 255.141 | 3.889 | 0.000 |
| fraud | 10.000 | SIG | 9 | 253.501 | 1.444 | 252.391 | 254.611 | 4.333 | 0.000 |
| fraud | 20.000 | ZS_BLIND | 9 | 222.324 | 5.750 | 217.904 | 226.744 | 3.667 | 0.000 |
| fraud | 20.000 | SIG | 9 | 220.633 | 2.787 | 218.491 | 222.775 | 3.667 | 0.000 |
| fraud | 30.000 | ZS_BLIND | 8 | 187.512 | 1.920 | 185.907 | 189.117 | 3.750 | 0.000 |
| fraud | 30.000 | SIG | 8 | 184.301 | 4.615 | 180.442 | 188.159 | 4.375 | 0.033 |
| suricata | 500.000 | ZS_BLIND | 8 | 37.533 | 1.880 | 35.961 | 39.104 | 4.750 | 0.000 |
| suricata | 500.000 | SIG | 8 | 36.956 | 0.211 | 36.780 | 37.133 | 4.750 | 0.000 |
| suricata | 1000.000 | ZS_BLIND | 7 | 34.141 | 0.195 | 33.961 | 34.321 | 4.000 | 0.000 |
| suricata | 1000.000 | SIG | 7 | 34.098 | 0.316 | 33.806 | 34.390 | 4.714 | 0.000 |
| suricata | 1500.000 | ZS_BLIND | 7 | 32.956 | 0.903 | 32.121 | 33.792 | 5.571 | 0.000 |
| suricata | 1500.000 | SIG | 7 | 33.718 | 1.324 | 32.493 | 34.943 | 4.286 | 0.000 |
| snort | 500.000 | ZS_BLIND | 9 | 8.143 | 0.000 | 8.143 | 8.143 | 3.111 | 1.000 |
| snort | 500.000 | GS_BLIND | 9 | 8.143 | 0.000 | 8.143 | 8.143 | 3.111 | 1.000 |
| snort | 500.000 | SIG | 9 | 8.143 | 0.000 | 8.143 | 8.143 | 3.111 | 1.000 |
| snort | 1000.000 | ZS_BLIND | 9 | 4.796 | 0.000 | 4.796 | 4.796 | 3.111 | 1.000 |
| snort | 1000.000 | GS_BLIND | 9 | 4.796 | 0.000 | 4.796 | 4.796 | 3.333 | 1.000 |
| snort | 1000.000 | SIG | 9 | 4.796 | 0.000 | 4.796 | 4.796 | 3.333 | 1.000 |
| snort | 1500.000 | ZS_BLIND | 8 | 3.111 | 0.000 | 3.111 | 3.111 | 3.125 | 1.000 |
| snort | 1500.000 | GS_BLIND | 8 | 3.111 | 0.000 | 3.111 | 3.111 | 3.000 | 1.000 |
| snort | 1500.000 | SIG | 8 | 3.111 | 0.000 | 3.111 | 3.111 | 3.000 | 1.000 |

### B2. Cross-evaluation: every final defender against the SAME attackers

Defender = final equilibrium defender mixture of each game (or a baseline). Attacker = final equilibrium attacker mixture of each game, or the fixed uniform attacker. Same evaluation episodes for all (common random numbers). "worst" = max over the attackers.

| dataset | budget | defender | ZS_BLIND_attacker | SIG_attacker | fixed_uniform | GS_BLIND_attacker | worst |
|---|---|---|---|---|---|---|---|
| fraud | 10.000 | ZS_BLIND | 255.051 | 253.964 | 197.139 |  | 255.203 |
| fraud | 10.000 | SIG | 254.143 | 253.143 | 198.487 |  | 254.342 |
| fraud | 10.000 | baseline_uniform | 271.287 | 269.969 | 229.750 |  | 271.312 |
| fraud | 10.000 | baseline_newest | 271.287 | 269.969 | 229.750 |  | 271.312 |
| fraud | 10.000 | baseline_proportion | 276.797 | 275.407 | 241.640 |  | 276.797 |
| fraud | 10.000 | baseline_fraud_rule | 270.837 | 269.355 | 234.159 |  | 270.837 |
| fraud | 10.000 | baseline_aics | 272.731 | 271.757 | 246.618 |  | 272.860 |
| fraud | 10.000 | baseline_icde | 272.731 | 271.757 | 246.618 |  | 272.860 |
| fraud | 10.000 | GS_BLIND |  |  |  |  |  |
| fraud | 10.000 | baseline_snort_rule |  |  |  |  |  |
| fraud | 10.000 | baseline_suricata_rule |  |  |  |  |  |
| fraud | 20.000 | ZS_BLIND | 222.802 | 224.311 | 178.960 |  | 225.196 |
| fraud | 20.000 | SIG | 217.934 | 220.008 | 174.703 |  | 220.849 |
| fraud | 20.000 | baseline_uniform | 236.352 | 236.796 | 196.967 |  | 237.616 |
| fraud | 20.000 | baseline_newest | 236.352 | 236.796 | 196.967 |  | 237.616 |
| fraud | 20.000 | baseline_proportion | 243.164 | 242.396 | 211.342 |  | 243.520 |
| fraud | 20.000 | baseline_fraud_rule | 227.765 | 227.415 | 194.526 |  | 228.296 |
| fraud | 20.000 | baseline_aics | 234.670 | 231.651 | 215.838 |  | 234.776 |
| fraud | 20.000 | baseline_icde | 238.166 | 235.863 | 216.548 |  | 238.330 |
| fraud | 20.000 | GS_BLIND |  |  |  |  |  |
| fraud | 20.000 | baseline_snort_rule |  |  |  |  |  |
| fraud | 20.000 | baseline_suricata_rule |  |  |  |  |  |
| fraud | 30.000 | ZS_BLIND | 188.374 | 187.233 | 156.394 |  | 189.208 |
| fraud | 30.000 | SIG | 186.891 | 185.255 | 157.159 |  | 187.418 |
| fraud | 30.000 | baseline_uniform | 204.534 | 202.939 | 165.351 |  | 205.615 |
| fraud | 30.000 | baseline_newest | 204.534 | 202.939 | 165.351 |  | 205.615 |
| fraud | 30.000 | baseline_proportion | 212.474 | 211.537 | 184.536 |  | 212.968 |
| fraud | 30.000 | baseline_fraud_rule | 186.993 | 185.627 | 157.033 |  | 187.581 |
| fraud | 30.000 | baseline_aics | 189.476 | 189.017 | 172.658 |  | 189.818 |
| fraud | 30.000 | baseline_icde | 206.488 | 206.716 | 193.422 |  | 207.099 |
| fraud | 30.000 | GS_BLIND |  |  |  |  |  |
| fraud | 30.000 | baseline_snort_rule |  |  |  |  |  |
| fraud | 30.000 | baseline_suricata_rule |  |  |  |  |  |
| suricata | 500.000 | ZS_BLIND | 38.598 | 40.623 | 87.198 |  | 87.198 |
| suricata | 500.000 | SIG | 40.982 | 38.292 | 85.509 |  | 85.509 |
| suricata | 500.000 | baseline_uniform | 56.440 | 55.811 | 94.380 |  | 94.380 |
| suricata | 500.000 | baseline_newest | 56.440 | 55.811 | 94.380 |  | 94.380 |
| suricata | 500.000 | baseline_proportion | 61.900 | 61.869 | 96.349 |  | 96.349 |
| suricata | 500.000 | baseline_fraud_rule |  |  |  |  |  |
| suricata | 500.000 | baseline_aics |  |  |  |  |  |
| suricata | 500.000 | baseline_icde |  |  |  |  |  |
| suricata | 500.000 | GS_BLIND |  |  |  |  |  |
| suricata | 500.000 | baseline_snort_rule |  |  |  |  |  |
| suricata | 500.000 | baseline_suricata_rule | 61.958 | 62.009 | 88.549 |  | 88.549 |
| suricata | 1000.000 | ZS_BLIND | 34.262 | 34.262 | 78.582 |  | 78.582 |
| suricata | 1000.000 | SIG | 34.390 | 34.390 | 74.955 |  | 74.955 |
| suricata | 1000.000 | baseline_uniform | 48.208 | 48.208 | 79.490 |  | 79.490 |
| suricata | 1000.000 | baseline_newest | 48.208 | 48.208 | 79.490 |  | 79.490 |
| suricata | 1000.000 | baseline_proportion | 56.391 | 56.391 | 82.549 |  | 82.549 |
| suricata | 1000.000 | baseline_fraud_rule |  |  |  |  |  |
| suricata | 1000.000 | baseline_aics |  |  |  |  |  |
| suricata | 1000.000 | baseline_icde |  |  |  |  |  |
| suricata | 1000.000 | GS_BLIND |  |  |  |  |  |
| suricata | 1000.000 | baseline_snort_rule |  |  |  |  |  |
| suricata | 1000.000 | baseline_suricata_rule | 56.650 | 56.650 | 76.844 |  | 76.844 |
| suricata | 1500.000 | ZS_BLIND | 33.185 | 33.185 | 68.369 |  | 68.369 |
| suricata | 1500.000 | SIG | 34.044 | 34.044 | 63.342 |  | 63.342 |
| suricata | 1500.000 | baseline_uniform | 42.246 | 42.246 | 69.908 |  | 69.908 |
| suricata | 1500.000 | baseline_newest | 42.246 | 42.246 | 69.908 |  | 69.908 |
| suricata | 1500.000 | baseline_proportion | 51.471 | 51.471 | 73.941 |  | 73.941 |
| suricata | 1500.000 | baseline_fraud_rule |  |  |  |  |  |
| suricata | 1500.000 | baseline_aics |  |  |  |  |  |
| suricata | 1500.000 | baseline_icde |  |  |  |  |  |
| suricata | 1500.000 | GS_BLIND |  |  |  |  |  |
| suricata | 1500.000 | baseline_snort_rule |  |  |  |  |  |
| suricata | 1500.000 | baseline_suricata_rule | 51.510 | 51.510 | 69.176 |  | 69.176 |
| snort | 500.000 | ZS_BLIND | 8.224 | 8.224 | 32.349 | 8.224 | 32.349 |
| snort | 500.000 | SIG | 8.224 | 8.224 | 32.349 | 8.224 | 32.349 |
| snort | 500.000 | baseline_uniform | 8.224 | 8.224 | 32.349 | 8.224 | 32.349 |
| snort | 500.000 | baseline_newest | 8.224 | 8.224 | 32.349 | 8.224 | 32.349 |
| snort | 500.000 | baseline_proportion | 11.784 | 11.784 | 59.072 | 11.784 | 59.072 |
| snort | 500.000 | baseline_fraud_rule |  |  |  |  |  |
| snort | 500.000 | baseline_aics |  |  |  |  |  |
| snort | 500.000 | baseline_icde |  |  |  |  |  |
| snort | 500.000 | GS_BLIND | 8.224 | 8.224 | 32.349 | 8.224 | 32.349 |
| snort | 500.000 | baseline_snort_rule | 13.217 | 13.217 | 38.004 | 13.217 | 38.004 |
| snort | 500.000 | baseline_suricata_rule |  |  |  |  |  |
| snort | 1000.000 | ZS_BLIND | 5.261 | 5.261 | 28.916 | 5.261 | 28.916 |
| snort | 1000.000 | SIG | 5.261 | 5.261 | 28.916 | 5.261 | 28.916 |
| snort | 1000.000 | baseline_uniform | 5.261 | 5.261 | 28.916 | 5.261 | 28.916 |
| snort | 1000.000 | baseline_newest | 5.261 | 5.261 | 28.916 | 5.261 | 28.916 |
| snort | 1000.000 | baseline_proportion | 6.175 | 6.175 | 51.322 | 6.175 | 51.322 |
| snort | 1000.000 | baseline_fraud_rule |  |  |  |  |  |
| snort | 1000.000 | baseline_aics |  |  |  |  |  |
| snort | 1000.000 | baseline_icde |  |  |  |  |  |
| snort | 1000.000 | GS_BLIND | 5.261 | 5.261 | 28.916 | 5.261 | 28.916 |
| snort | 1000.000 | baseline_snort_rule | 13.217 | 13.217 | 38.004 | 13.217 | 38.004 |
| snort | 1000.000 | baseline_suricata_rule |  |  |  |  |  |
| snort | 1500.000 | ZS_BLIND | 3.420 | 3.420 | 26.588 | 3.420 | 26.588 |
| snort | 1500.000 | SIG | 3.420 | 3.420 | 26.588 | 3.420 | 26.588 |
| snort | 1500.000 | baseline_uniform | 3.420 | 3.420 | 26.588 | 3.420 | 26.588 |
| snort | 1500.000 | baseline_newest | 3.420 | 3.420 | 26.588 | 3.420 | 26.588 |
| snort | 1500.000 | baseline_proportion | 3.420 | 3.420 | 45.903 | 3.420 | 45.903 |
| snort | 1500.000 | baseline_fraud_rule |  |  |  |  |  |
| snort | 1500.000 | baseline_aics |  |  |  |  |  |
| snort | 1500.000 | baseline_icde |  |  |  |  |  |
| snort | 1500.000 | GS_BLIND | 3.420 | 3.420 | 26.588 | 3.420 | 26.588 |
| snort | 1500.000 | baseline_snort_rule | 13.217 | 13.217 | 38.004 | 13.217 | 38.004 |
| snort | 1500.000 | baseline_suricata_rule |  |  |  |  |  |

Paired tests SIG defender vs other defenders (negative = SIG has LOWER loss). Only comparisons against the learned defenders are shown here; all (incl. baselines) are in cross_evaluation_tests.csv.

| dataset | budget | comparison | attacker | n | mean diff | % diff | Wilcoxon p | t p | Wilcoxon p (Holm) |
|---|---|---|---|---|---|---|---|---|---|
| fraud | 10.000 | SIG - ZS_BLIND | ZS_BLIND_attacker | 9 | -0.908 | -0.356 | 0.069 | 0.097 | 1.000 |
| fraud | 10.000 | SIG - ZS_BLIND | SIG_attacker | 9 | -0.821 | -0.323 | 0.161 | 0.124 | 1.000 |
| fraud | 10.000 | SIG - ZS_BLIND | fixed_uniform | 9 | 1.348 | 0.684 | 0.674 | 0.351 | 1.000 |
| fraud | 10.000 | SIG - ZS_BLIND | worst | 9 | -0.860 | -0.337 | 0.093 | 0.113 | 1.000 |
| fraud | 20.000 | SIG - ZS_BLIND | ZS_BLIND_attacker | 9 | -4.868 | -2.185 | 0.020 | 0.010 | 1.000 |
| fraud | 20.000 | SIG - ZS_BLIND | SIG_attacker | 9 | -4.304 | -1.919 | 0.027 | 0.010 | 1.000 |
| fraud | 20.000 | SIG - ZS_BLIND | fixed_uniform | 9 | -4.256 | -2.378 | 0.164 | 0.123 | 1.000 |
| fraud | 20.000 | SIG - ZS_BLIND | worst | 9 | -4.347 | -1.930 | 0.020 | 0.009 | 1.000 |
| fraud | 30.000 | SIG - ZS_BLIND | ZS_BLIND_attacker | 8 | -1.483 | -0.787 | 0.312 | 0.259 | 1.000 |
| fraud | 30.000 | SIG - ZS_BLIND | SIG_attacker | 8 | -1.978 | -1.057 | 0.250 | 0.182 | 1.000 |
| fraud | 30.000 | SIG - ZS_BLIND | fixed_uniform | 8 | 0.766 | 0.490 | 0.844 | 0.722 | 1.000 |
| fraud | 30.000 | SIG - ZS_BLIND | worst | 8 | -1.790 | -0.946 | 0.250 | 0.189 | 1.000 |
| suricata | 500.000 | SIG - ZS_BLIND | ZS_BLIND_attacker | 8 | 2.385 | 6.178 | 0.547 | 0.301 | 1.000 |
| suricata | 500.000 | SIG - ZS_BLIND | SIG_attacker | 8 | -2.331 | -5.738 | 0.742 | 0.399 | 1.000 |
| suricata | 500.000 | SIG - ZS_BLIND | fixed_uniform | 8 | -1.689 | -1.938 | 0.461 | 0.521 | 1.000 |
| suricata | 500.000 | SIG - ZS_BLIND | worst | 8 | -1.689 | -1.938 | 0.461 | 0.521 | 1.000 |
| suricata | 1000.000 | SIG - ZS_BLIND | ZS_BLIND_attacker | 7 | 0.128 | 0.373 | 0.938 | 0.604 | 1.000 |
| suricata | 1000.000 | SIG - ZS_BLIND | SIG_attacker | 7 | 0.128 | 0.373 | 0.938 | 0.604 | 1.000 |
| suricata | 1000.000 | SIG - ZS_BLIND | fixed_uniform | 7 | -3.628 | -4.616 | 0.469 | 0.387 | 1.000 |
| suricata | 1000.000 | SIG - ZS_BLIND | worst | 7 | -3.628 | -4.616 | 0.469 | 0.387 | 1.000 |
| suricata | 1500.000 | SIG - ZS_BLIND | ZS_BLIND_attacker | 7 | 0.859 | 2.589 | 0.297 | 0.245 | 1.000 |
| suricata | 1500.000 | SIG - ZS_BLIND | SIG_attacker | 7 | 0.859 | 2.589 | 0.297 | 0.245 | 1.000 |
| suricata | 1500.000 | SIG - ZS_BLIND | fixed_uniform | 7 | -5.026 | -7.352 | 0.578 | 0.549 | 1.000 |
| suricata | 1500.000 | SIG - ZS_BLIND | worst | 7 | -5.026 | -7.352 | 0.578 | 0.549 | 1.000 |
| snort | 500.000 | SIG - ZS_BLIND | ZS_BLIND_attacker | 9 | 0.000 | 0.000 | nan | nan | nan |
| snort | 500.000 | SIG - ZS_BLIND | SIG_attacker | 9 | 0.000 | 0.000 | nan | nan | nan |
| snort | 500.000 | SIG - ZS_BLIND | fixed_uniform | 9 | 0.000 | 0.000 | nan | nan | nan |
| snort | 500.000 | SIG - ZS_BLIND | GS_BLIND_attacker | 9 | 0.000 | 0.000 | nan | nan | nan |
| snort | 500.000 | SIG - ZS_BLIND | worst | 9 | 0.000 | 0.000 | nan | nan | nan |
| snort | 500.000 | SIG - GS_BLIND | ZS_BLIND_attacker | 9 | 0.000 | 0.000 | nan | nan | nan |
| snort | 500.000 | SIG - GS_BLIND | SIG_attacker | 9 | 0.000 | 0.000 | nan | nan | nan |
| snort | 500.000 | SIG - GS_BLIND | fixed_uniform | 9 | 0.000 | 0.000 | nan | nan | nan |
| snort | 500.000 | SIG - GS_BLIND | GS_BLIND_attacker | 9 | 0.000 | 0.000 | nan | nan | nan |
| snort | 500.000 | SIG - GS_BLIND | worst | 9 | 0.000 | 0.000 | nan | nan | nan |
| snort | 1000.000 | SIG - ZS_BLIND | ZS_BLIND_attacker | 9 | 0.000 | 0.000 | nan | nan | nan |
| snort | 1000.000 | SIG - ZS_BLIND | SIG_attacker | 9 | 0.000 | 0.000 | nan | nan | nan |
| snort | 1000.000 | SIG - ZS_BLIND | fixed_uniform | 9 | 0.000 | 0.000 | nan | nan | nan |
| snort | 1000.000 | SIG - ZS_BLIND | GS_BLIND_attacker | 9 | 0.000 | 0.000 | nan | nan | nan |
| snort | 1000.000 | SIG - ZS_BLIND | worst | 9 | 0.000 | 0.000 | nan | nan | nan |
| snort | 1000.000 | SIG - GS_BLIND | ZS_BLIND_attacker | 9 | 0.000 | 0.000 | nan | nan | nan |
| snort | 1000.000 | SIG - GS_BLIND | SIG_attacker | 9 | 0.000 | 0.000 | nan | nan | nan |
| snort | 1000.000 | SIG - GS_BLIND | fixed_uniform | 9 | 0.000 | 0.000 | nan | nan | nan |
| snort | 1000.000 | SIG - GS_BLIND | GS_BLIND_attacker | 9 | 0.000 | 0.000 | nan | nan | nan |
| snort | 1000.000 | SIG - GS_BLIND | worst | 9 | 0.000 | 0.000 | nan | nan | nan |
| snort | 1500.000 | SIG - ZS_BLIND | ZS_BLIND_attacker | 8 | 0.000 | 0.000 | nan | nan | nan |
| snort | 1500.000 | SIG - ZS_BLIND | SIG_attacker | 8 | 0.000 | 0.000 | nan | nan | nan |
| snort | 1500.000 | SIG - ZS_BLIND | fixed_uniform | 8 | 0.000 | 0.000 | nan | nan | nan |
| snort | 1500.000 | SIG - ZS_BLIND | GS_BLIND_attacker | 8 | 0.000 | 0.000 | nan | nan | nan |
| snort | 1500.000 | SIG - ZS_BLIND | worst | 8 | 0.000 | 0.000 | nan | nan | nan |
| snort | 1500.000 | SIG - GS_BLIND | ZS_BLIND_attacker | 8 | 0.000 | 0.000 | nan | nan | nan |
| snort | 1500.000 | SIG - GS_BLIND | SIG_attacker | 8 | 0.000 | 0.000 | nan | nan | nan |
| snort | 1500.000 | SIG - GS_BLIND | fixed_uniform | 8 | 0.000 | 0.000 | nan | nan | nan |
| snort | 1500.000 | SIG - GS_BLIND | GS_BLIND_attacker | 8 | 0.000 | 0.000 | nan | nan | nan |
| snort | 1500.000 | SIG - GS_BLIND | worst | 8 | 0.000 | 0.000 | nan | nan | nan |

## C. Belief diagnostics (signaling game, final equilibrium)

| dataset | budget | n (belief policy in support) | n (no belief policy in support) | |b_def - b_exactBayes| | off-path rate (def. conjecture) | off-path rate (exact) | final belief on true type |
|---|---|---|---|---|---|---|---|
| fraud | 10.000 | 9 | 0 | 0.069 | 0.000 | 0.000 | 0.731 |
| fraud | 20.000 | 9 | 0 | 0.063 | 0.000 | 0.000 | 0.742 |
| fraud | 30.000 | 8 | 0 | 0.018 | 0.000 | 0.000 | 0.753 |
| suricata | 500.000 | 8 | 0 | 0.000 | 0.000 | 0.000 | 0.717 |
| suricata | 1000.000 | 7 | 0 | 0.000 | 0.000 | 0.000 | 0.717 |
| suricata | 1500.000 | 7 | 0 | 0.000 | 0.000 | 0.000 | 0.717 |
| snort | 500.000 | 0 | 9 |  |  |  |  |
| snort | 1000.000 | 0 | 9 |  |  |  |  |
| snort | 1500.000 | 0 | 8 |  |  |  |  |

### Investigation split of the main belief policy at different beliefs (seed 0, middle budget)

Shows how the learned defender reacts to its belief, including beliefs it rarely or never reaches on the equilibrium path (off-path behaviour).

| dataset | alert counts typical of | belief | budget share per alert type |
|---|---|---|---|
| fraud | noisy | prior | 0.45 / 0.41 / 0.14 |
| fraud | noisy | certain_noisy | 0.50 / 0.00 / 0.50 |
| fraud | noisy | certain_stealthy | 0.00 / 1.00 / 0.00 |
| fraud | stealthy | prior | 0.42 / 0.32 / 0.27 |
| fraud | stealthy | certain_noisy | 0.50 / 0.00 / 0.50 |
| fraud | stealthy | certain_stealthy | 0.00 / 1.00 / 0.00 |

| dataset | alert counts typical of | belief | budget share per alert type |
|---|---|---|---|
| suricata | noisy | prior | 0.00 / 0.18 / 0.38 / 0.00 / 0.45 / 0.00 / 0.00 |
| suricata | noisy | certain_noisy | 0.00 / 0.00 / 0.95 / 0.04 / 0.00 / 0.00 / 0.00 |
| suricata | noisy | certain_stealthy | 0.00 / 0.33 / 0.33 / 0.00 / 0.34 / 0.00 / 0.00 |
| suricata | stealthy | prior | 0.00 / 0.18 / 0.38 / 0.00 / 0.44 / 0.00 / 0.00 |
| suricata | stealthy | certain_noisy | 0.00 / 0.00 / 0.96 / 0.04 / 0.00 / 0.00 / 0.00 |
| suricata | stealthy | certain_stealthy | 0.00 / 0.33 / 0.33 / 0.00 / 0.34 / 0.00 / 0.00 |

## D. Do the types call for different investigation patterns?

Best static budget split per type against the fixed uniform attacker (seed-0 jobs), and the loss when the OTHER type's best split is used instead.

| dataset | budget | type | best split | loss | other type | loss with other type's split |
|---|---|---|---|---|---|---|
| fraud | 10.000 | noisy | one_hot_t0 | 118.464 | stealthy | 213.718 |
| fraud | 10.000 | stealthy | one_hot_t1 | 239.614 | noisy | 264.236 |
| fraud | 20.000 | noisy | grid_0.7_0.1_0.2 | 87.782 | stealthy | 162.034 |
| fraud | 20.000 | stealthy | one_hot_t1 | 213.949 | noisy | 258.571 |
| fraud | 30.000 | noisy | grid_0.5_0.0_0.5 | 65.662 | stealthy | 112.547 |
| fraud | 30.000 | stealthy | one_hot_t1 | 188.661 | noisy | 264.236 |
| snort | 1000.000 | noisy | one_hot_t1 | 0.000 | stealthy | 45.501 |
| snort | 1000.000 | stealthy | one_hot_t0 | 58.157 | noisy | 75.370 |
| snort | 1500.000 | noisy | one_hot_t1 | 0.000 | stealthy | 41.608 |
| snort | 1500.000 | stealthy | one_hot_t0 | 53.273 | noisy | 75.370 |
| snort | 500.000 | noisy | one_hot_t1 | 0.000 | stealthy | 53.446 |
| snort | 500.000 | stealthy | one_hot_t0 | 64.954 | noisy | 75.370 |
| suricata | 1000.000 | noisy | one_hot_t2 | 4.405 | stealthy | 103.641 |
| suricata | 1000.000 | stealthy | one_hot_t1 | 80.984 | noisy | 146.544 |
| suricata | 1500.000 | noisy | one_hot_t2 | 0.966 | stealthy | 96.786 |
| suricata | 1500.000 | stealthy | one_hot_t1 | 71.986 | noisy | 146.544 |
| suricata | 500.000 | noisy | one_hot_t2 | 20.103 | stealthy | 115.237 |
| suricata | 500.000 | stealthy | one_hot_t1 | 95.956 | noisy | 146.544 |

## E. Sensitivity: type separability vs value of the belief (fixed attackers)

| dataset | budget | separability | difference | n | mean | std | CI low | CI high | Wilcoxon p | t p |
|---|---|---|---|---|---|---|---|---|---|---|
| fraud | 20.000 | 0.000 | BLIND - BELIEF | 5 | -0.500 | 8.146 | -10.614 | 9.614 | 0.812 | 0.897 |
| fraud | 20.000 | 0.250 | BLIND - BELIEF | 5 | 2.617 | 9.251 | -8.870 | 14.103 | 1.000 | 0.561 |
| fraud | 20.000 | 0.500 | BLIND - BELIEF | 5 | 0.078 | 7.602 | -9.361 | 9.517 | 0.715 | 0.983 |
| fraud | 20.000 | 0.750 | BLIND - BELIEF | 5 | 0.123 | 5.476 | -6.677 | 6.922 | 0.625 | 0.962 |
| fraud | 20.000 | 1.000 | BLIND - BELIEF | 5 | 5.327 | 4.747 | -0.567 | 11.222 | 0.125 | 0.066 |
| fraud | 20.000 | 0.000 | BLIND - INFORMED | 5 | -1.840 | 6.438 | -9.834 | 6.154 | 0.625 | 0.558 |
| fraud | 20.000 | 0.250 | BLIND - INFORMED | 5 | -0.038 | 5.406 | -6.750 | 6.675 | 1.000 | 0.988 |
| fraud | 20.000 | 0.500 | BLIND - INFORMED | 5 | 0.680 | 8.649 | -10.059 | 11.420 | 0.812 | 0.869 |
| fraud | 20.000 | 0.750 | BLIND - INFORMED | 5 | 9.796 | 6.029 | 2.310 | 17.282 | 0.062 | 0.022 |
| fraud | 20.000 | 1.000 | BLIND - INFORMED | 5 | 25.049 | 3.423 | 20.798 | 29.299 | 0.062 | 0.000 |

