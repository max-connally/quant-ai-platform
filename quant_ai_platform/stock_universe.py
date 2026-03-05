import yfinance as yf

def get_stock_universe():

    tickers = []

    # Major US tickers (example list)
    sp500 = [
        "AAPL","MSFT","AMZN","NVDA","META","GOOGL","TSLA","AMD","NFLX","INTC",
        "ORCL","CRM","ADBE","PYPL","CSCO","PEP","COST","AVGO","TXN","QCOM"
    ]

    tickers.extend(sp500)

    # simulate large universe
    for i in range(8000):
        tickers.append(f"STOCK{i}")

    return tickers
