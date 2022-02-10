# PDX Code Guild Mini-Capstone Project
# Yelp Restaurant Data Scraper and Visualization
# 01/27/2022
# Keenan Tabusa



# I wanted to use beautifulsoup to pull restaurant category data from yelp and graph it

# note: case sensitive BeautifulSoup and Counter
from bs4 import BeautifulSoup
import requests
import lxml
from collections import Counter
from matplotlib import pyplot as plt


page = requests.get('https://www.yelp.com/search?find_desc=Restaurants&find_loc=Portland%2C+OR&ns=1')
# This takes the page and converts it to text
page_text = page.text
# this converts the page to a bs4 object, 
soup_page = BeautifulSoup(page_text, 'lxml')

# for multiple pages can change the start #,  https://www.yelp.com/search?find_desc=Restaurants&find_loc=Portland%2C+OR&ns=1&start=0
# ugly to get the next 4 pages but need the data
page2 = requests.get('https://www.yelp.com/search?find_desc=Restaurants&find_loc=Portland&start=10')
page3 = requests.get('https://www.yelp.com/search?find_desc=Restaurants&find_loc=Portland&start=20')
# page4 = requests.get('https://www.yelp.com/search?find_desc=Restaurants&find_loc=Portland&start=30')
# page5 = requests.get('https://www.yelp.com/search?find_desc=Restaurants&find_loc=Portland&start=40')
page2_text = page2.text
page3_text = page3.text
# page4_text = page4.text
# page5_text = page5.text

soup_page2 = BeautifulSoup(page2_text, 'lxml')
soup_page3 = BeautifulSoup(page3_text, 'lxml')
# soup_page4 = BeautifulSoup(page4_text, 'lxml')
# soup_page5 = BeautifulSoup(page5_text, 'lxml')


# This section pulls the names of the restaurants from the first page.


# restaurants = soup_page.find_all("a", class_="css-1422juy")
# print(restaurants)

# this is able to pull all of the class css items, that have the attribute 'name', in order to filter out the generic link buttons
# for restaurant in restaurants:
#    if restaurant.has_attr("name"):
#        print(restaurant)
#        print(restaurant.contents)
# print(restaurants)
# print('\n')

categories = soup_page.find_all('p', class_ ="css-1p8aobs")
categories2 = soup_page2.find_all('p', class_ ="css-1p8aobs")
categories3 = soup_page3.find_all('p', class_ ="css-1p8aobs")
# categories4 = soup_page4.find_all('p', class_ ="css-1p8aobs")
# categories5 = soup_page5.find_all('p', class_ ="css-1p8aobs")

# print(categories)
# for cats in categories:
#     print(cats.get_text())

# categories_list = []
# for cats in categories:
#     categories_list.append(cats.get_text())

# list comprehension version of above
category_list = [cats.get_text() for cats in categories]

# look up whether you can loop or otherwise combine these into the original list comprehension
for cats in categories2:
    category_list.append(cats.get_text())

for cats in categories3:
    category_list.append(cats.get_text())

# for cats in categories4:
#     category_list.append(cats.get_text())

# for cats in categories5:
#      category_list.append(cats.get_text())


# Counter creates a specific counter class of dictionary so we cast the Counter data type to a regular dictionary
count = Counter(category_list)
count_dict = dict(count)

# the dictionary needs to be updated with .items() to update the dict key value pairs to a list of tuples
count_list = count_dict.items()

# can add the  reverse=True, parameter to reverse the order of the category headers
count_list = sorted(count_list)


# using a * before count_list fixes this from a "x, y = zip(count_list) ValueError: too many values to unpack (expected 2)"
# need to look in to why, it may just remove the 'dict_items()' bracket from the count_list
x, y = zip(*count_list)


# Graphing using maplotlib
plt.bar(x,y)
plt.xlabel('Retaurant Categories')
plt.xticks(rotation=45, ha='right')
plt.ylabel('Frequency')
plt.title('The Frequency of Restaurant Categories for the Top 30 Restaurants in Yelp')
plt.show()


# scatter plot by category/color, x and y: cost and rating

# can adjust the below string to search by other locations
# https://www.yelp.com/search?find_desc=Restaurants&find_loc=Portland%2C+OR&ns=1

# can output to a csv showing restaurant name and categories?



# In order to sort a list by the second variable we can use this function to sort them in place
# this wasn't working because we were trying to sort a dictionary? or list of tupes
# def sort_second(list):
#     list.sort(key = lambda x: x[1])
#     return list

# print(count_list)
# print(sort_second(count_list))