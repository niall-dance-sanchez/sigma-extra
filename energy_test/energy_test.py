import requests as req
import pandas as pd
from datetime import datetime, timedelta, timezone

BASE_ELEXON = "https://data.elexon.co.uk/bmrs/api/v1"

# Map interconnector codes to country names
INTERCONNECTOR_MAP = {
    "INTELEC": "Belgium (ElecLink)",
    "INTEW": "Ireland (East-West)",
    "INTFR": "France (IFA)",
    "INTIFA2": "France (IFA2)",
    "INTIRL": "Northern Ireland (Moyle)",
    "INTNED": "Netherlands (BritNed)",
    "INTNEM": "Belgium (Nemo Link)",
    "INTNSL": "Norway (North Sea Link)",
    "INTVKL": "Denmark (Viking Link)",
    "INTGRNL": "Ireland (Greenlink)"
}


def get_generation_by_type_summary() -> pd.DataFrame:
    """
    Fetch generation outturn summary (by fuel type, half-hourly).
    Flattens nested 'data' column and adds interconnector country mapping.
    """
    url = f"{BASE_ELEXON}/generation/outturn/summary?includeNegativeGeneration=true"
    resp = req.get(url)
    resp.raise_for_status()
    data = resp.json()

    # Extract main data
    if isinstance(data, dict) and "data" in data:
        records = data["data"]
    else:
        records = data

    df = pd.DataFrame(records)

    # Expand nested fuelType/generation list
    df = df.explode("data", ignore_index=True)
    df = pd.concat([df.drop(columns=["data"]),
                   df["data"].apply(pd.Series)], axis=1)

    # Add country column for interconnectors
    df["country"] = df["fuelType"].map(INTERCONNECTOR_MAP)

    return df


def get_utc_settlement_time() -> list[str]:
    """Get the settlement time in UTC"""

    end_time = datetime.now(timezone.utc)
    start_time = (end_time - timedelta(minutes=29))

    return [start_time.isoformat(), end_time.isoformat()]



def get_regional_carbon_intensity() -> int:
    pass


def get_national_energy_generation(start_time: str, end_time: str) -> int:
    
    url = f"https://api.carbonintensity.org.uk/generation/{start_time}/{end_time}"
    response = req.get(url)
    data = response.json()["data"][0]

    return data 

if __name__ == "__main__":

    # ELEXON

    # response = req.get("https://data.elexon.co.uk/bmrs/api/v1/generation/outturn/current")
    # data = response.json()
    # print(data)


    # response = req.get("https://data.elexon.co.uk/bmrs/api/v1/demand/outturn/summary")
    # data = response.json()
    # print(data)


    # response = req.get("https://data.elexon.co.uk/bmrs/api/v1/balancing/pricing/market-index?from=2025-09-13T00%3A00Z&to=2025-09-13T00%3A30Z&format=json")
    # data = response.json()
    # print(data)

    # NESO 
    from_time = "2025-10-01T14:01Z"
    to_time = "2025-10-01T14:30Z"
    # url = f"https://api.carbonintensity.org.uk/regional/intensity/{from_time}/{to_time}"
    # response = req.get(url)
    # data = response.json()["data"][0]

    # print(data["from"], data["to"])

    # regions = data["regions"]
    # for r in regions:
    #     print(r["regionid"], r["shortname"])
    #     # for g in r["generationmix"]:
    #     #     print(g)

    

    # url = f"https://api.carbonintensity.org.uk/generation/{from_time}/{to_time}"
    # response = req.get(url)
    # data = response.json()["data"][0]
    # print(data["from"], data["to"])
    # fuel_types = data["generationmix"]
    # for f in fuel_types:
    #     print(f)


    # pd.set_option("display.max_columns", None)
    # pd.set_option("display.width", None)

    # gen_df = get_generation_by_type_summary()
    # print(gen_df.head(20))
    # print("\nColumns:", gen_df.columns.tolist())

    # print(get_utc_settlement_time())

    
    print(type(get_national_energy_generation(from_time, to_time)))
    




        
