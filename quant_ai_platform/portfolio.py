def build_portfolio(df):

    if df.empty:
        return "No portfolio suggestions available."

    top = df.sort_values("score", ascending=False).head(5)

    portfolio = []

    for _, row in top.iterrows():

        portfolio.append({
            "ticker": row["ticker"],
            "allocation": "20%"
        })

    return portfolio
