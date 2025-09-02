from dataclasses import dataclass

@dataclass
class Config:
    tickers: list[tuple[str, str]] = (("AAA","BBB"),)
    data_dir: str = "data"
    start: str = "2020-01-01"
    end: str = "2025-01-01"
    price_col: str = "close"
    rolling_window: int = 60
    z_window: int = 60
    entry_z: float = 2.0
    exit_z: float = 0.5
    target_vol: float = 0.10
    vol_lookback: int = 20
    cost_bps: float = 1.0
    initial_capital: float = 1_000_000.0
    max_leverage: float = 3.0
    frequency: str = "B"
    out_dir: str = "out"
