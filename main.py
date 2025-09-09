import yfinance as yf
from backtesting import Backtest
from strategies.sma_crossover import SmaCross

def run_backtest(symbol="AAPL", start="2018-01-01", end="2024-01-01", cash=10000):
    df = yf.download(symbol, start=start, end=end)
    df = df.dropna()

    bt = Backtest(df, SmaCross, cash=cash, commission=0.001)
    stats = bt.run()
    print(stats)
    bt.plot()

if __name__ == "__main__":
    run_backtest("AAPL")
