import requests

### VERSION 1 ###

response = requests.get('https://favqs.com/api/qotd')

quotes = response.json()['quote']

print(quotes['author'] + ',', quotes['body']) #'quote' -author F string

### VERSION 2 ###

usr_keywrd = input('Enter a keyword to search for quotes:')

page = 1 # +=1

url_params = {
    'filter': usr_keywrd,
    'page': page

}

response = requests.get('https://favqs.com/api/quotes?', params = url_params, headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})

quotes = response.json()['quotes']
print(quotes)


#REPL For loop nested while true loop
