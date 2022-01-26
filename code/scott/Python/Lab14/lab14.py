import requests
import json
response = requests.get('https://icanhazdadjoke.com', params={format:json}, headers={'Accept': 'application/json',})
json_res = response.json()
print("\n")
print(json_res['joke'])
print("\n")