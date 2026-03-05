import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go

from quant_ai_platform.scanner import analyze_stock
from quant_ai_platform.sentiment import get_sentiment
from quant_ai_platform.probability import profit_probability
from quant_ai_platform.portfolio import build_portfolio
from quant_ai_platform.stock_universe import get_stock_universe

from streamlit_autorefresh import st_autorefresh

REFRESH_TIME = 60

count = st_autorefresh(interval=REFRESH_TIME*1000, key="refresh")

st.set_page_config(layout="wide")

st.title("AI Trading Dashboard")

seconds_left = REFRESH_TIME - (count % REFRESH_TIME)

st.info(f"Next refresh in: {seconds_left} seconds")

st.header("Top AI Opportunities")

stocks = get_stock_universe()[:80]

results = []

for s in stocks:

    r = analyze_stock(s)

    if r:

        sentiment = get_sentiment()

        prob = profit_probability(r["score"])

        results.append({
            "ticker": r["ticker"],
            "score": r["score"],
            "patterns": r["patterns"],
            "sentiment": sentiment,
            "profit_probability": f"{int(prob*100)}%"
        })

df = pd.DataFrame(results)

if not df.empty:

    df = df.sort_values("score", ascending=False)

    df["signal"] = df["score"].apply(
        lambda x: "BUY" if x > 1.4 else "WATCH"
    )

    st.dataframe(df.head(20), use_container_width=True)

    st.header("Suggested Portfolio")

    portfolio = build_portfolio(df)

    st.write(portfolio)

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

    st.plotly_chart(fig, use_container_width=True)


