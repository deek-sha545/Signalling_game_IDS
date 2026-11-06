# Signaling-game results (full_v2 mode)

Completed jobs: 90 (dataset x budget x seed). Oracle: ddpg. Defender loss = expected discounted loss per episode, lower is better. n = number of independent seeds.

## A. Defenders against FIXED type-based attackers (conditions a, b, c + baselines)

| dataset | budget | defender | n | mean loss | std | CI low | CI high |
|---|---|---|---|---|---|---|---|
| fraud | 10.000 | BLIND | 10 | 198.878 | 5.782 | 194.742 | 203.014 |
| fraud | 10.000 | INFORMED | 10 | 190.634 | 4.462 | 187.442 | 193.826 |
| fraud | 10.000 | BELIEF | 10 | 197.734 | 1.878 | 196.390 | 199.078 |
| fraud | 10.000 | baseline_uniform | 10 | 229.750 | 0.000 | 229.750 | 229.750 |
| fraud | 10.000 | baseline_newest | 10 | 229.750 | 0.000 | 229.750 | 229.750 |
| fraud | 10.000 | baseline_proportion | 10 | 241.640 | 0.000 | 241.640 | 241.640 |
| fraud | 10.000 | baseline_fraud_rule | 10 | 234.159 | 0.000 | 234.159 | 234.159 |
| fraud | 10.000 | baseline_aics | 10 | 246.618 | 0.000 | 246.618 | 246.618 |
| fraud | 10.000 | baseline_icde | 10 | 246.618 | 0.000 | 246.618 | 246.618 |
| fraud | 20.000 | BLIND | 10 | 179.221 | 2.235 | 177.622 | 180.820 |
| fraud | 20.000 | INFORMED | 10 | 154.792 | 2.330 | 153.125 | 156.459 |
| fraud | 20.000 | BELIEF | 10 | 173.414 | 5.282 | 169.635 | 177.192 |
| fraud | 20.000 | baseline_uniform | 10 | 196.967 | 0.000 | 196.967 | 196.967 |
| fraud | 20.000 | baseline_newest | 10 | 196.967 | 0.000 | 196.967 | 196.967 |
| fraud | 20.000 | baseline_proportion | 10 | 211.342 | 0.000 | 211.342 | 211.342 |
| fraud | 20.000 | baseline_fraud_rule | 10 | 194.526 | 0.000 | 194.526 | 194.526 |
| fraud | 20.000 | baseline_aics | 10 | 215.838 | 0.000 | 215.838 | 215.838 |
| fraud | 20.000 | baseline_icde | 10 | 216.548 | 0.000 | 216.548 | 216.548 |
| fraud | 30.000 | BLIND | 10 | 156.756 | 8.302 | 150.817 | 162.694 |
| fraud | 30.000 | INFORMED | 10 | 134.325 | 2.528 | 132.516 | 136.133 |
| fraud | 30.000 | BELIEF | 10 | 149.233 | 3.186 | 146.954 | 151.512 |
| fraud | 30.000 | baseline_uniform | 10 | 165.351 | 0.000 | 165.351 | 165.351 |
| fraud | 30.000 | baseline_newest | 10 | 165.351 | 0.000 | 165.351 | 165.351 |
| fraud | 30.000 | baseline_proportion | 10 | 184.536 | 0.000 | 184.536 | 184.536 |
| fraud | 30.000 | baseline_fraud_rule | 10 | 157.033 | 0.000 | 157.033 | 157.033 |
| fraud | 30.000 | baseline_aics | 10 | 172.658 | 0.000 | 172.658 | 172.658 |
| fraud | 30.000 | baseline_icde | 10 | 193.422 | 0.000 | 193.422 | 193.422 |
| suricata | 500.000 | BLIND | 10 | 70.621 | 2.203 | 69.045 | 72.198 |
| suricata | 500.000 | INFORMED | 10 | 61.265 | 0.920 | 60.606 | 61.923 |
| suricata | 500.000 | BELIEF | 10 | 62.433 | 1.355 | 61.463 | 63.402 |
| suricata | 500.000 | baseline_uniform | 10 | 94.380 | 0.000 | 94.380 | 94.380 |
| suricata | 500.000 | baseline_newest | 10 | 94.380 | 0.000 | 94.380 | 94.380 |
| suricata | 500.000 | baseline_proportion | 10 | 96.349 | 0.000 | 96.349 | 96.349 |
| suricata | 500.000 | baseline_suricata_rule | 10 | 88.549 | 0.000 | 88.549 | 88.549 |
| suricata | 1000.000 | BLIND | 10 | 55.554 | 2.096 | 54.054 | 57.053 |
| suricata | 1000.000 | INFORMED | 10 | 44.289 | 1.105 | 43.498 | 45.079 |
| suricata | 1000.000 | BELIEF | 10 | 45.370 | 0.842 | 44.767 | 45.972 |
| suricata | 1000.000 | baseline_uniform | 10 | 79.490 | 0.000 | 79.490 | 79.490 |
| suricata | 1000.000 | baseline_newest | 10 | 79.490 | 0.000 | 79.490 | 79.490 |
| suricata | 1000.000 | baseline_proportion | 10 | 82.549 | 0.000 | 82.549 | 82.549 |
| suricata | 1000.000 | baseline_suricata_rule | 10 | 76.844 | 0.000 | 76.844 | 76.844 |
| suricata | 1500.000 | BLIND | 10 | 48.577 | 1.640 | 47.403 | 49.750 |
| suricata | 1500.000 | INFORMED | 10 | 37.383 | 1.352 | 36.416 | 38.350 |
| suricata | 1500.000 | BELIEF | 10 | 38.852 | 1.329 | 37.901 | 39.803 |
| suricata | 1500.000 | baseline_uniform | 10 | 69.908 | 0.000 | 69.908 | 69.908 |
| suricata | 1500.000 | baseline_newest | 10 | 69.908 | 0.000 | 69.908 | 69.908 |
| suricata | 1500.000 | baseline_proportion | 10 | 73.941 | 0.000 | 73.941 | 73.941 |
| suricata | 1500.000 | baseline_suricata_rule | 10 | 69.176 | 0.000 | 69.176 | 69.176 |
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
| snort | 1500.000 | BLIND | 10 | 26.787 | 0.631 | 26.336 | 27.239 |
| snort | 1500.000 | INFORMED | 10 | 27.010 | 1.337 | 26.054 | 27.966 |
| snort | 1500.000 | BELIEF | 10 | 26.591 | 0.012 | 26.583 | 26.600 |
| snort | 1500.000 | baseline_uniform | 10 | 26.588 | 0.000 | 26.588 | 26.588 |
| snort | 1500.000 | baseline_newest | 10 | 26.588 | 0.000 | 26.588 | 26.588 |
| snort | 1500.000 | baseline_proportion | 10 | 45.903 | 0.000 | 45.903 | 45.903 |
| snort | 1500.000 | baseline_snort_rule | 10 | 38.004 | 0.000 | 38.004 | 38.004 |

