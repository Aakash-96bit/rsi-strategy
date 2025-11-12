# RSI Mean Reversion Strategy – TCS

This project implements a **Relative Strength Index (RSI)** mean reversion strategy using Python. It uses 5-year data of Tata Consultancy Services (TCS.NS) from Yahoo Finance and evaluates performance using **QuantStats**.

## ⚠️ Disclaimer

This project was developed as part of my learning journey in quantitative trading and algorithmic research. Some portions of the code were assisted by AI tools (e.g., for syntax, debugging, and documentation), but all logic, structure, and validation were personally reviewed and tested.

This project is for educational and research purposes only. The results shown are based on historical simulations and do not represent real trading outcomes. Nothing here should be interpreted as investment advice or financial guidance.

## 📊 Overview

- **Stock:** TCS (Tata Consultancy Services)
- **Indicator:** RSI (Relative Strength Index)
- **RSI Period:** 14
- **Oversold Level:** 30 (Buy Signal)
- **Overbought Level:** 70 (Sell Signal)
- **Benchmark:** NIFTY 50 (^NSEI)
- **Output Report:** `tcs_rsi_report.html`

## 🎯 Why TCS?

TCS is ideal for RSI mean reversion strategies because:
- **Low Volatility:** Beta of 0.7-0.9 vs NIFTY, providing stable price movements
- **High Liquidity:** Large-cap IT stock with excellent daily trading volume
- **Mean Reversion Characteristics:** Less volatile stocks perform better with RSI strategies
- **Non-Commodity:** IT services stocks work better than commodity-related stocks for RSI

## 🎯 Strategy Logic

**Buy Signal:** When RSI crosses below 30 (oversold condition)
**Sell Signal:** When RSI crosses above 70 (overbought condition)

This is a mean reversion strategy that assumes prices will revert to the mean after extreme movements.

## 🧭 How to Run
```bash
pip install -r requirements.txt
python rsi_strategy_tcs.py
```
## 🔧 Customization

You can modify the following parameters in `rsi_strategy_tcs.py`:

- `TICKER`: Change to any NSE stock (e.g., "HDFCBANK.NS", "ASIANPAINT.NS")
- `RSI_PERIOD`: Adjust lookback period (default: 14)
- `OVERSOLD_LEVEL`: Buy threshold (default: 30)
- `OVERBOUGHT_LEVEL`: Sell threshold (default: 70)
- `START_DATE` and `END_DATE`: Adjust backtest period

## 📊 Metrics Calculated

- Total Return
- Sharpe Ratio
- Maximum Drawdown
- Win Rate
- CAGR
- Volatility
- And more via QuantStats HTML report

## 📚 About RSI on TCS

The RSI is particularly effective on TCS because:
- Low beta (0.7-0.9) provides smoother mean reversion patterns
- High liquidity ensures efficient trade execution
- IT sector stability reduces false signals
- Consistent trading volume supports reliable backtesting
