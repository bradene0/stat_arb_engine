import pandas as pd

def summary(df: pd.DataFrame) -> dict:
    r = df["ret"].dropna()
    ann = r.mean()*252
    vol = r.std()* (252**0.5)
    sharpe = ann/vol if vol>0 else float("nan")
    mdd = (df["equity"]/df["equity"].cummax() - 1).min()
    tcost = df["tc"].sum()
    return {"ann_ret": float(ann), "ann_vol": float(vol), "sharpe": float(sharpe), "max_dd": float(mdd), "tot_cost": float(tcost)}
