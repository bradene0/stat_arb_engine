import pandas as pd
from ..utils import zscore as _z

def spread_z(e: pd.Series, window: int) -> pd.Series:
    return _z(e, window)
