import requests

def get_stock_universe():

    url = "https://financialmodelingprep.com/api/v3/stock/list"

    try:
        data = requests.get(url).json()

        tickers = []

        for item in data:
            if item["type"] == "stock":
                tickers.append(item["symbol"])

        return tickers[:8000]

    except:
        return []
