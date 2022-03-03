# Lab 15: Quotes API
# 01/25/2022


# For this lab we'll be using the Favqs Quotes API to first get a random quote, and then allow the user to find quotes by keyword. To accomplish this we'll be using the requests library.

import requests
import json
import pprint

# Version 1: 
# The URL to get a random quote is https://favqs.com/api/qotd, send a request here, parse the JSON in the response into a python dictionary, and show the quote and the author.

response = requests.get('https://favqs.com/api/qotd')
quotes_dict = json.loads(response.text)

print('\n')
# print(quotes_dict.get('quote').get('body'))
# print(quotes_dict.get('quote').get('author'))
# these didn't run because of the use of ' vs " for the f'string.
# print(f'Quote: {quotes_dict.get('quote').get('body')}')
# print(f'Author: {quotes_dict.get('quote').get('author')}')

# this format for referencing a dictionary within a dictionary is more common than the above, and is slightly faster than the above because the get method uses some try and accept features.
print(f"Quote: {quotes_dict['quote']['body']}")
print(f"Author: {quotes_dict['quote']['author']}")



# Version 2: List Quotes by Keyword
# The Favqs Quote API also supports getting a list of quotes associated with a given keyword https://favqs.com/api/quotes?page=<page>&filter=<keyword>. Prompt the user for a keyword, list the quotes you get in response, and prompt the user to either show the next page or enter a new keyword. You can use string concatenation to build the URL.

# > enter a keyword to search for quotes: nature
# 25 quotes associated with nature - page 1
# <list of quotes>
# > enter 'next page' or 'done': next page
# 25 quotes associated with nature - page 2
# <list of quotes>
# > enter 'next page' or 'done': done
# > enter a keyword to search for quotes:


# This API endpoint requires an API key be included in a request header. You can find documentation of specifying request headers here and documentation on authorization with the Favqs API here under "Authorization".

# headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}

print('\n\n')
page = 0
search_term = input("Enter a keyword to search for quotes: ")


# theres URL params will add to the URL to fill the text "?page=<page>&filter=<keyword>"
url_params = {
    'page': page,
    'filter': search_term
}

response_v2 = requests.get('https://favqs.com/api/quotes', params = url_params, headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}) 


quotes_dict_v2 = json.loads(response_v2.text)
# print(quotes_dict_v2)

pprint.pprint(response_v2.json())

