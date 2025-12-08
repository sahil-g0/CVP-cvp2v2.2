import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gmean

# Load  Excel data

df = pd.read_excel("ece382n_results_alu2_1.xlsx")

# Identify columns
alu_cols = ["alu_2","alu_5", "alu_10", "alu_25", "alu_50", "alu_100", "alu_250"]

trace_names = df["trace"]
baseline = df["baseline"]

# Compute Δ = (threshold - baseline)

alu_delta = df[alu_cols].subtract(df["baseline"], axis=0)

# ALU combined plot
plt.figure(figsize=(10,6))
for idx, row in alu_delta.iterrows():
    trace = df.loc[idx, "trace"]
    plt.plot(alu_cols, row.values, marker='o', label=trace)

plt.axhline(0, color='gray', linestyle='none')
plt.title("ALU Heuristic — Δ Prediction Accuracy (%) Across All Traces")
plt.xlabel("ALU Threshold")
plt.ylabel("Δ Prediction Accuracy (%)")
plt.grid(True)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

alu_mean = alu_delta.mean(axis=0)

# Plot ALU summary
plt.figure(figsize=(8,5))
plt.plot(alu_cols, alu_mean, marker='o')
plt.title("ALU Heuristic — Mean Δ Prediction Accuracy (%) Over Baseline")
plt.ylabel("Δ Prediction Accuracy (%)")
plt.xlabel("Threshold")
plt.grid(True)
plt.tight_layout()
plt.show()
