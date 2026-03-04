import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

st.title("AI Trading Dashboard")

ticker = st.text_input("Enter Stock Symbol")

if ticker:

    df = yf.download(ticker)

    fig = go.Figure(data=[go.Candlestick(
        x=df.index,
        open=df["Open"],
        high=df["High"],
        low=df["Low"],
        close=df["Close"]
    )])

    st.plotly_chart(fig)
