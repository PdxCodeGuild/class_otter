import requests
import json

response = requests.get('https://favqs.com/api/qotd', headers = {'Content-Type' : 'application/json'})
data = json.loads(response.text)
quote = json.dumps(data['quote']['body'])
print()
# author = json.dumps(data['quote']['author'])

author = data['quote'].get('author')
print(f'{quote}\n -{author}')
print()





# print(json.dumps(data))
# print()
# print(quote)
# print()
# print(f'-{author}')
# print()
# print(data['quote'])
# print()
# pprint(data)