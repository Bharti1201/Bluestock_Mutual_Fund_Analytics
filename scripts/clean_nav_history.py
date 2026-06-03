import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

# date format
df["date"] = pd.to_datetime(df["date"])

# sort
df = df.sort_values(
    by=["amfi_code", "date"]
)

# remove duplicates
df = df.drop_duplicates()

# NAV > 0
df = df[df["nav"] > 0]

# create folder
import os
os.makedirs("data/processed", exist_ok=True)

# save
df.to_csv(
    "data/processed/nav_history_clean.csv",
    index=False
)

print(df.shape)
print("NAV History Cleaned")