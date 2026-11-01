# Signaling-game results (full_v2 mode)

Completed jobs: 82 (dataset x budget x seed). Oracle: ddpg. Defender loss = expected discounted loss per episode, lower is better. n = number of independent seeds.

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
| fraud | 30.000 | BLIND | 9 | 156.982 | 8.773 | 150.239 | 163.726 |
| fraud | 30.000 | INFORMED | 9 | 134.698 | 2.372 | 132.875 | 136.521 |
| fraud | 30.000 | BELIEF | 9 | 149.940 | 2.410 | 148.087 | 151.792 |
| fraud | 30.000 | baseline_uniform | 9 | 165.351 | 0.000 | 165.351 | 165.351 |
| fraud | 30.000 | baseline_newest | 9 | 165.351 | 0.000 | 165.351 | 165.351 |
| fraud | 30.000 | baseline_proportion | 9 | 184.536 | 0.000 | 184.536 | 184.536 |
| fraud | 30.000 | baseline_fraud_rule | 9 | 157.033 | 0.000 | 157.033 | 157.033 |
| fraud | 30.000 | baseline_aics | 9 | 172.658 | 0.000 | 172.658 | 172.658 |
| fraud | 30.000 | baseline_icde | 9 | 193.422 | 0.000 | 193.422 | 193.422 |
| suricata | 500.000 | BLIND | 8 | 70.443 | 1.766 | 68.967 | 71.920 |
| suricata | 500.000 | INFORMED | 8 | 61.278 | 0.989 | 60.451 | 62.105 |
| suricata | 500.000 | BELIEF | 8 | 62.320 | 1.194 | 61.323 | 63.318 |
| suricata | 500.000 | baseline_uniform | 8 | 94.380 | 0.000 | 94.380 | 94.380 |
| suricata | 500.000 | baseline_newest | 8 | 94.380 | 0.000 | 94.380 | 94.380 |
| suricata | 500.000 | baseline_proportion | 8 | 96.349 | 0.000 | 96.349 | 96.349 |
| suricata | 500.000 | baseline_suricata_rule | 8 | 88.549 | 0.000 | 88.549 | 88.549 |
| suricata | 1000.000 | BLIND | 9 | 55.805 | 2.057 | 54.223 | 57.386 |
| suricata | 1000.000 | INFORMED | 9 | 44.287 | 1.172 | 43.386 | 45.188 |
| suricata | 1000.000 | BELIEF | 9 | 45.359 | 0.892 | 44.673 | 46.045 |
| suricata | 1000.000 | baseline_uniform | 9 | 79.490 | 0.000 | 79.490 | 79.490 |
| suricata | 1000.000 | baseline_newest | 9 | 79.490 | 0.000 | 79.490 | 79.490 |
| suricata | 1000.000 | baseline_proportion | 9 | 82.549 | 0.000 | 82.549 | 82.549 |
| suricata | 1000.000 | baseline_suricata_rule | 9 | 76.844 | 0.000 | 76.844 | 76.844 |
| suricata | 1500.000 | BLIND | 9 | 48.661 | 1.717 | 47.341 | 49.980 |
| suricata | 1500.000 | INFORMED | 9 | 37.459 | 1.411 | 36.375 | 38.544 |
| suricata | 1500.000 | BELIEF | 9 | 38.473 | 0.609 | 38.005 | 38.941 |
| suricata | 1500.000 | baseline_uniform | 9 | 69.908 | 0.000 | 69.908 | 69.908 |
| suricata | 1500.000 | baseline_newest | 9 | 69.908 | 0.000 | 69.908 | 69.908 |
| suricata | 1500.000 | baseline_proportion | 9 | 73.941 | 0.000 | 73.941 | 73.941 |
| suricata | 1500.000 | baseline_suricata_rule | 9 | 69.176 | 0.000 | 69.176 | 69.176 |
| snort | 500.000 | BLIND | 10 | 32.977 | 1.562 | 31.859 | 34.094 |
| snort | 500.000 | INFORMED | 10 | 32.366 | 0.037 | 32.339 | 32.392 |
| snort | 500.000 | BELIEF | 10 | 32.437 | 0.242 | 32.264 | 32.611 |
| snort | 500.000 | baseline_uniform | 10 | 32.349 | 0.000 | 32.349 | 32.349 |
| snort | 500.000 | baseline_newest | 10 | 32.349 | 0.000 | 32.349 | 32.349 |
| snort | 500.000 | baseline_proportion | 10 | 59.072 | 0.000 | 59.072 | 59.072 |
| snort | 500.000 | baseline_snort_rule | 10 | 38.004 | 0.000 | 38.004 | 38.004 |
| snort | 1000.000 | BLIND | 10 | 29.997 | 2.754 | 28.027 | 31.967 |
| snort | 1000.000 | INFORMED | 10 | 29.347 | 1.099 | 28.560 | 30.133 |
| snort | 1000.000 | BELIEF | 10 | 28.917 | 0.002 | 28.916 | 28.919 |
| snort | 1000.000 | baseline_uniform | 10 | 28.916 | 0.000 | 28.916 | 28.916 |
| snort | 1000.000 | baseline_newest | 10 | 28.916 | 0.000 | 28.916 | 28.916 |
| snort | 1000.000 | baseline_proportion | 10 | 51.322 | 0.000 | 51.322 | 51.322 |
| snort | 1000.000 | baseline_snort_rule | 10 | 38.004 | 0.000 | 38.004 | 38.004 |
| snort | 1500.000 | BLIND | 9 | 26.809 | 0.665 | 26.298 | 27.321 |
| snort | 1500.000 | INFORMED | 9 | 27.057 | 1.409 | 25.974 | 28.140 |
| snort | 1500.000 | BELIEF | 9 | 26.588 | 0.000 | 26.588 | 26.588 |
| snort | 1500.000 | baseline_uniform | 9 | 26.588 | 0.000 | 26.588 | 26.588 |
| snort | 1500.000 | baseline_newest | 9 | 26.588 | 0.000 | 26.588 | 26.588 |
| snort | 1500.000 | baseline_proportion | 9 | 45.903 | 0.000 | 45.903 | 45.903 |
| snort | 1500.000 | baseline_snort_rule | 9 | 38.004 | 0.000 | 38.004 | 38.004 |

