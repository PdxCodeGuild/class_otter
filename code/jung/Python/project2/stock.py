#%%
import numpy as np
import pandas as pd
from pandas_datareader import data as web
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
import mplfinance as mpf



def save_to_csv_from_yahoo(ticker, syear, smonth, sday, eyear, emonth, eday):
    start = dt.datetime(syear, smonth, sday)
    end = dt.datetime(eyear, emonth, eday)

    df = web.DataReader(ticker, "yahoo", start, end)

    df.to_csv("/Users/jung/Downloads/class_otter/code/jung/project2/" + ticker + ".csv")
    return df

print(save_to_csv_from_yahoo("AMZN", 2020, 1, 1, 2021, 1, 1))

def get_df_from_csv(ticker):
    try:
        df = pd.read_csv("/Users/jung/Downloads/class_otter/code/jung/project2/" + ticker + ".csv")
    except FileNotFoundError:
        print("File Doesn't Exist")
    else:
        return df

AMZN = get_df_from_csv("AMZN")

def add_daily_return_to_df(df, ticker):
    df["Daily Return"] = (df["Adj Close"] / df["Adj Close"].shift(1)) - 1
    df.to_csv("/Users/jung/Downloads/class_otter/code/jung/project2/" + ticker + ".csv")
    return df

print(add_daily_return_to_df(AMZN, "AMZN"))

def get_return_defined_time(df, syear, smonth, sday, eyear, emonth, eday):
    start = f"{syear}-{smonth}-{sday}"
    end = f"{eyear}-{emonth}-{eday}"
    df["Date"] = pd.to_datetime(df["Date"])
    mask = (df["Date"] >= start) & (df["Date"] <= end)
    daily_return = df.loc[mask]["Daily Return"].mean()
    df2 = df.loc[mask]
    days = df2.shape[0]
    return (days * daily_return)

total_return = get_return_defined_time(AMZN, 2020, 1, 1, 2021, 1, 1)
print(f"Total Return: {total_return}")

def mplfinance_plot(ticker, chart_type, syear, smonth, sday, eyear, emonth, eday):
    start = f"{syear}-{smonth}-{sday}"
    end = f"{eyear}-{emonth}-{eday}"
    
    try:
        df = pd.read_csv("/Users/jung/Downloads/class_otter/code/jung/project2/" + ticker + ".csv")
    except FileNotFoundError:
        print("File Doesn't Exist")
    else:  
        df.index = pd.DateTimeIndex(df['Date'])
        df_sub = df.loc[start:end]
        mpf.plot(df_sub, type = 'candle')
        mpf.plot(df_sub, type = 'line')
        mpf.plot(df_sub, type = 'ohlc', mav = 4)
        
        s = mpf.make_mpf_style(base_mpf_style = 'charles', rc = {'font-size' : 8})
        fig = mpf.figure(figsize = (12, 8), style = s)
        ax = fig.add_subplot(2,1,2)
        av = fig.add_subplot(2,1,2, sharex = ax)
        mpf.plot(df_sub, type = chart_type, mav = (3,5,), ax = ax, volume = av, show_nontrading= True)

print(mplfinance_plot("AMZN", "ohlc", 2020, 1, 1, 2021, 1, 1))
# %%
