import yfinance as yf

def load_stock(symbol):

    try:
        df = yf.download(symbol, period="2y", progress=False)
        return df
    except:
        return None
