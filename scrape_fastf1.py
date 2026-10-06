import os
import fastf1
import pandas as pd
os.makedirs("cache", exist_ok=True)
os.makedirs("data", exist_ok=True)
fastf1.Cache.enable_cache("cache")
session = fastf1.get_session(2023, "Spanish Grand Prix", "R")
session.load()
laps = session.laps.pick_quicklaps().copy()
laps["DriverFullName"] = laps["Driver"].apply(lambda code: session.get_driver(code)["FullName"])
df = laps[["Driver", "DriverFullName", "Team", "LapTime", "Compound", "TrackStatus", "Position"]].dropna().copy()
df["LapTimeSeconds"] = df["LapTime"].dt.total_seconds()
df.to_csv("data/spanish_fastf1_real.csv", index=False)
podium = df.groupby("DriverFullName")["LapTimeSeconds"].min().nsmallest(3).reset_index()
podium.to_csv("data/predicted_podium.csv", index=False)
print("✅ Saved data with driver names!")



