def build_portfolio(df):

    df = df.sort_values("score", ascending=False)

    return df.head(5)["ticker"].tolist()
