#----------------------Get all the libraries I need using 'pip install'-------------------------#

from bs4 import BeautifulSoup
import requests
import pprint
import pandas as pd


#----------------------Using Get method to get all information of the URL-------------------------#

url = "https://money.cnn.com/data/us_markets/"
response = requests.get(url)
# print(response.content)
soup = BeautifulSoup(response.content, "html.parser") # Using bs4 to make HTML looks nice and clean
# print(soup)

tickers_sec = soup.find_all('td',{'class':'wsod_firstCol'}) # Find information from "What's Moving" in CNN BUSINESS
# pprint.pprint(tickers_sec)


#----------------------Digging through HTML to find useful data-------------------------#
count = 0
tickers_list = []
for tickers in tickers_sec:
    for ticker in tickers:
        tickers_list.append(ticker)
# pprint.pprint(tickers_list)

tickers_list = tickers_list[1::2]
tickers = []
for items in tickers_list:
    for item in items:
        tickers.append(item)

tickers = tickers[0:10] # I only need 10 companies from "What's Moiving" in CNN BUSINESS
# pprint.pprint(tickers)


#----------------------Organize index by each list-------------------------#
tickers_price = soup.find_all("td", {"class": "wsod_aRight"}) 

tickers_price = tickers_price[0:30]
# pprint.pprint(tickers_price)

price_index = [0,3,6,9,12,15,18,21,24,27]
change_index = [1,4,7,10,13,16,19,22,25,28]
per_change_index = [2,5,8,11,14,17,20,23,26,29]


#----------------------Organize data by each list-------------------------#
prices =[]
price_data=[] 

prices = [tickers_price[i] for i in price_index] 
for price in prices:
    # print(price)
    for pri in price:
        # print(pri)    
        for p in pri:
            # print(p)
            price_data.append(p)
# print(price_data)


changes = []
change_data = []

changes = [tickers_price[i] for i in change_index]
for change_price in changes:
    # print(change_price)
    for change_pri in change_price:
        # print(change_pri)
        for change_p in change_pri:
            # print(change_p)
            for ch_p in change_p:
                # print(ch_p)
                change_data.append(ch_p)
# print(change_data)


per_change = []
per_change_data = []

per_changes = [tickers_price[i] for i in per_change_index]
for per_change in per_changes:
    # print(per_change)
    for per_chang in per_change:
        # print(per_chang)
        for per_chan in per_chang:
            for per_cha in per_chan:
                # print(per_cha)
                per_change_data.append(per_cha)
# print(per_change_data)
            


#----------------------Using pandas to make a data frame of "tickers", "price_data", "change_data", and "per_change_data" -------------------------#
data = []

df = pd.DataFrame(data)
df["Gainers & Losers"] = tickers
df["price"] = price_data
df["change"] = change_data
df["%change"] = per_change_data

print(df)