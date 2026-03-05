import os
import sys

# Add current folder to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

from scanner import analyze_stock
from sentiment import get_sentiment
from probability import profit_probability
from portfolio import build_portfolio
from stock_universe import get_stock_universe

from streamlit_autorefresh import st_autorefresh


# -------------------------------
# Refresh settings
# -------------------------------

REFRESH_TIME = 60

count = st_autorefresh(interval=REFRESH_TIME * 1000, key="refresh")

seconds_left = REFRESH_TIME - (count % REFRESH_TIME)


# -------------------------------
# Page setup
# -------------------------------

st.set_page_config(
    page_title="AI Trading Dashboard",
    layout="wide"
)

st.title("AI Trading Dashboard")

st.info(f"Next refresh in: {seconds_left} seconds")


# -------------------------------
# Stock scanner
# -------------------------------

st.header("Top AI Opportunities")

stocks = get_stock_universe()[:80]

results = []

for ticker in stocks:

    r = analyze_stock(ticker)

    if r:

        sentiment = get_sentiment()

        prob = profit_probability(r["score"])

        results.append({
            "ticker": r["ticker"],
            "score": r["score"],
            "patterns": r["patterns"],
            "sentiment": sentiment,
            "profit_probability": f"{int(prob * 100)}%"
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

else:

    st.warning("No signals found")


# -------------------------------
# Chart viewer
# -------------------------------

st.header("Stock Chart Viewer")

ticker_input = st.text_input("Enter stock symbol")

if ticker_input:

    data = yf.download(ticker_input)

    fig = go.Figure(data=[go.Candlestick(
        x=data.index,
        open=data["Open"],
        high=data["High"],
        low=data["Low"],
        close=data["Close"]
    )])

    st.plotly_chart(fig, use_container_width=True)




