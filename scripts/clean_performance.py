import pandas as pd

df = pd.read_csv(
    "data/raw/07_scheme_performance (1).csv"
)

# expense ratio range
df = df[
    (df["expense_ratio_pct"] >= 0.1)
    &
    (df["expense_ratio_pct"] <= 2.5)
]

# remove duplicates
df = df.drop_duplicates()

df.to_csv(
    "data/processed/scheme_performance_clean.csv",
    index=False
)

print(df.shape)
print("Performance Cleaned")