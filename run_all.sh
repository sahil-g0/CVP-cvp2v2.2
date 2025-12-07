#!/bin/bash

OUTDIR="results/alu/int"

# Predictor binaries and corresponding threshold names
BINS=(
  cvp_alu_50
  cvp_alu_100
  cvp_alu_500
  cvp_alu_1000
  cvp_alu_5000
  cvp_alu_10000
)

THRESHOLDS=(
  50
  100
  500
  1000
  5000
  10000
)

# Traces to evaluate
TRACES=(
  int_0_trace.gz
  int_1_trace.gz
  int_6_trace.gz
  int_8_trace.gz
  int_9_trace.gz
  int_13_trace.gz
  int_18_trace.gz
  int_21_trace.gz
  int_27_trace.gz
  int_35_trace.gz
)

mkdir -p "$OUTDIR"

for trace in "${TRACES[@]}"; do
  # Extract trace number: X from int_X_trace.gz
  num=$(echo "$trace" | grep -oP '(?<=int_)\d+(?=_trace)')

  # Matching addr file
  addr_file="alu_pc_int_${num}.txt"

  for i in "${!BINS[@]}"; do
    bin="${BINS[$i]}"
    thr="${THRESHOLDS[$i]}"

    outfile="$OUTDIR/int_${num}_trace_alu_${thr}.txt"

    echo "Running $bin with $addr_file on $trace → $outfile"

    "./$bin" -v -alu "$addr_file" "$trace" > "$outfile"
  done
done
# chmod +x run_all.sh
echo "All runs complete."
