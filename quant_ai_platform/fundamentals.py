import yfinance as yf

def get_fundamental_score(symbol):

    try:

        stock = yf.Ticker(symbol)

        info = stock.info

        pe = info.get("trailingPE", 0)
        growth = info.get("earningsGrowth", 0)

        score = 0

        if pe and pe < 25:
            score += 1

        if growth and growth > 0:
            score += 1

        return score

    except:
        return 0
