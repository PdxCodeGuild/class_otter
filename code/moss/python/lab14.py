import requests
import json

### VERSION 1 ###
# response = requests.get('https://icanhazdadjoke.com/', headers = {'accept': 'application/json'} )

# jokes = response.json()

# print(jokes['joke'])

### OPTIONAL VERSION 2 INCOMPLETE ###

while True :

    search_term = input("\nWhat term would you like to search by? Enter a word or 'Q' to exit:\n").upper()
    
    if search_term == 'Q':
        print("\nGood-bye.")
        break
    
    else:

        response = requests.get('https://icanhazdadjoke.com/search', params = {"search_term":search_term}, headers={'Accept':'application/json'})
        
        data = json.loads(response.text)
        # print(data["results"])

        joke_quote_data = response.json()['results']
        
        for result in joke_quote_data:
            joke = result["joke"]
            print(joke)
        
         
            