# 📈 Stat-Arb Engine

A modular Python backtesting engine for **pairs trading** using a statistical arbitrage strategy.  
The system identifies cointegrated asset pairs, calculates dynamic hedge ratios, and generates trading signals from the Z-score of their spread.  
It supports volatility targeting and transaction cost simulation for realistic performance evaluation.

---

## 🚀 Features
- **Dynamic Hedge Ratio**  
  Rolling OLS regression adapts hedge ratios to changing market conditions.  
- **Z-Score Signal Generation**  
  Standardized spread deviations trigger entry and exit signals.  
- **Configurable Parameters**  
  Adjust tickers, rolling windows, and thresholds in `config.py`.  
- **Volatility Targeting**  
  Scales positions for stable risk exposure.  
- **Transaction Costs**  
  Simple cost model to reflect real-world frictions.  
- **Modular Design**  
  Separate modules for data, signals, backtesting, and reporting.


---

## ⚙️ Installation
```bash
git clone https://github.com/yourname/stat_arb_engine.git
cd stat_arb_engine
pip install -r requirements.txt
---



