import requests

def get_stock_universe():

    url = "https://financialmodelingprep.com/api/v3/stock/list"

    try:
        data = requests.get(url).json()

        tickers = []

        for item in data:

            symbol = item.get("symbol")

            if symbol and "." not in symbol:
                tickers.append(symbol)

        return tickers

    except:
        return []
