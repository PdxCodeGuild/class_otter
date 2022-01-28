import pandas as pd

aapl.to_csv("data/aapl_ohlc.csv")
df = pd.read_csv("data/aapl_ohlc.csv", header = 0, index_col = 'Date', parse_dates=True)