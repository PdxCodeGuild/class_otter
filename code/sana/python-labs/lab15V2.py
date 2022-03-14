import requests
import json
keyword = input('enter keyword: ')
page = 1
url = f"https://favqs.com/api/quotes?page={page}&filter={keyword}"
# print(url)
response = requests.get(url, headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}, params={'format': 'json'})
# print(response.text)
data = json.loads(response.text)
for quote in data['quotes']:
    print()
    print(quote['author'])
    print(quote['body'])
    print()
while data['last_page'] == False:
    command = input("Type 'n' for next page or 'k' to change keyword or 'q' to quit: ")
    if command == 'n':
        page += 1
        url = f"https://favqs.com/api/quotes?page={page}&filter={keyword}"
# print(url)
        response = requests.get(url, headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}, params={'format': 'json'})
# print(response.text)
        data = json.loads(response.text)
        for quote in data['quotes']:
            print()
            print(quote['author'])
            print(quote['body'])
            print()
    elif command == 'k':
        keyword = input('enter keyword: ')
        page = 1
        url = f"https://favqs.com/api/quotes?page={page}&filter={keyword}"
# print(url)
        response = requests.get(url, headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}, params={'format': 'json'})
# print(response.text)
        data = json.loads(response.text)
        for quote in data['quotes']:
            print()
            print(quote['author'])
            print(quote['body'])
            print()
    else:
        break