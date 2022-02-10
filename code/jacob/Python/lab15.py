"""
Lab 15: Quotes API
"""

import requests
import json
"""
Version 1
"""
def quotd():
    response = requests.get('https://favqs.com/api/qotd', headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
    data = json.loads(response.text)

    return (f"Author:  {data['quote']['author']}\n Quote: {data['quote']['body']}")

"""    
print()
print(quotd())
print()

Version 2
"""
"""
page_selection = 0
page = 1
keyword = input('Enter a keyword to search for quotes: ')
while page_selection != 'done':
        
    response = requests.get('https://favqs.com/api/quotes', params = {'page': page, 'filter': keyword}, headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})

    data = json.loads(response.text)
    print()

    for result in data['quotes']:    
        try:
            print(f"Author: {result['author']}")
            print(f"Quote: {result['body']}")
        except KeyError:
            print('Last page has been reached!')
            break   
    print()
         
    page_selection = input("Enter 'next page' or 'done': ")

    if page_selection == 'done':
        break
    
    elif page_selection == 'next page':
        page += 1
"""