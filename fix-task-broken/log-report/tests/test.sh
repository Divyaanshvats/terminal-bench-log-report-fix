#!/bin/bash

mkdir -p /logs/verifier

if pytest /tests/test_outputs.py \
    --json-report \
    --json-report-file=/logs/verifier/ctrf.json; then
    echo 1 > /logs/verifier/reward.txt
else
    echo 0 > /logs/verifier/reward.txt
fi