Paired tests (negative mean difference = first defender has LOWER loss):

| dataset | budget | comparison | n | mean diff | Wilcoxon p | t-test p | Wilcoxon p (Holm) |
|---|---|---|---|---|---|---|---|
| fraud | 10.000 | BELIEF - BLIND | 10 | -1.144 | 0.779 | 0.604 | 1.000 |
| fraud | 10.000 | INFORMED - BLIND | 10 | -8.244 | 0.015 | 0.015 | 0.212 |
| fraud | 10.000 | BELIEF - INFORMED | 10 | 7.100 | 0.011 | 0.001 | 0.174 |
| fraud | 20.000 | BELIEF - BLIND | 10 | -5.807 | 0.010 | 0.004 | 0.166 |
| fraud | 20.000 | INFORMED - BLIND | 10 | -24.429 | 0.002 | 0.000 | 0.053 |
| fraud | 20.000 | BELIEF - INFORMED | 10 | 18.622 | 0.002 | 0.000 | 0.053 |
| fraud | 30.000 | BELIEF - BLIND | 10 | -7.522 | 0.014 | 0.010 | 0.205 |
| fraud | 30.000 | INFORMED - BLIND | 10 | -22.431 | 0.002 | 0.000 | 0.053 |
| fraud | 30.000 | BELIEF - INFORMED | 10 | 14.909 | 0.002 | 0.000 | 0.053 |
| suricata | 500.000 | BELIEF - BLIND | 10 | -8.189 | 0.002 | 0.000 | 0.053 |
| suricata | 500.000 | INFORMED - BLIND | 10 | -9.357 | 0.002 | 0.000 | 0.053 |
| suricata | 500.000 | BELIEF - INFORMED | 10 | 1.168 | 0.049 | 0.027 | 0.586 |
| suricata | 1000.000 | BELIEF - BLIND | 10 | -10.184 | 0.002 | 0.000 | 0.053 |
| suricata | 1000.000 | INFORMED - BLIND | 10 | -11.265 | 0.002 | 0.000 | 0.053 |
| suricata | 1000.000 | BELIEF - INFORMED | 10 | 1.081 | 0.064 | 0.043 | 0.709 |
| suricata | 1500.000 | BELIEF - BLIND | 10 | -9.725 | 0.002 | 0.000 | 0.053 |
| suricata | 1500.000 | INFORMED - BLIND | 10 | -11.193 | 0.002 | 0.000 | 0.053 |
| suricata | 1500.000 | BELIEF - INFORMED | 10 | 1.469 | 0.084 | 0.060 | 0.756 |
| snort | 500.000 | BELIEF - BLIND | 10 | -0.539 | 0.770 | 0.319 | 1.000 |
| snort | 500.000 | INFORMED - BLIND | 10 | -0.611 | 0.064 | 0.247 | 0.709 |
| snort | 500.000 | BELIEF - INFORMED | 10 | 0.071 | 0.314 | 0.388 | 1.000 |
| snort | 1000.000 | BELIEF - BLIND | 10 | -1.080 | 0.036 | 0.246 | 0.464 |
| snort | 1000.000 | INFORMED - BLIND | 10 | -0.651 | 0.401 | 0.528 | 1.000 |
| snort | 1000.000 | BELIEF - INFORMED | 10 | -0.429 | 0.293 | 0.248 | 1.000 |
| snort | 1500.000 | BELIEF - BLIND | 10 | -0.196 | 0.593 | 0.353 | 1.000 |
| snort | 1500.000 | INFORMED - BLIND | 10 | 0.223 | 0.655 | 0.658 | 1.000 |
| snort | 1500.000 | BELIEF - INFORMED | 10 | -0.419 | 0.655 | 0.348 | 1.000 |

