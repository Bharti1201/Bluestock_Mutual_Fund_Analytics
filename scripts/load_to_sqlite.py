import pandas as pd
from sqlalchemy import create_engine

# SQLite Database
engine = create_engine("sqlite:///bluestock_mf.db")

# Load CSV Files
nav_df = pd.read_csv("data/processed/nav_history_clean.csv")

txn_df = pd.read_csv(
    "data/processed/investor_transactions_clean.csv"
)

perf_df = pd.read_csv(
    "data/processed/scheme_performance_clean.csv"
)

# Load into SQLite
nav_df.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

txn_df.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

perf_df.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

print("Database Loaded Successfully")