import requests
import pandas as pd

scheme_code = "125497"

print("Fetching Scheme Code:", scheme_code)

url = f"https://api.mfapi.in/mf/{scheme_code}"

response = requests.get(url)

print("Status Code:", response.status_code)

data = response.json()

print("\nMeta Data:")
print(data["meta"])

print("\nScheme Name:")
print(data["meta"]["scheme_name"])

nav_df = pd.DataFrame(data["data"])

print("\nTop 5 NAV Records:")
print(nav_df.head())

nav_df.to_csv(
    "data/raw/hdfc_top100_nav.csv",
    index=False
)

print("\nCSV Saved Successfully")