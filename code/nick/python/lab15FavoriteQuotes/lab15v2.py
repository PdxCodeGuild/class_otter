import requests
import json

keyword = input('enter a keyword to search for quotes. ')
page_number = 1

while True:
    response = requests.get(f'https://favqs.com/api/quotes?page={page_number}&filter={keyword}', headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
    data = json.loads(response.text)


    page_of_quotes = data['quotes']
    number_of_quotes = 0

    for quote in page_of_quotes:
        number_of_quotes +=1
        print(f"{quote['body']}")
        print(quote['author'])
        print()
    print(f'there are {number_of_quotes} associated with {keyword}')

    user_input = input("enter 'next page' or 'done'. ")

    if user_input == 'next page':
        page_number +=1
    elif user_input == 'done':
        break
    else:
        break
