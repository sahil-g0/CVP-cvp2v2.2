#!/bin/bash

OUTDIR="results"

# Predictor binaries and corresponding threshold names
BINS=(
  cvp_ls_0half
  cvp_ls_1
  cvp_ls_2
  cvp_ls_5
  cvp_ls_7
  cvp_ls_10
)

THRESHOLDS=(
  0half
  1
  2
  5
  7
  10
)

# Traces to evaluate
TRACES=(
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
  addr_file="addrs_ls_${num}.txt"

  for i in "${!BINS[@]}"; do
    bin="${BINS[$i]}"
    thr="${THRESHOLDS[$i]}"

    outfile="$OUTDIR/int_${num}_trace_ls_${thr}.txt"

    echo "Running $bin with $addr_file on $trace → $outfile"

    "./$bin" -v -lsfile "$addr_file" "$trace" > "$outfile"
  done
done

echo "All runs complete."