## B. Equilibrium (double oracle) results: zero-sum vs general-sum vs signaling

For suricata and fraud test.py defines no separate attacker gain, so the general-sum game equals the zero-sum game and GS_BLIND is not run separately; there SIG differs from ZS_BLIND ONLY by the belief/types. Snort has distinct gains.

### B1. Defender loss at the restricted-game equilibrium (each game against its OWN attacker)

Caution: these are values of DIFFERENT games (the attacker objective differs between zero-sum and general-sum), so they are not a like-for-like comparison of defenders; see B2.

"weight newest" = average equilibrium probability on the initial non-learned `newest` defender; a value near 1 means the RL best responses never beat that heuristic in the restricted game.

| dataset | budget | game | n | mean loss | std | CI low | CI high | DO iterations | weight newest |
|---|---|---|---|---|---|---|---|---|---|
| fraud | 10.000 | ZS_BLIND | 10 | 255.045 | 1.583 | 253.912 | 256.177 | 3.900 | 0.000 |
| fraud | 10.000 | SIG | 10 | 253.769 | 1.604 | 252.622 | 254.917 | 4.200 | 0.000 |
| fraud | 20.000 | ZS_BLIND | 10 | 223.345 | 6.309 | 218.831 | 227.858 | 3.500 | 0.100 |
| fraud | 20.000 | SIG | 10 | 220.930 | 2.791 | 218.934 | 222.927 | 3.500 | 0.000 |
| fraud | 30.000 | ZS_BLIND | 10 | 186.916 | 2.300 | 185.271 | 188.561 | 3.500 | 0.000 |
| fraud | 30.000 | SIG | 10 | 183.700 | 4.263 | 180.650 | 186.750 | 4.500 | 0.027 |
| suricata | 500.000 | ZS_BLIND | 10 | 37.388 | 1.686 | 36.181 | 38.594 | 4.800 | 0.000 |
| suricata | 500.000 | SIG | 10 | 36.924 | 0.199 | 36.782 | 37.066 | 4.900 | 0.000 |
| suricata | 1000.000 | ZS_BLIND | 10 | 34.140 | 0.165 | 34.022 | 34.258 | 3.800 | 0.000 |
| suricata | 1000.000 | SIG | 10 | 34.098 | 0.385 | 33.823 | 34.373 | 4.800 | 0.000 |
| suricata | 1500.000 | ZS_BLIND | 10 | 33.055 | 0.788 | 32.492 | 33.619 | 5.400 | 0.000 |
| suricata | 1500.000 | SIG | 10 | 30.725 | 9.748 | 23.752 | 37.698 | 4.200 | 0.000 |
| snort | 500.000 | ZS_BLIND | 10 | 8.143 | 0.000 | 8.143 | 8.143 | 3.200 | 1.000 |
| snort | 500.000 | GS_BLIND | 10 | 8.143 | 0.000 | 8.143 | 8.143 | 3.000 | 1.000 |
| snort | 500.000 | SIG | 10 | 8.143 | 0.000 | 8.143 | 8.143 | 3.200 | 1.000 |
| snort | 1000.000 | ZS_BLIND | 10 | 4.796 | 0.000 | 4.796 | 4.796 | 3.200 | 1.000 |
| snort | 1000.000 | GS_BLIND | 10 | 4.796 | 0.000 | 4.796 | 4.796 | 3.200 | 1.000 |
| snort | 1000.000 | SIG | 10 | 4.796 | 0.000 | 4.796 | 4.796 | 3.200 | 1.000 |
| snort | 1500.000 | ZS_BLIND | 10 | 3.111 | 0.000 | 3.111 | 3.111 | 3.300 | 1.000 |
| snort | 1500.000 | GS_BLIND | 10 | 3.111 | 0.000 | 3.111 | 3.111 | 3.000 | 1.000 |
| snort | 1500.000 | SIG | 10 | 3.111 | 0.000 | 3.111 | 3.111 | 3.000 | 1.000 |

