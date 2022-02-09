import requests
import json
response = requests.get('https://favqs.com/api/qotd', headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}, params={'format': 'json'})
# print(response.text)
data = json.loads(response.text)
# print(data)
print(data['quote']['body'])
