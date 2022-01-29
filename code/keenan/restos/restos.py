# PDX Code Guild Mini-Capstone Project
# Yelp Restaurant Data Scraper and Visualization
# 01/27/2022
# Keenan Tabusa

# installed the beautifulsoup4 library for this project
# could have used json - we've used this in the past to parse HTML files, bs4 is an alternative

# using beautifulsoup to pull restaurant category data from yelp
# can output to a csv showing restaurant name and categories?
# graph it

from bs4 import BeautifulSoup
import requests
# could use urllib library? but requests is preferred
import lxml

# open the webpage
# save the 'restaurant' as an individual variable (searching by class)
# scatter plot by category/color, x and y: cost and rating

# this will just ping the page
page = requests.get('https://www.yelp.com/search?find_desc=Restaurants&find_loc=Portland%2C+OR&ns=1')

# This takes the page and converts it to text
page_text = page.text

# this converts the page to a bs4 object, 
soup_page = BeautifulSoup(page_text, 'lxml')
# print(soup_page)

restaurants = soup_page.find_all("a", class_="css-1422juy")
print(restaurants)
print(restaurants.prettify())
print(len(restaurants))

# This should be the parse info we want? class = "css-1422juy"
# name = "lechon" is what we want to print for each instance
# the first instance of this class is just a 'portland' button
# the second is 'restaurants'


# can adjust the below string to search by other locations
# https://www.yelp.com/search?find_desc=Restaurants&find_loc=Portland%2C+OR&ns=1


