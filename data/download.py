# data/download.py
import os
import argparse
import yfinance as yf
import pandas as pd

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
os.makedirs(DATA_DIR, exist_ok=True)

def cache_path(symbol, interval):
    safe = symbol.replace("/", "-").upper()
    return os.path.join(DATA_DIR, f"{safe}_{interval}.csv")

def download(symbol: str, start: str, end: str, interval: str = "1d") -> pd.DataFrame:
    df = yf.download(symbol, start=start, end=end, interval=interval, auto_adjust=True, progress=False)
    if df.empty:
        raise ValueError(f"No data fetched for {symbol}. Check symbol or dates.")
    df = df.dropna()
    return df

def get_data(symbol: str, start: str, end: str, interval: str = "1d", cache: bool = True) -> pd.DataFrame:
    path = cache_path(symbol, interval)
    if cache and os.path.exists(path):
        return pd.read_csv(path, parse_dates=True, index_col=0)
    df = download(symbol, start, end, interval)
    if cache:
        df.to_csv(path)
        print(f"[saved] {path}")
    return df

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--symbol", default="AAPL")
    ap.add_argument("--start", default="2018-01-01")
    ap.add_argument("--end",   default="2024-01-01")
    ap.add_argument("--interval", default="1d")
    args = ap.parse_args()
    _ = get_data(args.symbol, args.start, args.end, args.interval, cache=True)
    print("[ok] downloaded & cached")
