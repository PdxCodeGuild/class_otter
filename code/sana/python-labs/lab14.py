import requests
import json
response = requests.get('https://icanhazdadjoke.com/', headers={'accept': 'application/json'})
print(response.text)
data = json.loads(response.text)
print(data)
# print(data['id'])
print(data['joke'])