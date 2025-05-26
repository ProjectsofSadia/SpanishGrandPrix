import pandas as pd
def load_and_process(data_path):
    df = pd.read_csv(data_path)

    if "Position" not in df.columns:
        raise ValueError("The dataset must contain a 'Position' column.")

    df['Winner'] = df['Position'].apply(lambda x: 1 if x == 1 else 0)
    df.fillna(0, inplace=True)

    return df
def prepare_fastf1_data(csv_path):
    df = pd.read_csv(csv_path)

    df["LapTimeSeconds"] = pd.to_timedelta(df["LapTime"]).dt.total_seconds()
    df["CompoundCode"] = df["Compound"].astype("category").cat.codes
    df["TeamCode"] = df["Team"].astype("category").cat.codes
    df["DriverCode"] = df["Driver"].astype("category").cat.codes
    df["Winner"] = df["Position"].apply(lambda x: 1 if x == 1 else 0)
    if "DriverFullName" in df.columns:
        df["DriverFullName"] = df["DriverFullName"]
    else:
        df["DriverFullName"] = df["Driver"]

    features = df[["LapTimeSeconds", "CompoundCode", "TeamCode", "DriverCode"]]
    target = df["Winner"]

    return features, target, df[["DriverCode", "DriverFullName"]].drop_duplicates()
