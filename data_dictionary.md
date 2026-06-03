# Data Dictionary

## 01_fund_master.csv

| Column       | Type    | Description                          |
| ------------ | ------- | ------------------------------------ |
| amfi_code    | INTEGER | Unique mutual fund scheme identifier |
| fund_house   | TEXT    | Asset Management Company             |
| category     | TEXT    | Scheme category                      |
| sub_category | TEXT    | Scheme sub-category                  |

---

## 02_nav_history.csv

| Column    | Type    | Description       |
| --------- | ------- | ----------------- |
| amfi_code | INTEGER | Scheme identifier |
| date      | DATE    | NAV date          |
| nav       | REAL    | Net Asset Value   |

---

## 07_scheme_performance.csv

| Column            | Type | Description              |
| ----------------- | ---- | ------------------------ |
| return_1yr_pct    | REAL | One year return          |
| return_3yr_pct    | REAL | Three year return        |
| return_5yr_pct    | REAL | Five year return         |
| expense_ratio_pct | REAL | Expense ratio percentage |

---

## 08_investor_transactions.csv

| Column           | Type    | Description                |
| ---------------- | ------- | -------------------------- |
| investor_id      | INTEGER | Investor unique ID         |
| transaction_date | DATE    | Transaction date           |
| transaction_type | TEXT    | SIP, Lumpsum or Redemption |
| amount_inr       | REAL    | Transaction amount         |
| state            | TEXT    | Investor state             |
| city             | TEXT    | Investor city              |
| kyc_status       | TEXT    | Investor KYC status        |

Source: Bluestock Mutual Fund Analytics Dataset
