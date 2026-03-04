def rank_stocks(stocks):

    ranked = sorted(stocks,key=lambda x:x["score"],reverse=True)

    return ranked[:5]
