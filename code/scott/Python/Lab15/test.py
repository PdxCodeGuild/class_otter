# Version 1 of Lab
import requests

url = 'https://favqs.com/api/qotd'

response = requests.get(url)
data = response.json()
print('Author:', data['quote']['author'])
print('Quote:', data['quote']['body'])

# Version 2 of Lab
while True:
    user_input = input("Enter a keyword to search for quotes or 'done' to quit: ").lower()
    page = 1
    if user_input == 'done':
        break
    while True:
        keyword_url = f'https://favqs.com/api/quotes?page={page}&filter={user_input}'
        headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
        response = requests.get(keyword_url, headers = headers)
        data = response.json()
        num_quotes = 0
        for i in range(0, len(data['quotes'])):
            num_quotes += 1
        print(f'{num_quotes} quotes associated with {user_input} - page {page}\n')
        
        for quote in data['quotes']:
            print(quote['body'])

        next_page = input("Enter 'next page' or 'done': ")

        if next_page == 'next page' and data['last_page'] == True or next_page == 'next' and data['last_page'] == True:
            print('There are no more pages\n')
            break
        elif next_page == 'next page' or next_page == 'next':
            page += 1
        elif next_page == 'done':
            break
