import pandas as pd
import numpy as np
from ..signals.pairs import hedge_ratio, spread, coint_check
from ..signals.zscore import spread_z
from ..risk import position_sizer
from ..costs import turnover, costs
from ..utils import clip_leverage

class PairsBacktester:
    def __init__(self, cfg):
        self.cfg = cfg

    def _signals(self, x: pd.Series, y: pd.Series):
        beta = hedge_ratio(x, y, self.cfg.rolling_window)
        e = spread(y, x, beta)
        z = spread_z(e, self.cfg.z_window)
        sig = pd.Series(0.0, index=z.index)
        sig[z > self.cfg.entry_z] = -1.0
        sig[z < -self.cfg.entry_z] = 1.0
        sig[(z.abs() <= self.cfg.exit_z)] = 0.0
        sig = sig.replace(to_replace=0.0, method="ffill").fillna(0.0)
        return beta, e, z, sig

    def _weights(self, sig: pd.Series, x: pd.Series, y: pd.Series, beta: pd.Series):
        br = beta.reindex(sig.index).fillna(method="ffill").fillna(0.0)
        w_spread = position_sizer(sig, (y.pct_change()- (br*x).pct_change()), self.cfg.target_vol, self.cfg.vol_lookback)
        wy =  w_spread
        wx = -w_spread * br
        w = pd.concat({"x": wx, "y": wy}, axis=1).fillna(0.0)
        w = clip_leverage(w, self.cfg.max_leverage)
        return w

    def _pnl(self, w: pd.DataFrame, x: pd.Series, y: pd.Series):
        rx = x.pct_change().fillna(0.0)
        ry = y.pct_change().fillna(0.0)
        ret_gross = (w["x"].shift(1)*rx + w["y"].shift(1)*ry).fillna(0.0)
        tc = costs(turnover(w), self.cfg.cost_bps)
        ret_net = ret_gross - tc
        equity = (1 + ret_net).cumprod() * self.cfg.initial_capital
        return ret_net, equity, tc

    def run_pair(self, x: pd.Series, y: pd.Series):
        beta, e, z, sig = self._signals(x, y)
        w = self._weights(sig, x, y, beta)
        ret, eq, tc = self._pnl(w, x, y)
        info = coint_check(e)
        out = pd.concat({
            "x": x,
            "y": y,
            "beta": beta,
            "spread": e,
            "z": z,
            "signal": sig,
            "wx": w["x"],
            "wy": w["y"],
            "ret": ret,
            "tc": tc,
            "equity": eq
        }, axis=1)
        return out, info
