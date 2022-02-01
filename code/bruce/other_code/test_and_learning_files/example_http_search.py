# *********************************** #
#         requests with search        #
#   HTTP API requests response json   #
#             Version: 0.0            #
#         Author: Bruce Stull         #
#              2022-01-22             #
# *********************************** #

import requests

# Resources:
# https://www.codespeedy.com/generating-jokes-in-python-with-the-help-of-apis/
# https://icanhazdadjoke.com/api#search-for-dad-jokes

search_term = input("Enter your search term: ")
response = requests.get(f"https://icanhazdadjoke.com/search?term={search_term}", headers= {"Accept":"application/json"})
connection = response.ok
json_response = response.json()
sequence_of_joke_ids = json_response["results"]
no_of_jokes = len(sequence_of_joke_ids)
user_input_string=""
if no_of_jokes==0:
  while no_of_jokes==0:
    user_input_string = input("Try some other word(Type 'quit' to quit): ")
    if user_input_string=="quit":
      break
    else:  
        response = requests.get(f"https://icanhazdadjoke.com/search?term={user_input_string}", headers= {"Accept":"application/json"})
        json_response = response.json()
        sequence_of_joke_ids = json_response["results"]
        no_of_jokes = len(sequence_of_joke_ids)

if user_input_string!="quit":
  response = requests.get(f"https://icanhazdadjoke.com/search?term={user_input_string}", headers= {"Accept":"application/json"})
  sequence_of_joke_ids = json_response["results"]
  no_of_jokes = len(sequence_of_joke_ids)
  print(f"There are {no_of_jokes} joke/s available.\n")
  print(f"The {no_of_jokes} jokes are:\n")
  x=0
  for each_joke in sequence_of_joke_ids:
    print(sequence_of_joke_ids[x]['joke'])
    x+=1