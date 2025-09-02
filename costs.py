import pandas as pd
import numpy as np

def turnover(weights: pd.DataFrame) -> pd.Series:
    dw = weights.diff().abs().sum(axis=1).fillna(0.0)
    return dw

def costs(turnover_series: pd.Series, cost_bps: float) -> pd.Series:
    return turnover_series * (cost_bps / 1e4)
