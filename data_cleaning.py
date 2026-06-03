import pandas as pd

# ==========================
# LOAD FILE
# ==========================

perf = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

print("Original Shape:")
print(perf.shape)

# ==========================
# CONVERT RETURNS TO NUMERIC
# ==========================

return_cols = [
    'return_1yr_pct',
    'return_3yr_pct',
    'return_5yr_pct'
]

for col in return_cols:

    perf[col] = pd.to_numeric(
        perf[col],
        errors='coerce'
    )

# ==========================
# FLAG RETURN ANOMALIES
# ==========================

perf['return_anomaly_flag'] = (
    perf[return_cols]
    .isna()
    .any(axis=1)
)

# ==========================
# CLEAN EXPENSE RATIO
# ==========================

perf['expense_ratio_pct'] = pd.to_numeric(
    perf['expense_ratio_pct'],
    errors='coerce'
)

perf['expense_ratio_flag'] = (
    (perf['expense_ratio_pct'] < 0.1)
    |
    (perf['expense_ratio_pct'] > 2.5)
)

# ==========================
# REMOVE DUPLICATES
# ==========================

perf = perf.drop_duplicates()

print("\nAnomaly Count:")
print(
    perf['return_anomaly_flag']
    .sum()
)

print("\nExpense Ratio Issues:")
print(
    perf['expense_ratio_flag']
    .sum()
)

print("\nCleaned Shape:")
print(perf.shape)

# ==========================
# SAVE FILE
# ==========================

perf.to_csv(
    "data/processed/clean_scheme_performance.csv",
    index=False
)

print("\nFile Saved Successfully!")