import requests
import pandas as pd
from pathlib import Path

schemes = {
    "SBI_Bluechip": "119551",
    "ICICI_Bluechip": "120503",
    "Nippon_Large_Cap": "118632",
    "Axis_Bluechip": "119092",
    "Kotak_Bluechip": "120841"
}

save_path = Path("data/raw")

for name, code in schemes.items():

    print(f"Fetching {name}")

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    data = response.json()

    nav_df = pd.DataFrame(data["data"])

    nav_df.to_csv(
        save_path / f"{name}.csv",
        index=False
    )

    print(f"{name} saved successfully")