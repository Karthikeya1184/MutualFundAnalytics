-- ====================================
-- 1. TOP 5 FUNDS BY AUM
-- ====================================

SELECT *
FROM fact_aum
ORDER BY aum DESC
LIMIT 5;

-- ====================================
-- 2. AVERAGE NAV PER MONTH
-- ====================================

SELECT
strftime('%Y-%m', date) AS month,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month
ORDER BY month;

-- ====================================
-- 3. SIP TRANSACTIONS
-- ====================================

SELECT
COUNT(*) AS sip_count
FROM fact_transactions
WHERE transaction_type='SIP';

-- ====================================
-- 4. TRANSACTIONS BY STATE
-- ====================================

SELECT
state,
COUNT(*) AS total_txns
FROM fact_transactions
GROUP BY state
ORDER BY total_txns DESC;

-- ====================================
-- 5. LOW EXPENSE RATIO FUNDS
-- ====================================

SELECT *
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- ====================================
-- 6. BEST 5-YEAR RETURNS
-- ====================================

SELECT *
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;

-- ====================================
-- 7. BEST 3-YEAR RETURNS
-- ====================================

SELECT *
FROM fact_performance
ORDER BY return_3yr_pct DESC
LIMIT 10;

-- ====================================
-- 8. HIGHEST NAV
-- ====================================

SELECT *
FROM fact_nav
ORDER BY nav DESC
LIMIT 10;

-- ====================================
-- 9. REDEMPTION ANALYSIS
-- ====================================

SELECT
SUM(amount_inr)
FROM fact_transactions
WHERE transaction_type='Redemption';

-- ====================================
-- 10. AVERAGE RETURN
-- ====================================

SELECT
AVG(return_1yr_pct),
AVG(return_3yr_pct),
AVG(return_5yr_pct)
FROM fact_performance;