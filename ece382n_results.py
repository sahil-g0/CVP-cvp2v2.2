import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Load  Excel data

df = pd.read_excel("ece382n_results.xlsx")

# Identify columns
ls_cols = ["ls_half", "ls_1", "ls_2", "ls_5", "ls_7", "ls_10"]
alu_cols = ["alu_50", "alu_100", "alu_500", "alu_1000", "alu_5000", "alu_10000"]

trace_names = df["trace"]
baseline = df["baseline"]

# Compute Δ = (threshold - baseline)

ls_delta = df[ls_cols].subtract(df["baseline"], axis=0)
alu_delta = df[alu_cols].subtract(df["baseline"], axis=0)

# LS combined plot
plt.figure(figsize=(10,6))
for idx, row in ls_delta.iterrows():
    trace = df.loc[idx, "trace"]
    plt.plot(ls_cols, row.values, marker='o', label=trace, linestyle='none')

plt.axhline(0, color='gray', linestyle='none')
plt.title("LS Predictor — Δ Correct Prediction (%) Across All Traces")
plt.xlabel("LS Threshold")
plt.ylabel("Δ Correct Prediction (%)")
plt.grid(True)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()


# ALU combined plot
plt.figure(figsize=(10,6))
for idx, row in alu_delta.iterrows():
    trace = df.loc[idx, "trace"]
    plt.plot(alu_cols, row.values, marker='o', label=trace, linestyle='none')

plt.axhline(0, color='gray', linestyle='none')
plt.title("ALU Predictor — Δ Correct Prediction (%) Across All Traces")
plt.xlabel("ALU Threshold")
plt.ylabel("Δ Correct Prediction (%)")
plt.grid(True)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
