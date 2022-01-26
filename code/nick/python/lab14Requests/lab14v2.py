import requests

term = input('what kinda joke do you want to hear? ')
response = requests.get(f'https://icanhazdadjoke.com/search?term={term}', headers={'Accept':'application/json'})
joke = response.json()
jokes = joke['results']

print(jokes[0])