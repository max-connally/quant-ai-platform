import yfinance as yf
from features import build_features
import patterns


def analyze_stock(ticker):

    try:
        df = yf.download(ticker, period="1y")

        if df.empty:
            return None

        df = build_features(df)

        pattern_list = []
        pattern_score = 0

        if patterns.double_bottom(df):
            pattern_list.append("double_bottom")
            pattern_score += 0.5

        if patterns.head_shoulders(df):
            pattern_list.append("head_shoulders")
            pattern_score += 0.5

        if patterns.cup_handle(df):
            pattern_list.append("cup_handle")
            pattern_score += 0.5

        score = pattern_score

        return {
            "ticker": ticker,
            "score": score,
            "patterns": pattern_list
        }

    except:
        return None
