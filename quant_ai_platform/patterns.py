import numpy as np

def double_bottom(df):

    closes = df["Close"].tail(30)

    if len(closes) < 30:
        return False

    last_price = float(closes.iloc[-1])
    min_price = float(closes.min())
    mean_price = float(closes.mean())

    return abs(last_price - min_price) < mean_price * 0.01


def double_top(df):

    closes = df["Close"].tail(30)

    if len(closes) < 30:
        return False

    last_price = float(closes.iloc[-1])
    max_price = float(closes.max())
    mean_price = float(closes.mean())

    return abs(last_price - max_price) < mean_price * 0.01


def head_shoulders(df):

    prices = df["Close"].tail(50)

    if len(prices) < 50:
        return False

    left = float(prices.iloc[10])
    head = float(prices.iloc[25])
    right = float(prices.iloc[40])

    return head > left and head > right


def cup_handle(df):

    prices = df["Close"].tail(60)

    if len(prices) < 60:
        return False

    last_price = float(prices.iloc[-1])
    mean_price = float(prices.mean())

    return last_price > mean_price
