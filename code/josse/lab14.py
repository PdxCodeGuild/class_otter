import requests
import time
response = requests.get('https://icanhazdadjoke.com/',
                        headers={'Accept': 'application/json'})
# print(response.text)  # 76.105.187.182
jokes = response.json()
print(jokes["joke"])
# print(jokes)
