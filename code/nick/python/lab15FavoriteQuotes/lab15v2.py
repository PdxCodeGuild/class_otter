import requests
import json

response = requests.get('https://favqs.com/api/quotes?page=<page>&filter=keyword', headers = {'Content-Type' : 'application/json'})

# author = json.dumps(data['quote']['author'])
print(response)
