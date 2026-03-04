from scanner import analyze_stock
from portfolio import rank_stocks
from config import WATCHLIST_FILE

watchlist = open(WATCHLIST_FILE).read().splitlines()

results = []

for s in watchlist:

    r = analyze_stock(s)

    if r:
        results.append(r)

portfolio = rank_stocks(results)

print("Top signals:")

for p in portfolio:

    print(p)
