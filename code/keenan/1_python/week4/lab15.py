# Lab 15: Quotes API
# 01/25/2022
# updated 04/20/2022 - Site down as of 04/20/2022

# For this lab we'll be using the Favqs Quotes API to first get a random quote, and then allow the user to find quotes by keyword. To accomplish this we'll be using the requests library.

import requests
import json


# Version 1: 
# The URL to get a random quote is https://favqs.com/api/qotd, send a request here, parse the JSON in the response into a python dictionary, and show the quote and the author.

response = requests.get('https://favqs.com/api/qotd')
quotes_dict = json.loads(response.text)

print('\n')

print(quotes_dict.get('quote').get('body'))
print(quotes_dict.get('quote').get('author'))
# # these didn't run because of the use of ' vs " for the f'string.
# print(f'Quote: {quotes_dict.get('quote').get('body')}')
# print(f'Author: {quotes_dict.get('quote').get('author')}')

# this format for referencing a dictionary within a dictionary is more common than the above, and is slightly faster than the above because the get method uses some try and accept features.
# print(f"Quote: {quotes_dict['quote'].get('body')}")
# print(f"Author: {quotes_dict['quote'].get('author')}")



