import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go

from scanner import analyze_stock

# Title
st.title("AI Trading Dashboard")

# ----------------------------
# STOCK SCANNER SECTION
# ----------------------------

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

    st.dataframe(df)
else:
    st.write("No signals found")

# ----------------------------
# STOCK CHART SECTION
# ----------------------------

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
