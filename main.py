import yfinance as yf
import pandas as pd
from backtesting import Backtest
from strategies.sma_crossover import SmaCross

def run_backtest(symbol="AAPL", start="2018-01-01", end="2024-01-01", cash=10000):
    df = yf.download(symbol, start=start, end=end)

    # MultiIndex hatane ke liye
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    df = df[['Open', 'High', 'Low', 'Close', 'Volume']]  # only required columns

    bt = Backtest(df, SmaCross, cash=cash, commission=0.001)
    stats = bt.run()
    print(stats)
    bt.plot()

if __name__ == "__main__":
    run_backtest("AAPL")
