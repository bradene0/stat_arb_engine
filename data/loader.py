import os
import pandas as pd

def load_price_csv(path: str, date_col: str="date", price_col: str="close"):
    df = pd.read_csv(path, parse_dates=[date_col])
    df = df[[date_col, price_col]].rename(columns={date_col:"date", price_col:"price"})
    df = df.sort_values("date").dropna()
    df = df.drop_duplicates("date").set_index("date")
    return df["price"]

def load_pair(data_dir: str, a: str, b: str, price_col="close"):
    pa = load_price_csv(os.path.join(data_dir, f"{a}.csv"), price_col=price_col)
    pb = load_price_csv(os.path.join(data_dir, f"{b}.csv"), price_col=price_col)
    j = pa.index.intersection(pb.index)
    return pa.loc[j], pb.loc[j]
