#!/bin/bash
# Reproduce the signaling-game experiments.
#   ./run_signaling.sh toy    -> minutes, checks the whole pipeline
#   ./run_signaling.sh full   -> the paper results (about half a day on 8 cores)
# Outputs: runs/<toy|full>/ (raw per-job JSON/CSV/logs) and results/<toy|full>/ (tables + figures)
set -e
MODE=${1:-toy}
cd "$(dirname "$0")/src"
export IDS_CONFIG=signaling_${MODE}.conf
PY=../venv/bin/python
$PY -m unittest test_signaling_belief
$PY -u signaling_do.py sensitivity
$PY -u signaling_do.py main
$PY -u signaling_analysis.py ${MODE}
