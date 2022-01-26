# Lab 14: Dad Joke API
# 01/24/2022

# Use the Dad Joke API to get a dad joke and display it to the user. You may want to also use time.sleep to add suspense.

# Part 1
# Use the requests library to send an HTTP request to https://icanhazdadjoke.com/ with the accept header as application/json. This will return a dad joke in JSON format. You can then use the .json() method on the response to get a dictionary. Get the joke out of the dictionary and show it to the user.

# Part 2 (optional)
# Add the ability to "search" for jokes using another endpoint. Create a REPL that allows one to enter a search term and go through jokes one at a time. You can also add support for multiple pages.


import requests
import json
import time

# term = input("Enter a joke search term: ")params = {"term": term}
response = requests.get('https://icanhazdadjoke.com/', headers = {"Accept": 'application/json'})

# setting a sleep timer
time.sleep(3)
print('\n')

# print(response.url)

# this response is a json string that looks like a dictionary
# print(response.text)
# is this a dictionary response already? if we use the .json()
# print(response.json())

# pprint.pprint(response.json())

dict_joke = json.loads(response.text)
# print(dict_joke)

print(dict_joke["joke"])


