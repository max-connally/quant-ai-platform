import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go

from scanner import analyze_stock
from streamlit_autorefresh import st_autorefresh

# Auto refresh every 60 seconds
st_autorefresh(interval=60000, key="refresh")

st.title("AI Trading Dashboard")

# -----------------------------------
# STOCK SCANNER
# -----------------------------------

st.header("Top AI Stock Opportunities")

watchlist = [
"AAPL","MSFT","NVDA","META","TSLA",
"AMD","AMZN","GOOGL","NFLX","INTC"
]

results = []

for stock in watchlist:

    r = analyze_stock(stock)

    if r:
        results.append(r)

df = pd.DataFrame(results)

if not df.empty:

    df = df.sort_values("score", ascending=False)

    # create trading signal
    df["signal"] = df["score"].apply(
        lambda x: "BUY" if x > 1 else "WATCH"
    )

    st.dataframe(df)

else:
    st.write("No signals found")

# -----------------------------------
# STOCK CHART
# -----------------------------------

st.header("Stock Chart Viewer")

ticker = st.text_input("Enter stock symbol")

if ticker:

    data = yf.download(ticker)

    fig = go.Figure(data=[go.Candlestick(
        x=data.index,
        open=data["Open"],
        high=data["High"],
        low=data["Low"],
        close=data["Close"]
    )])

    st.plotly_chart(fig)
