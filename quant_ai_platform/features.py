import ta
import pandas as pd

def build_features(df):

    # Ensure columns are 1D
    close = df["Close"].squeeze()
    high = df["High"].squeeze()
    low = df["Low"].squeeze()

    df["RSI"] = ta.momentum.RSIIndicator(close).rsi()

    df["EMA20"] = ta.trend.EMAIndicator(close, 20).ema_indicator()

    df["EMA50"] = ta.trend.EMAIndicator(close, 50).ema_indicator()

    df["returns"] = close.pct_change()

    df = df.dropna()

    return df
