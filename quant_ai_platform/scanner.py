import yfinance as yf
import pandas as pd

from features import build_features
import patterns


def analyze_stock(ticker):

    try:

        data = yf.download(ticker, period="6mo")

        if data.empty:
            return None

        df = build_features(data)

        score = 1.0
        detected_patterns = []

        if patterns.double_bottom(df):
            score += 0.3
            detected_patterns.append("double_bottom")

        if patterns.cup_handle(df):
            score += 0.4
            detected_patterns.append("cup_handle")

        if patterns.head_shoulders(df):
            score += 0.2
            detected_patterns.append("head_shoulders")

        # NEW RULE (this helps produce signals)
        if score < 1.1:
            return None

        return {
            "ticker": ticker,
            "score": score,
            "patterns": detected_patterns
        }

    except Exception:
        return None