Paired tests (negative mean difference = first defender has LOWER loss):

| dataset | budget | comparison | n | mean diff | Wilcoxon p | t-test p | Wilcoxon p (Holm) |
|---|---|---|---|---|---|---|---|
| fraud | 10.000 | BELIEF - BLIND | 9 | -1.167 | 0.612 | 0.637 | 1.000 |
| fraud | 10.000 | INFORMED - BLIND | 9 | -8.244 | 0.025 | 0.028 | 0.376 |
| fraud | 10.000 | BELIEF - INFORMED | 9 | 7.078 | 0.017 | 0.002 | 0.294 |
| fraud | 20.000 | BELIEF - BLIND | 9 | -6.033 | 0.020 | 0.007 | 0.312 |
| fraud | 20.000 | INFORMED - BLIND | 9 | -24.364 | 0.004 | 0.000 | 0.105 |
| fraud | 20.000 | BELIEF - INFORMED | 9 | 18.331 | 0.004 | 0.000 | 0.105 |
| fraud | 30.000 | BELIEF - BLIND | 9 | -7.043 | 0.027 | 0.024 | 0.383 |
| fraud | 30.000 | INFORMED - BLIND | 9 | -22.284 | 0.004 | 0.000 | 0.105 |
| fraud | 30.000 | BELIEF - INFORMED | 9 | 15.242 | 0.004 | 0.000 | 0.105 |
| suricata | 500.000 | BELIEF - BLIND | 8 | -8.123 | 0.008 | 0.000 | 0.148 |
| suricata | 500.000 | INFORMED - BLIND | 8 | -9.165 | 0.008 | 0.000 | 0.148 |
| suricata | 500.000 | BELIEF - INFORMED | 8 | 1.042 | 0.148 | 0.080 | 1.000 |
| suricata | 1000.000 | BELIEF - BLIND | 9 | -10.446 | 0.004 | 0.000 | 0.105 |
| suricata | 1000.000 | INFORMED - BLIND | 9 | -11.518 | 0.004 | 0.000 | 0.105 |
| suricata | 1000.000 | BELIEF - INFORMED | 9 | 1.072 | 0.098 | 0.070 | 1.000 |
| suricata | 1500.000 | BELIEF - BLIND | 9 | -10.188 | 0.004 | 0.000 | 0.105 |
| suricata | 1500.000 | INFORMED - BLIND | 9 | -11.201 | 0.004 | 0.000 | 0.105 |
| suricata | 1500.000 | BELIEF - INFORMED | 9 | 1.014 | 0.164 | 0.114 | 1.000 |
| snort | 500.000 | BELIEF - BLIND | 10 | -0.539 | 0.770 | 0.319 | 1.000 |
| snort | 500.000 | INFORMED - BLIND | 10 | -0.611 | 0.064 | 0.247 | 0.773 |
| snort | 500.000 | BELIEF - INFORMED | 10 | 0.071 | 0.314 | 0.388 | 1.000 |
| snort | 1000.000 | BELIEF - BLIND | 10 | -1.080 | 0.036 | 0.246 | 0.464 |
| snort | 1000.000 | INFORMED - BLIND | 10 | -0.651 | 0.401 | 0.528 | 1.000 |
| snort | 1000.000 | BELIEF - INFORMED | 10 | -0.429 | 0.293 | 0.248 | 1.000 |
| snort | 1500.000 | BELIEF - BLIND | 9 | -0.222 | 0.180 | 0.346 | 1.000 |
| snort | 1500.000 | INFORMED - BLIND | 9 | 0.248 | 0.655 | 0.661 | 1.000 |
| snort | 1500.000 | BELIEF - INFORMED | 9 | -0.470 | 0.317 | 0.347 | 1.000 |

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
| fraud | 30.000 | ZS_BLIND | 9 | 186.965 | 2.434 | 185.094 | 188.835 | 3.556 | 0.000 |
| fraud | 30.000 | SIG | 9 | 183.955 | 4.441 | 180.541 | 187.368 | 4.556 | 0.030 |
| suricata | 500.000 | ZS_BLIND | 8 | 37.533 | 1.880 | 35.961 | 39.104 | 4.750 | 0.000 |
| suricata | 500.000 | SIG | 8 | 36.956 | 0.211 | 36.780 | 37.133 | 4.750 | 0.000 |
| suricata | 1000.000 | ZS_BLIND | 9 | 34.151 | 0.171 | 34.020 | 34.282 | 3.778 | 0.000 |
| suricata | 1000.000 | SIG | 9 | 34.067 | 0.395 | 33.763 | 34.370 | 4.778 | 0.000 |
| suricata | 1500.000 | ZS_BLIND | 9 | 33.041 | 0.835 | 32.400 | 33.683 | 5.333 | 0.000 |
| suricata | 1500.000 | SIG | 9 | 33.788 | 1.169 | 32.890 | 34.686 | 4.222 | 0.000 |
| snort | 500.000 | ZS_BLIND | 10 | 8.143 | 0.000 | 8.143 | 8.143 | 3.200 | 1.000 |
| snort | 500.000 | GS_BLIND | 10 | 8.143 | 0.000 | 8.143 | 8.143 | 3.000 | 1.000 |
| snort | 500.000 | SIG | 10 | 8.143 | 0.000 | 8.143 | 8.143 | 3.200 | 1.000 |
| snort | 1000.000 | ZS_BLIND | 10 | 4.796 | 0.000 | 4.796 | 4.796 | 3.200 | 1.000 |
| snort | 1000.000 | GS_BLIND | 10 | 4.796 | 0.000 | 4.796 | 4.796 | 3.200 | 1.000 |
| snort | 1000.000 | SIG | 10 | 4.796 | 0.000 | 4.796 | 4.796 | 3.200 | 1.000 |
| snort | 1500.000 | ZS_BLIND | 9 | 3.111 | 0.000 | 3.111 | 3.111 | 3.222 | 1.000 |
| snort | 1500.000 | GS_BLIND | 9 | 3.111 | 0.000 | 3.111 | 3.111 | 3.111 | 1.000 |
| snort | 1500.000 | SIG | 9 | 3.111 | 0.000 | 3.111 | 3.111 | 3.111 | 1.000 |

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
| fraud | 30.000 | ZS_BLIND | 188.230 | 188.063 | 155.740 |  | 189.819 |
| fraud | 30.000 | SIG | 186.159 | 185.328 | 156.521 |  | 187.250 |
| fraud | 30.000 | baseline_uniform | 204.117 | 203.421 | 165.351 |  | 205.800 |
| fraud | 30.000 | baseline_newest | 204.117 | 203.421 | 165.351 |  | 205.800 |
| fraud | 30.000 | baseline_proportion | 212.562 | 211.744 | 184.536 |  | 213.015 |
| fraud | 30.000 | baseline_fraud_rule | 186.898 | 185.941 | 157.033 |  | 187.678 |
| fraud | 30.000 | baseline_aics | 189.760 | 188.899 | 172.658 |  | 190.064 |
| fraud | 30.000 | baseline_icde | 206.855 | 206.458 | 193.422 |  | 207.398 |
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
| suricata | 1000.000 | ZS_BLIND | 34.340 | 34.340 | 75.707 |  | 75.707 |
| suricata | 1000.000 | SIG | 34.518 | 34.518 | 69.186 |  | 69.186 |
| suricata | 1000.000 | baseline_uniform | 48.208 | 48.208 | 79.490 |  | 79.490 |
| suricata | 1000.000 | baseline_newest | 48.208 | 48.208 | 79.490 |  | 79.490 |
| suricata | 1000.000 | baseline_proportion | 56.391 | 56.391 | 82.549 |  | 82.549 |
| suricata | 1000.000 | baseline_fraud_rule |  |  |  |  |  |
| suricata | 1000.000 | baseline_aics |  |  |  |  |  |
| suricata | 1000.000 | baseline_icde |  |  |  |  |  |
| suricata | 1000.000 | GS_BLIND |  |  |  |  |  |
| suricata | 1000.000 | baseline_snort_rule |  |  |  |  |  |
| suricata | 1000.000 | baseline_suricata_rule | 56.650 | 56.650 | 76.844 |  | 76.844 |
| suricata | 1500.000 | ZS_BLIND | 33.270 | 33.270 | 69.511 |  | 69.511 |
| suricata | 1500.000 | SIG | 34.113 | 34.113 | 63.720 |  | 63.720 |
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
| fraud | 20.000 | SIG - ZS_BLIND | ZS_BLIND_attacker | 9 | -4.868 | -2.185 | 0.020 | 0.010 | 0.918 |
| fraud | 20.000 | SIG - ZS_BLIND | SIG_attacker | 9 | -4.304 | -1.919 | 0.027 | 0.010 | 1.000 |
| fraud | 20.000 | SIG - ZS_BLIND | fixed_uniform | 9 | -4.256 | -2.378 | 0.164 | 0.123 | 1.000 |
| fraud | 20.000 | SIG - ZS_BLIND | worst | 9 | -4.347 | -1.930 | 0.020 | 0.009 | 0.918 |
| fraud | 30.000 | SIG - ZS_BLIND | ZS_BLIND_attacker | 9 | -2.071 | -1.100 | 0.164 | 0.127 | 1.000 |
| fraud | 30.000 | SIG - ZS_BLIND | SIG_attacker | 9 | -2.736 | -1.455 | 0.129 | 0.086 | 1.000 |
| fraud | 30.000 | SIG - ZS_BLIND | fixed_uniform | 9 | 0.782 | 0.502 | 0.652 | 0.680 | 1.000 |
| fraud | 30.000 | SIG - ZS_BLIND | worst | 9 | -2.568 | -1.353 | 0.129 | 0.091 | 1.000 |
| suricata | 500.000 | SIG - ZS_BLIND | ZS_BLIND_attacker | 8 | 2.385 | 6.178 | 0.547 | 0.301 | 1.000 |
| suricata | 500.000 | SIG - ZS_BLIND | SIG_attacker | 8 | -2.331 | -5.738 | 0.742 | 0.399 | 1.000 |
| suricata | 500.000 | SIG - ZS_BLIND | fixed_uniform | 8 | -1.689 | -1.938 | 0.461 | 0.521 | 1.000 |
| suricata | 500.000 | SIG - ZS_BLIND | worst | 8 | -1.689 | -1.938 | 0.461 | 0.521 | 1.000 |
| suricata | 1000.000 | SIG - ZS_BLIND | ZS_BLIND_attacker | 9 | 0.178 | 0.518 | 0.570 | 0.359 | 1.000 |
| suricata | 1000.000 | SIG - ZS_BLIND | SIG_attacker | 9 | 0.178 | 0.518 | 0.570 | 0.359 | 1.000 |
| suricata | 1000.000 | SIG - ZS_BLIND | fixed_uniform | 9 | -6.520 | -8.613 | 0.203 | 0.155 | 1.000 |
| suricata | 1000.000 | SIG - ZS_BLIND | worst | 9 | -6.520 | -8.613 | 0.203 | 0.155 | 1.000 |
| suricata | 1500.000 | SIG - ZS_BLIND | ZS_BLIND_attacker | 9 | 0.844 | 2.535 | 0.129 | 0.141 | 1.000 |
| suricata | 1500.000 | SIG - ZS_BLIND | SIG_attacker | 9 | 0.844 | 2.535 | 0.129 | 0.141 | 1.000 |
| suricata | 1500.000 | SIG - ZS_BLIND | fixed_uniform | 9 | -5.791 | -8.331 | 0.359 | 0.371 | 1.000 |
| suricata | 1500.000 | SIG - ZS_BLIND | worst | 9 | -5.791 | -8.331 | 0.359 | 0.371 | 1.000 |
| snort | 500.000 | SIG - ZS_BLIND | ZS_BLIND_attacker | 10 | 0.000 | 0.000 | nan | nan | nan |
| snort | 500.000 | SIG - ZS_BLIND | SIG_attacker | 10 | 0.000 | 0.000 | nan | nan | nan |
| snort | 500.000 | SIG - ZS_BLIND | fixed_uniform | 10 | 0.000 | 0.000 | nan | nan | nan |
| snort | 500.000 | SIG - ZS_BLIND | GS_BLIND_attacker | 10 | 0.000 | 0.000 | nan | nan | nan |
| snort | 500.000 | SIG - ZS_BLIND | worst | 10 | 0.000 | 0.000 | nan | nan | nan |
| snort | 500.000 | SIG - GS_BLIND | ZS_BLIND_attacker | 10 | 0.000 | 0.000 | nan | nan | nan |
| snort | 500.000 | SIG - GS_BLIND | SIG_attacker | 10 | 0.000 | 0.000 | nan | nan | nan |
| snort | 500.000 | SIG - GS_BLIND | fixed_uniform | 10 | 0.000 | 0.000 | nan | nan | nan |
| snort | 500.000 | SIG - GS_BLIND | GS_BLIND_attacker | 10 | 0.000 | 0.000 | nan | nan | nan |
| snort | 500.000 | SIG - GS_BLIND | worst | 10 | 0.000 | 0.000 | nan | nan | nan |
| snort | 1000.000 | SIG - ZS_BLIND | ZS_BLIND_attacker | 10 | 0.000 | 0.000 | nan | nan | nan |
| snort | 1000.000 | SIG - ZS_BLIND | SIG_attacker | 10 | 0.000 | 0.000 | nan | nan | nan |
| snort | 1000.000 | SIG - ZS_BLIND | fixed_uniform | 10 | 0.000 | 0.000 | nan | nan | nan |
| snort | 1000.000 | SIG - ZS_BLIND | GS_BLIND_attacker | 10 | 0.000 | 0.000 | nan | nan | nan |
| snort | 1000.000 | SIG - ZS_BLIND | worst | 10 | 0.000 | 0.000 | nan | nan | nan |
| snort | 1000.000 | SIG - GS_BLIND | ZS_BLIND_attacker | 10 | 0.000 | 0.000 | nan | nan | nan |
| snort | 1000.000 | SIG - GS_BLIND | SIG_attacker | 10 | 0.000 | 0.000 | nan | nan | nan |
| snort | 1000.000 | SIG - GS_BLIND | fixed_uniform | 10 | 0.000 | 0.000 | nan | nan | nan |
| snort | 1000.000 | SIG - GS_BLIND | GS_BLIND_attacker | 10 | 0.000 | 0.000 | nan | nan | nan |
| snort | 1000.000 | SIG - GS_BLIND | worst | 10 | 0.000 | 0.000 | nan | nan | nan |
| snort | 1500.000 | SIG - ZS_BLIND | ZS_BLIND_attacker | 9 | 0.000 | 0.000 | nan | nan | nan |
| snort | 1500.000 | SIG - ZS_BLIND | SIG_attacker | 9 | 0.000 | 0.000 | nan | nan | nan |
| snort | 1500.000 | SIG - ZS_BLIND | fixed_uniform | 9 | 0.000 | 0.000 | nan | nan | nan |
| snort | 1500.000 | SIG - ZS_BLIND | GS_BLIND_attacker | 9 | 0.000 | 0.000 | nan | nan | nan |
| snort | 1500.000 | SIG - ZS_BLIND | worst | 9 | 0.000 | 0.000 | nan | nan | nan |
| snort | 1500.000 | SIG - GS_BLIND | ZS_BLIND_attacker | 9 | 0.000 | 0.000 | nan | nan | nan |
| snort | 1500.000 | SIG - GS_BLIND | SIG_attacker | 9 | 0.000 | 0.000 | nan | nan | nan |
| snort | 1500.000 | SIG - GS_BLIND | fixed_uniform | 9 | 0.000 | 0.000 | nan | nan | nan |
| snort | 1500.000 | SIG - GS_BLIND | GS_BLIND_attacker | 9 | 0.000 | 0.000 | nan | nan | nan |
| snort | 1500.000 | SIG - GS_BLIND | worst | 9 | 0.000 | 0.000 | nan | nan | nan |

## C. Belief diagnostics (signaling game, final equilibrium)

| dataset | budget | n (belief policy in support) | n (no belief policy in support) | |b_def - b_exactBayes| | off-path rate (def. conjecture) | off-path rate (exact) | final belief on true type |
|---|---|---|---|---|---|---|---|
| fraud | 10.000 | 9 | 0 | 0.069 | 0.000 | 0.000 | 0.731 |
| fraud | 20.000 | 9 | 0 | 0.063 | 0.000 | 0.000 | 0.742 |
| fraud | 30.000 | 9 | 0 | 0.023 | 0.000 | 0.000 | 0.750 |
| suricata | 500.000 | 8 | 0 | 0.000 | 0.000 | 0.000 | 0.717 |
| suricata | 1000.000 | 9 | 0 | 0.000 | 0.000 | 0.000 | 0.717 |
| suricata | 1500.000 | 9 | 0 | 0.000 | 0.000 | 0.000 | 0.717 |
| snort | 500.000 | 0 | 10 |  |  |  |  |
| snort | 1000.000 | 0 | 10 |  |  |  |  |
| snort | 1500.000 | 0 | 9 |  |  |  |  |

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

