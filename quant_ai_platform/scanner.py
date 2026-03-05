from data_engine import load_stock
from features import build_features
from pattern_probability import pattern_probability
import patterns

from fundamentals import get_fundamental_score


def analyze_stock(symbol):

    df = load_stock(symbol)

    if df is None or len(df) < 100:
        return None

    df = build_features(df)

    detected = []

    if patterns.double_bottom(df):
        detected.append("double_bottom")

    if patterns.cup_handle(df):
        detected.append("cup_handle")

    pattern_score = pattern_probability(detected)

    fundamental_score = get_fundamental_score(symbol)

total_score = pattern_score + fundamental_score

    return {
        "ticker": symbol,
        "score": total_score,
        "patterns": detected
    }

