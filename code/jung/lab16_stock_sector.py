#----------------------Get all the libraries I need using 'pip install'-------------------------#

from bs4 import BeautifulSoup
import requests
import pprint 
import pandas as pd


#----------------------Using Get method to get all information of the URL-------------------------#

url = "https://money.cnn.com/data/us_markets/"
response = requests.get(url)
# print(response.content)
# pprint.pprint(response.content)
soup = BeautifulSoup(response.content, "html.parser") # Using bs4 to make HTML or XML looks nice and readable
# print(soup)

# 'class':'wsod_firstCol' contains name of sectors
tickers_sec = soup.find_all('td',{'class':'wsod_firstCol'}) # Find information from "Stock Sector" in CNN BUSINESS
# pprint.pprint(tickers_sec)


#----------------------Digging through HTML to find name-------------------------#
count = 0
tickers_list = []
for tickers in tickers_sec:
    for ticker in tickers:
        tickers_list.append(ticker)
# pprint.pprint(tickers_list)

tickers_list = tickers_list[20::1]
tickers = []
for items in tickers_list:
    for item in items:
        tickers.append(item)
# print(tickers) # I pull out the name and put it into a list called "tickers"



#----------------------Digging through HTML to find percentage-------------------------#
tickers_percent = soup.find_all("td", {"class": "wsod_aRight"}) 
# pprint.pprint(tickers_percent)

tickers_percent = tickers_percent[30::1]
# pprint.pprint(tickers_percent)

per_change = []
per_change_data = []

per_changes = [tickers_percent[i] for i in range(len(tickers_percent))]
for per_change in per_changes:
    # print(per_change)
    for per_chang in per_change:
        # print(per_chang)
        for per_chan in per_chang:
            # print(per_chan)
            per_change_data.append(per_chan)
# print(per_change_data)


# #----------------------Using pandas to make a data frame of "tickers", "price_data", "change_data", and "per_change_data" -------------------------#
data = []

df = pd.DataFrame(data)
df["Stock Sectors"] = tickers
df["%Change"] = per_change_data

# print(df)