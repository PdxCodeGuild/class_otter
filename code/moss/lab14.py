import requests

### VERSION 1 ###
response = requests.get('https://icanhazdadjoke.com/', headers = {'accept': 'application/json'} )
jokes = response.json()
print(jokes['joke'])

### OPTIONAL VERSION 2 INCOMPLETE ###
# usr_search = input("\nWhat term would you like to search by? Type a word or 'Q' to exit:\n")

# response = requests.get('https://icanhazdadjoke.com/search', usr_search, headers={'accept':'application/json'} )
# jokes = response.json()['results']
# print(jokes)

# # while True :
# #     if usr_search == 'Q':
# #         break
# #     else:
# #         for joke in jokes:
# #             print(joke)
        
         
            