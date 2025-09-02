import numpy as np
import pandas as pd
from statsmodels.tsa.stattools import adfuller
from ..utils import rolling_beta

def hedge_ratio(x: pd.Series, y: pd.Series, window: int) -> pd.Series:
    b = rolling_beta(x, y, window)
    return b

def spread(y: pd.Series, x: pd.Series, beta: pd.Series) -> pd.Series:
    beta = beta.reindex(y.index).fillna(method="ffill")
    return y - beta * x

def coint_check(e: pd.Series) -> dict:
    e = e.dropna()
    if len(e) < 25:
        return {"adf_p": np.nan, "stationary": False}
    res = adfuller(e, maxlag=1, autolag="AIC")
    p = res[1]
    return {"adf_p": float(p), "stationary": bool(p < 0.05)}
