import requests

### VERSION 1 ###
response = requests.get('https://icanhazdadjoke.com/', headers = {'accept': 'application/json'} )

jokes = response.json()

print(jokes['joke'])

### OPTIONAL VERSION 2 INCOMPLETE ###

while True :
    search_term = input("\nWhat term would you like to search by? Type a word or 'Q' to exit:\n")

    response = requests.get('https://icanhazdadjoke.com/search?term=' + search_term, headers={'accept':'application/json'} )
    jokes = response.json()['results']
    print(jokes)
    
    if search_term == 'Q':
        break
    else:
        for joke in jokes:
            print(joke)
        
         
            