# Data Dictionary

## fact_nav

| Column | Description |
|----------|----------|
| amfi_code | Mutual Fund Code |
| date | NAV Date |
| nav | Net Asset Value |

## fact_transactions

| Column | Description |
|----------|----------|
| investor_id | Investor ID |
| transaction_date | Transaction Date |
| amount_inr | Investment Amount |
| state | State |
| gender | Gender |
| kyc_status | KYC Status |

## fact_performance

| Column | Description |
|----------|----------|
| scheme_name | Fund Name |
| return_1yr_pct | One Year Return |
| expense_ratio_pct | Expense Ratio |
| aum_crore | Assets Under Management |
| risk_grade | Risk Category |