
import pprint
import requests

# response = requests.get('https://api.ipify.org')
# print(response.url)
# print(response.text) # 76.105.187.182
# print(response.status_code) # 200
# print(response.encoding) # ISO-8859-1
# print(response.headers) # {'Content-Type': 'text/plain', 'Content-Length': '14', ...}

search_word = 'home'

response_ = requests.get(r'https://favqs.com/api/quotes', headers = {
        'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"',
        'page': '1',
        'filter': search_word
        })
json_response = response_.json()
pprint.pprint(json_response)