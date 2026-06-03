SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

SELECT AVG(return_1yr_pct)
FROM fact_performance;

SELECT scheme_name, morningstar_rating
FROM fact_performance
ORDER BY morningstar_rating DESC;

SELECT scheme_name, expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

SELECT COUNT(*)
FROM fact_transactions;

SELECT AVG(amount_inr)
FROM fact_transactions;

SELECT state, COUNT(*)
FROM fact_transactions
GROUP BY state;

SELECT gender, COUNT(*)
FROM fact_transactions
GROUP BY gender;

SELECT kyc_status, COUNT(*)
FROM fact_transactions
GROUP BY kyc_status;

SELECT scheme_name, risk_grade
FROM fact_performance
WHERE risk_grade='Very High';