import requests

response = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'})
print(response.json())
joke = response.json()
print(joke['joke'])
