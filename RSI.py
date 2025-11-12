import yfinance as yf
import pandas as pd
import numpy as np
import quantstats as qs

# config
TICKER = "TCS.NS"  # Tata Consultancy Services
BENCHMARK = "^NSEI"  # NIFTY 50
START_DATE = "2020-01-01"
END_DATE = "2025-11-12"
RSI_PERIOD = 14
OVERSOLD_LEVEL = 30  # Buy signal threshold
OVERBOUGHT_LEVEL = 70  # Sell signal threshold
INITIAL_CAPITAL = 100000

# fetch
print(f"Fetching data for {TICKER}...")
data = yf.download(TICKER, start=START_DATE, end=END_DATE, progress=False)
benchmark = yf.download(BENCHMARK, start=START_DATE, end=END_DATE, progress=False)

# calculate RSI
def calculate_rsi(data, period=14):
    """Calculate Relative Strength Index"""
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

data['RSI'] = calculate_rsi(data, RSI_PERIOD)

# generate signals
data['Signal'] = 0
data['Position'] = 0

for i in range(1, len(data)):
    # buy signal: RSI crosses below oversold level
    if data['RSI'].iloc[i-1] > OVERSOLD_LEVEL and data['RSI'].iloc[i] <= OVERSOLD_LEVEL:
        data.loc[data.index[i], 'Signal'] = 1  # Buy

    # sell signal: RSI crosses above overbought level
    elif data['RSI'].iloc[i-1] < OVERBOUGHT_LEVEL and data['RSI'].iloc[i] >= OVERBOUGHT_LEVEL:
        data.loc[data.index[i], 'Signal'] = -1  # Sell

# track positions (1 = long, 0 = flat)
position = 0
for i in range(len(data)):
    if data['Signal'].iloc[i] == 1:
        position = 1
    elif data['Signal'].iloc[i] == -1:
        position = 0
    data.loc[data.index[i], 'Position'] = position

# calculate returns
data['Returns'] = data['Close'].pct_change()
data['Strategy_Returns'] = data['Position'].shift(1) * data['Returns']

# Remove NaN values
data = data.dropna()

# QuantStats
strategy_returns = data['Strategy_Returns']
benchmark_returns = benchmark['Close'].pct_change().dropna()

# align dates
strategy_returns, benchmark_returns = strategy_returns.align(benchmark_returns, join='inner')

# report
print("\n Generating QuantStats Report...")
qs.reports.html(
    strategy_returns,
    benchmark=benchmark_returns,
    output='tcs_rsi_report.html',
    title='RSI Mean Reversion Strategy - TCS'
)

print("\n Report generated: tcs_rsi_report.html")
print(f"\n Strategy Statistics:")
print(f"Total Return: {(strategy_returns + 1).prod() - 1:.2%}")
print(f"Sharpe Ratio: {qs.stats.sharpe(strategy_returns):.2f}")
print(f"Max Drawdown: {qs.stats.max_drawdown(strategy_returns):.2%}")
print(f"Win Rate: {qs.stats.win_rate(strategy_returns):.2%}")
