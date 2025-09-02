import numpy as np
import pandas as pd

def volatility_target(position_spread_ret: pd.Series, target_vol: float, lookback: int) -> pd.Series:
    vol = position_spread_ret.rolling(lookback).std().fillna(0.0)
    scale = (target_vol / (vol.replace(0, np.nan))).clip(upper=10.0)
    return scale.fillna(0.0)

def position_sizer(signals: pd.Series, spread_ret: pd.Series, target_vol: float, lookback: int) -> pd.Series:
    raw = signals.shift(1).fillna(0.0)
    scaled = raw * volatility_target(spread_ret * raw, target_vol, lookback)
    return scaled.clip(-1.0, 1.0)
