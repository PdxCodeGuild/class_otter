import requests
import json

keyword = input('enter a key word to search for quotes. ')
page_number = 1

def page_of_quotes():
    for index in range(len(list_of_quotes)):
        for key in list_of_quotes[index]:
            if key == 'body':
                words = list_of_quotes[index][key]
            if key == 'author':
                author = list_of_quotes[index][key]
        print(f"'{words}' -{author}")
        print()
    print(f'25 quotes associated with {keyword} - page {page_number}')


response = requests.get(f'https://favqs.com/api/quotes?page={page_number}&filter={keyword}', headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
data = json.loads(response.text)
list_of_quotes = data['quotes']

page_of_quotes()
