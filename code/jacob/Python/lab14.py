"""
Lab 14: Dad Joke API
"""

import requests
import json

type_selection = 0

while type_selection != 'done':
    print()
    type_selection = input('What type of search do you want to use? Enter "page" or "term" search or "done" to end? ')

    if type_selection == 'done':
        break

    elif type_selection == 'page':

        search_selection = int(input('What page do you want? '))

    elif type_selection == 'term':
        search_selection = input('What term are you looking for? ')

    print()
    response = requests.get('https://icanhazdadjoke.com/search', params = {type_selection: search_selection},  headers = {'Accept': 'application/json'})
    data = json.loads(response.text)

    for result in data['results']:
        print(result['joke'])

    