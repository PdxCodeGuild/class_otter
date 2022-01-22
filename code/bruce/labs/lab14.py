# ********************************** #
#        Lab 14: Dad Joke API        #
#   request http GET response json   #
#            Version: 1.0            #
#        Author: Bruce Stull         #
#             2022-01-22             #
# ********************************** #

import time
import requests
from requests.exceptions import HTTPError

# Assignment:
# https://github.com/PdxCodeGuild/class_otter/blob/main/1%20Python/labs/14%20Dad%20Joke%20API.md

# References:
# https://github.com/PdxCodeGuild/class_otter/blob/main/1%20Python/docs/15%20Requests.md
# https://icanhazdadjoke.com/api
# For searches:
    # https://icanhazdadjoke.com/api#search-for-dad-jokes

# Lab 14: Dad Joke API

# Use the Dad Joke API to get a dad joke and display it to the user.
# You may want to also use time.sleep to add suspense.

# Part 1
    # Use the requests library to send an HTTP request to https://icanhazdadjoke.com/
    # with the accept header as application/json. This will return a dad joke in JSON format.
    # You can then use the .json() method on the response to get a dictionary.
    # Get the joke out of the dictionary and show it to the user.

# Part 2 (optional)
    # Add the ability to "search" for jokes using another endpoint.
    # Create a REPL that allows one to enter a search term and go through jokes one at a time.
    # You can also add support for multiple pages.

# ############# Utilities #############
# # These will be added to modules in the future, but we are hard-coding the function into this file for now.

# def print_variable_and_description(variable_under_review, description_of_logic = '', print_logic_results = True):
#     '''Accepts three arguments: A variable we are examining, a description of the logic we are examining, and a print flag.'''
#     __name__ = print_variable_and_description
#     string_result = f"{print_variable_and_description.__name__}: {description_of_logic}: {variable_under_review}"
#     if print_logic_results:
#         print(string_result)
# #####################################

# ################## A simple request ##################
# try:
#     response = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'})
#     # Does some error handling.
#     response.raise_for_status()

#     # access JSON content
#     json_response = response.json()

# except HTTPError as http_err:
#     print(f'HTTP error occurred: {http_err}')
# except Exception as err:
#     print(f'Other error occurred: {err}')
# ######################################################
# ##################### How to 'get' the joke #####################
# # Print the response so we can see what stuff it includes.
# print(json_response)    # {'id': 'fNZTCdFBImb', 'joke': 'Why did the house go to the doctor? It was having window panes.', 'status': 200}

# # This is how we get the 'joke' from the 'response' since 'joke' is a key.
# the_joke = json_response['joke']
# print(the_joke)
# #################################################################

####################### How to get a 'search' response #######################
# Add 'search?term={search_term}' to the request string.
search_term = "hipster"

def submit_search_request_get_json(search_term):
    '''Accepts argument of search term. Submits search_term  to website and, hopefully, returns json object.'''
    try:
        response = requests.get(f"https://icanhazdadjoke.com/search?term={search_term}", headers= {"Accept":"application/json"})
        # Does some error handling.
        response.raise_for_status()
        # access JSON content
        json_response = response.json()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    return json_response

# # Example response.
# json_response = submit_search_request_get_json('hipster')
# print(json_response)
# # {'current_page': 1, 'limit': 20, 'next_page': 1, 'previous_page': 1, 'results': [{'id': 'xc21Lmbxcib', 'joke': 'How did the hipster burn the roof of his mouth? He ate the pizza before it was cool.'}, {'id': 'GlGBIY0wAAd', 'joke': 'How much does a hipster weigh? An instagram.'}, {'id': 'NRuHJYgaUDd', 'joke': "How many hipsters does it take to change a lightbulb? Oh, it's a really obscure number. You've probably never heard of it."}], 'search_term': 'hipster', 'status': 200, 'total_jokes': 3, 'total_pages': 1}

# # Lots of information, so let's get the keys first.
# json_response = submit_search_request_get_json('hipster')
# json_search_response_keys = json_response.keys()
# print(json_search_response_keys)   # dict_keys(['current_page', 'limit', 'next_page', 'previous_page', 'results', 'search_term', 'status', 'total_jokes', 'total_pages'])

# 'results' is where the 'joke's are.
# Provides a list of 'joke' dictionaries. Keys are 'id' and 'joke'.
json_response = submit_search_request_get_json('dog')
the_jokes_list = json_response['results']
# Displays a list, which contains several dictionaries, which each have an 'id' and 'joke'.
# print(the_jokes_list)
# [{'id': 'xc21Lmbxcib', 'joke': 'How did the hipster burn the roof of his mouth? He ate the pizza before it was cool.'}, {'id': 'GlGBIY0wAAd', 'joke': 'How much does a hipster weigh? An instagram.'}, {'id': 'NRuHJYgaUDd', 'joke': "How many hipsters does it take to change a lightbulb? Oh, it's a really obscure number. You've probably never heard of it."}]

for joke in the_jokes_list:
    print(joke['joke'])

##############################################################################



def main():
    pass

main()