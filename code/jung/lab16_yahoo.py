from pandas_datareader import data as pdr
from datetime import date
import yfinance as yf
yf.pdr_override()
import pandas as pd


tick_list = []

def find_ticker():
    while True:
        search = input("Type ticker symbol or 'exit': ")
        if search == "exit":
            break
        else:
            search.upper()
            tick_list.append(search)
    print(tick_list)


find_ticker()

today = date.today()

