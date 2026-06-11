"""
Data Cleaning Module

Purpose:
Fetch mutual fund data and save it for processing.

Author:
Karthikeya Bammidi
"""
import pandas as pd

print("Starting Data Cleaning...")

# ==========================================
# 01 FUND MASTER
# ==========================================

fund = pd.read_csv("data/raw/01_fund_master.csv")

fund = fund.drop_duplicates()

fund['launch_date'] = pd.to_datetime(
    fund['launch_date'],
    errors='coerce'
)

fund.to_csv(
    "data/processed/clean_fund_master.csv",
    index=False
)

print("clean_fund_master.csv created")

# ==========================================
# 02 NAV HISTORY
# ==========================================

nav = pd.read_csv(
    "data/raw/02_nav_history.csv"
)

nav['date'] = pd.to_datetime(
    nav['date'],
    errors='coerce'
)

nav = nav.sort_values(
    ['amfi_code','date']
)

nav['nav'] = (
    nav.groupby('amfi_code')['nav']
       .ffill()
)

nav = nav.drop_duplicates()

nav = nav[
    nav['nav'] > 0
]

nav.to_csv(
    "data/processed/clean_nav_history.csv",
    index=False
)

print("clean_nav_history.csv created")

# ==========================================
# 03 AUM BY FUND HOUSE
# ==========================================

aum = pd.read_csv(
    "data/raw/03_aum_by_fund_house.csv"
)

aum['date'] = pd.to_datetime(
    aum['date'],
    errors='coerce'
)

aum = aum.drop_duplicates()

aum.to_csv(
    "data/processed/clean_aum_by_fund_house.csv",
    index=False
)

print("clean_aum_by_fund_house.csv created")

# ==========================================
# 04 MONTHLY SIP INFLOWS
# ==========================================

sip = pd.read_csv(
    "data/raw/04_monthly_sip_inflows.csv"
)

sip = sip.drop_duplicates()

sip.to_csv(
    "data/processed/clean_monthly_sip_inflows.csv",
    index=False
)

print("clean_monthly_sip_inflows.csv created")

# ==========================================
# 05 CATEGORY INFLOWS
# ==========================================

cat = pd.read_csv(
    "data/raw/05_category_inflows.csv"
)

cat = cat.drop_duplicates()

cat.to_csv(
    "data/processed/clean_category_inflows.csv",
    index=False
)

print("clean_category_inflows.csv created")

# ==========================================
# 06 INDUSTRY FOLIO COUNT
# ==========================================

folio = pd.read_csv(
    "data/raw/06_industry_folio_count.csv"
)

folio = folio.drop_duplicates()

folio.to_csv(
    "data/processed/clean_industry_folio_count.csv",
    index=False
)

print("clean_industry_folio_count.csv created")

# ==========================================
# 07 SCHEME PERFORMANCE
# ==========================================

perf = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

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

perf['return_anomaly_flag'] = (
    perf[return_cols]
    .isna()
    .any(axis=1)
)

perf['expense_ratio_pct'] = pd.to_numeric(
    perf['expense_ratio_pct'],
    errors='coerce'
)

perf['expense_ratio_flag'] = (
    (perf['expense_ratio_pct'] < 0.1)
    |
    (perf['expense_ratio_pct'] > 2.5)
)

perf = perf.drop_duplicates()

perf.to_csv(
    "data/processed/clean_scheme_performance.csv",
    index=False
)

print("clean_scheme_performance.csv created")

# ==========================================
# 08 INVESTOR TRANSACTIONS
# ==========================================

txn = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

txn['transaction_date'] = pd.to_datetime(
    txn['transaction_date'],
    errors='coerce'
)

txn['amount_inr'] = pd.to_numeric(
    txn['amount_inr'],
    errors='coerce'
)

txn = txn[
    txn['amount_inr'] > 0
]

txn = txn.drop_duplicates()

txn.to_csv(
    "data/processed/clean_investor_transactions.csv",
    index=False
)

print("clean_investor_transactions.csv created")

# ==========================================
# 09 PORTFOLIO HOLDINGS
# ==========================================

holdings = pd.read_csv(
    "data/raw/09_portfolio_holdings.csv"
)

holdings['portfolio_date'] = pd.to_datetime(
    holdings['portfolio_date'],
    errors='coerce'
)

holdings = holdings.drop_duplicates()

holdings.to_csv(
    "data/processed/clean_portfolio_holdings.csv",
    index=False
)

print("clean_portfolio_holdings.csv created")

# ==========================================
# 10 BENCHMARK INDICES
# ==========================================

bench = pd.read_csv(
    "data/raw/10_benchmark_indices.csv"
)

bench = bench.drop_duplicates()

bench.to_csv(
    "data/processed/clean_benchmark_indices.csv",
    index=False
)

print("clean_benchmark_indices.csv created")

print("\nALL 10 CLEAN FILES CREATED SUCCESSFULLY!")