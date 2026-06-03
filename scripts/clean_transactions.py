import pandas as pd

df = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

# standardize transaction type
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

# amount > 0
df = df[df["amount_inr"] > 0]

# date format
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"]
)

# save
df.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)

print(df.shape)
print("Transactions Cleaned")