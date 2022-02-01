from symtable import Symbol
import numpy as np
import pandas as pd
import requests
import xlsxwriter
import math
from secret import IEX_CLOUD_API_TOKEN
import pprint


stocks = pd.read_csv("sp_500_stocks.csv")
# print(stocks)


symbol = "AAPL"
api_url = f"https://sandbox.iexapis.com/stable/stock/{symbol}/quote/?token={IEX_CLOUD_API_TOKEN}"
# print(api_url)
data = requests.get(api_url).json()
# pprint.pprint(data)

price = data["latestPrice"]
market_cap = data["marketCap"]

my_col = ["Tickers", "Stock Price", "Market Cap", "Number of Shares to Buy"]
final_dataframe = pd.DataFrame(columns = my_col)

# print(final_dataframe)

final_dataframe.append(
    pd.Series(
        [
            symbol,
            price,
            market_cap,
            "N/A"
        ],
    index = my_col
    ),
    ignore_index=True
)

# print(final_dataframe)

final_dataframe = pd.DataFrame(columns = my_col)
for stock in stocks["Ticker"]:
    api_url = f"https://sandbox.iexapis.com/stable/stock/{stock}/quote/?token={IEX_CLOUD_API_TOKEN}"
    data = requests.get(api_url).json()
    final_dataframe = final_dataframe.append(
        pd.Series(
            [
                stock,
                data["latestPrice"],
                data["marketCap"],
                "N/A"
            ],
        index = my_col
        ),
    ignore_index = True
    )

# print(final_dataframe)

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i : i + n]

symbol_groups = list(chunks(stocks["Ticker"], 100))

symbol_strings = []
for i in range(0, len(symbol_groups)):
    symbol_strings.append(','.join(symbol_groups[i]))

final_dataframe = pd.DataFrame(columns= my_col)
for symbol_string in symbol_strings:
    bathc_api_call_url = f'https://sandbox.iexapis.com/stable/stock/market/batch?symbol={symbol_string}&types=quote&token={IEX_CLOUD_API_TOKEN}'


data = requests.get(bathc_api_call_url).json()
for symbol in symbol_string.split(", "):
    print(symbol)