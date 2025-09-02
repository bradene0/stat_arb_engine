import pandas as pd
import numpy as np

def to_returns(px: pd.Series) -> pd.Series:
    return px.pct_change().replace([np.inf, -np.inf], np.nan)

def align(a: pd.Series, b: pd.Series) -> tuple[pd.Series, pd.Series]:
    j = a.index.intersection(b.index)
    return a.loc[j], b.loc[j]

def rolling_beta(x: pd.Series, y: pd.Series, window: int) -> pd.Series:
    cov = x.rolling(window).cov(y)
    var = x.rolling(window).var()
    beta = cov / var
    return beta

def zscore(s: pd.Series, window: int) -> pd.Series:
    m = s.rolling(window).mean()
    sd = s.rolling(window).std(ddof=0)
    return (s - m) / sd

def clip_leverage(weights: pd.DataFrame, max_leverage: float) -> pd.DataFrame:
    lev = weights.abs().sum(axis=1).replace(0, np.nan)
    scale = (max_leverage / lev).clip(upper=1.0).fillna(1.0)
    return weights.mul(scale, axis=0)
