from bs4 import BeautifulSoup
import requests
import time
from random import randint


def scrape_news_summaries(s):
    time.sleep(randint(0, 2))  # relax and don't let google be angry
    r = requests.get("http://www.google.co.uk/search?q="+s+"&tbm=nws")
    print(r.status_code)  # Print the status code
    content = r.text
    news_summaries = []
    soup = BeautifulSoup(content, "html.parser")
    st_divs = soup.findAll("div", {"class": "st"})
    for st_div in st_divs:
        news_summaries.append(st_div.text)
    return news_summaries


l = scrape_news_summaries("T-Notes")
#l = scrape_news_summaries("""T-Notes""")
for n in l:
    print(n)