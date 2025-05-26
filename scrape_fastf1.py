import fastf1
import pandas as pd
fastf1.Cache.enable_cache('cache')
session = fastf1.get_session(2023, 'Spanish Grand Prix', 'R')
session.load()

laps = session.laps.pick_quicklaps()
laps['DriverFullName'] = laps['Driver'].apply(lambda code: session.get_driver(code)['FullName'])
df["LapTimeSeconds"] = pd.to_timedelta(df["LapTime"]).dt.total_seconds()
df = laps[["Driver", "DriverFullName", "Team", "LapTime", "Compound", "TrackStatus", "Position"]].dropna()

df.to_csv("data/spanish_fastf1_real.csv", index=False)
df_sorted = df.sort_values("LapTimeSeconds")
podium = df_sorted[["DriverFullName", "LapTimeSeconds"]].drop_duplicates().head(3)
podium.to_csv("data/predicted_podium.csv", index=False)

print("✅ Saved data with driver names!")