### B2. Cross-evaluation: every final defender against the SAME attackers

Defender = final equilibrium defender mixture of each game (or a baseline). Attacker = final equilibrium attacker mixture of each game, or the fixed uniform attacker. Same evaluation episodes for all (common random numbers). "worst" = max over the attackers.

| dataset | budget | defender | ZS_BLIND_attacker | SIG_attacker | fixed_uniform | GS_BLIND_attacker | worst |
|---|---|---|---|---|---|---|---|
| fraud | 10.000 | ZS_BLIND | 255.240 | 254.128 | 197.122 |  | 255.376 |
| fraud | 10.000 | SIG | 254.105 | 253.146 | 198.101 |  | 254.285 |
| fraud | 10.000 | baseline_uniform | 271.424 | 270.096 | 229.750 |  | 271.447 |
| fraud | 10.000 | baseline_newest | 271.424 | 270.096 | 229.750 |  | 271.447 |
| fraud | 10.000 | baseline_proportion | 276.879 | 275.525 | 241.640 |  | 276.879 |
| fraud | 10.000 | baseline_fraud_rule | 270.922 | 269.466 | 234.159 |  | 270.922 |
| fraud | 10.000 | baseline_aics | 272.974 | 271.881 | 246.618 |  | 273.089 |
| fraud | 10.000 | baseline_icde | 272.974 | 271.881 | 246.618 |  | 273.089 |
| fraud | 10.000 | GS_BLIND |  |  |  |  |  |
| fraud | 10.000 | baseline_snort_rule |  |  |  |  |  |
| fraud | 10.000 | baseline_suricata_rule |  |  |  |  |  |
| fraud | 20.000 | ZS_BLIND | 224.096 | 225.455 | 180.760 |  | 226.251 |
| fraud | 20.000 | SIG | 218.199 | 220.065 | 174.297 |  | 220.823 |
| fraud | 20.000 | baseline_uniform | 236.291 | 236.691 | 196.967 |  | 237.429 |
| fraud | 20.000 | baseline_newest | 236.291 | 236.691 | 196.967 |  | 237.429 |
| fraud | 20.000 | baseline_proportion | 242.967 | 242.276 | 211.342 |  | 243.288 |
| fraud | 20.000 | baseline_fraud_rule | 227.534 | 227.220 | 194.526 |  | 228.013 |
| fraud | 20.000 | baseline_aics | 234.340 | 231.622 | 215.838 |  | 234.435 |
| fraud | 20.000 | baseline_icde | 237.888 | 235.816 | 216.548 |  | 238.036 |
| fraud | 20.000 | GS_BLIND |  |  |  |  |  |
| fraud | 20.000 | baseline_snort_rule |  |  |  |  |  |
| fraud | 20.000 | baseline_suricata_rule |  |  |  |  |  |
| fraud | 30.000 | ZS_BLIND | 187.790 | 187.990 | 155.983 |  | 189.570 |
| fraud | 30.000 | SIG | 185.246 | 184.834 | 156.756 |  | 186.565 |
| fraud | 30.000 | baseline_uniform | 204.088 | 203.786 | 165.351 |  | 205.927 |
| fraud | 30.000 | baseline_newest | 204.088 | 203.786 | 165.351 |  | 205.927 |
| fraud | 30.000 | baseline_proportion | 212.342 | 211.904 | 184.536 |  | 213.049 |
| fraud | 30.000 | baseline_fraud_rule | 186.642 | 186.107 | 157.033 |  | 187.671 |
| fraud | 30.000 | baseline_aics | 189.341 | 189.057 | 172.658 |  | 190.105 |
| fraud | 30.000 | baseline_icde | 206.419 | 206.472 | 193.422 |  | 207.318 |
| fraud | 30.000 | GS_BLIND |  |  |  |  |  |
| fraud | 30.000 | baseline_snort_rule |  |  |  |  |  |
| fraud | 30.000 | baseline_suricata_rule |  |  |  |  |  |
| suricata | 500.000 | ZS_BLIND | 38.474 | 40.095 | 88.302 |  | 88.302 |
| suricata | 500.000 | SIG | 40.381 | 38.229 | 86.173 |  | 86.173 |
| suricata | 500.000 | baseline_uniform | 56.314 | 55.811 | 94.380 |  | 94.380 |
| suricata | 500.000 | baseline_newest | 56.314 | 55.811 | 94.380 |  | 94.380 |
| suricata | 500.000 | baseline_proportion | 61.894 | 61.869 | 96.349 |  | 96.349 |
| suricata | 500.000 | baseline_fraud_rule |  |  |  |  |  |
| suricata | 500.000 | baseline_aics |  |  |  |  |  |
| suricata | 500.000 | baseline_icde |  |  |  |  |  |
| suricata | 500.000 | GS_BLIND |  |  |  |  |  |
| suricata | 500.000 | baseline_snort_rule |  |  |  |  |  |
| suricata | 500.000 | baseline_suricata_rule | 61.968 | 62.009 | 88.549 |  | 88.549 |
| suricata | 1000.000 | ZS_BLIND | 34.320 | 34.320 | 76.331 |  | 76.331 |
| suricata | 1000.000 | SIG | 34.615 | 34.615 | 70.217 |  | 70.217 |
| suricata | 1000.000 | baseline_uniform | 48.208 | 48.208 | 79.490 |  | 79.490 |
| suricata | 1000.000 | baseline_newest | 48.208 | 48.208 | 79.490 |  | 79.490 |
| suricata | 1000.000 | baseline_proportion | 56.391 | 56.391 | 82.549 |  | 82.549 |
| suricata | 1000.000 | baseline_fraud_rule |  |  |  |  |  |
| suricata | 1000.000 | baseline_aics |  |  |  |  |  |
| suricata | 1000.000 | baseline_icde |  |  |  |  |  |
| suricata | 1000.000 | GS_BLIND |  |  |  |  |  |
| suricata | 1000.000 | baseline_snort_rule |  |  |  |  |  |
| suricata | 1000.000 | baseline_suricata_rule | 56.650 | 56.650 | 76.844 |  | 76.844 |
| suricata | 1500.000 | ZS_BLIND | 33.293 | 32.965 | 68.052 |  | 68.052 |
| suricata | 1500.000 | SIG | 36.534 | 31.043 | 62.366 |  | 63.180 |
| suricata | 1500.000 | baseline_uniform | 42.246 | 41.795 | 69.908 |  | 69.908 |
| suricata | 1500.000 | baseline_newest | 42.246 | 41.795 | 69.908 |  | 69.908 |
| suricata | 1500.000 | baseline_proportion | 51.471 | 47.821 | 73.941 |  | 73.941 |
| suricata | 1500.000 | baseline_fraud_rule |  |  |  |  |  |
| suricata | 1500.000 | baseline_aics |  |  |  |  |  |
| suricata | 1500.000 | baseline_icde |  |  |  |  |  |
| suricata | 1500.000 | GS_BLIND |  |  |  |  |  |
| suricata | 1500.000 | baseline_snort_rule |  |  |  |  |  |
| suricata | 1500.000 | baseline_suricata_rule | 51.510 | 47.748 | 69.176 |  | 69.176 |
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
| fraud | 10.000 | SIG - ZS_BLIND | ZS_BLIND_attacker | 10 | -1.135 | -0.445 | 0.038 | 0.045 | 1.000 |
| fraud | 10.000 | SIG - ZS_BLIND | SIG_attacker | 10 | -0.981 | -0.386 | 0.086 | 0.060 | 1.000 |
| fraud | 10.000 | SIG - ZS_BLIND | fixed_uniform | 10 | 0.979 | 0.497 | 0.953 | 0.461 | 1.000 |
| fraud | 10.000 | SIG - ZS_BLIND | worst | 10 | -1.091 | -0.427 | 0.051 | 0.053 | 1.000 |
| fraud | 20.000 | SIG - ZS_BLIND | ZS_BLIND_attacker | 10 | -5.897 | -2.631 | 0.010 | 0.006 | 0.479 |
| fraud | 20.000 | SIG - ZS_BLIND | SIG_attacker | 10 | -5.389 | -2.390 | 0.014 | 0.008 | 0.643 |
| fraud | 20.000 | SIG - ZS_BLIND | fixed_uniform | 10 | -6.463 | -3.576 | 0.084 | 0.068 | 1.000 |
| fraud | 20.000 | SIG - ZS_BLIND | worst | 10 | -5.428 | -2.399 | 0.010 | 0.007 | 0.479 |
| fraud | 30.000 | SIG - ZS_BLIND | ZS_BLIND_attacker | 10 | -2.544 | -1.354 | 0.084 | 0.061 | 1.000 |
| fraud | 30.000 | SIG - ZS_BLIND | SIG_attacker | 10 | -3.156 | -1.679 | 0.064 | 0.040 | 1.000 |
| fraud | 30.000 | SIG - ZS_BLIND | fixed_uniform | 10 | 0.773 | 0.496 | 0.492 | 0.647 | 1.000 |
| fraud | 30.000 | SIG - ZS_BLIND | worst | 10 | -3.006 | -1.585 | 0.064 | 0.042 | 1.000 |
| suricata | 500.000 | SIG - ZS_BLIND | ZS_BLIND_attacker | 10 | 1.907 | 4.956 | 0.678 | 0.295 | 1.000 |
| suricata | 500.000 | SIG - ZS_BLIND | SIG_attacker | 10 | -1.866 | -4.653 | 0.515 | 0.391 | 1.000 |
| suricata | 500.000 | SIG - ZS_BLIND | fixed_uniform | 10 | -2.129 | -2.411 | 0.232 | 0.317 | 1.000 |
| suricata | 500.000 | SIG - ZS_BLIND | worst | 10 | -2.129 | -2.411 | 0.232 | 0.317 | 1.000 |
| suricata | 1000.000 | SIG - ZS_BLIND | ZS_BLIND_attacker | 10 | 0.295 | 0.859 | 0.322 | 0.176 | 1.000 |
| suricata | 1000.000 | SIG - ZS_BLIND | SIG_attacker | 10 | 0.295 | 0.859 | 0.322 | 0.176 | 1.000 |
| suricata | 1000.000 | SIG - ZS_BLIND | fixed_uniform | 10 | -6.114 | -8.010 | 0.160 | 0.136 | 1.000 |
| suricata | 1000.000 | SIG - ZS_BLIND | worst | 10 | -6.114 | -8.010 | 0.160 | 0.136 | 1.000 |
| suricata | 1500.000 | SIG - ZS_BLIND | ZS_BLIND_attacker | 10 | 3.240 | 9.732 | 0.064 | 0.217 | 1.000 |
| suricata | 1500.000 | SIG - ZS_BLIND | SIG_attacker | 10 | -1.922 | -5.831 | 0.432 | 0.510 | 1.000 |
| suricata | 1500.000 | SIG - ZS_BLIND | fixed_uniform | 10 | -5.686 | -8.356 | 0.275 | 0.325 | 1.000 |
| suricata | 1500.000 | SIG - ZS_BLIND | worst | 10 | -4.872 | -7.160 | 0.375 | 0.402 | 1.000 |
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
| snort | 1500.000 | SIG - ZS_BLIND | ZS_BLIND_attacker | 10 | 0.000 | 0.000 | nan | nan | nan |
| snort | 1500.000 | SIG - ZS_BLIND | SIG_attacker | 10 | 0.000 | 0.000 | nan | nan | nan |
| snort | 1500.000 | SIG - ZS_BLIND | fixed_uniform | 10 | 0.000 | 0.000 | nan | nan | nan |
| snort | 1500.000 | SIG - ZS_BLIND | GS_BLIND_attacker | 10 | 0.000 | 0.000 | nan | nan | nan |
| snort | 1500.000 | SIG - ZS_BLIND | worst | 10 | 0.000 | 0.000 | nan | nan | nan |
| snort | 1500.000 | SIG - GS_BLIND | ZS_BLIND_attacker | 10 | 0.000 | 0.000 | nan | nan | nan |
| snort | 1500.000 | SIG - GS_BLIND | SIG_attacker | 10 | 0.000 | 0.000 | nan | nan | nan |
| snort | 1500.000 | SIG - GS_BLIND | fixed_uniform | 10 | 0.000 | 0.000 | nan | nan | nan |
| snort | 1500.000 | SIG - GS_BLIND | GS_BLIND_attacker | 10 | 0.000 | 0.000 | nan | nan | nan |
| snort | 1500.000 | SIG - GS_BLIND | worst | 10 | 0.000 | 0.000 | nan | nan | nan |

## C. Belief diagnostics (signaling game, final equilibrium)

| dataset | budget | n (belief policy in support) | n (no belief policy in support) | |b_def - b_exactBayes| | off-path rate (def. conjecture) | off-path rate (exact) | final belief on true type |
|---|---|---|---|---|---|---|---|
| fraud | 10.000 | 10 | 0 | 0.072 | 0.000 | 0.000 | 0.731 |
| fraud | 20.000 | 10 | 0 | 0.070 | 0.000 | 0.000 | 0.739 |
| fraud | 30.000 | 10 | 0 | 0.021 | 0.000 | 0.000 | 0.747 |
| suricata | 500.000 | 10 | 0 | 0.000 | 0.000 | 0.000 | 0.717 |
| suricata | 1000.000 | 10 | 0 | 0.000 | 0.000 | 0.000 | 0.717 |
| suricata | 1500.000 | 10 | 0 | 0.000 | 0.000 | 0.000 | 0.745 |
| snort | 500.000 | 0 | 10 |  |  |  |  |
| snort | 1000.000 | 0 | 10 |  |  |  |  |
| snort | 1500.000 | 0 | 10 |  |  |  |  |

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

