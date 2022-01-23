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


############# Utilities #############
# These will be added to modules in the future,
# but we are hard-coding the function into this file for now.

def print_variable_and_description(
        variable_under_review,
        description_of_logic='',
        print_logic_results=True
        ):
    '''Accepts three arguments: A variable we are examining,
    a description of the logic we are examining, and a print flag.
    '''
    __name__ = print_variable_and_description
    string_result = f"{print_variable_and_description.__name__}: {description_of_logic}: {variable_under_review}"
    if print_logic_results:
        print(string_result)
#####################################


def submit_request_get_json(url='https://icanhazdadjoke.com/', **kwargs):
    '''Accepts argument of search term and search_word. Submits request to website and, hopefully, returns json object.'''
    try:
        # Get response object.
        response = requests.get(
            f"{url}",
            headers={"Accept":"application/json"}
            )
        # Check for error handling.
        response.raise_for_status()
        # If response is successful, format response to json dictionary.
        json_response = response.json()
    except HTTPError as http_error:
        print(f'HTTP error occurred: {http_error}')
    except Exception as error:
        print(f'Other error occurred: {error}')
    return json_response


def submit_search_request_get_json(url, search_word, **kwargs):
    '''Accepts argument of search term and search_word. Submits request to website and, hopefully, returns json object.'''
    try:
        # Get response object.
        response = requests.get(
            f"{url}{search_word}",
            headers={"Accept":"application/json"}
            )
        # Check for error handling.
        response.raise_for_status()
        # If response is successful, format response to json dictionary.
        json_response = response.json()
    except HTTPError as http_error:
        print(f'HTTP error occurred: {http_error}')
    except Exception as error:
        print(f'Other error occurred: {error}')
    return json_response


def console_display_scanner(
        time_delay = .007,
        number_of_cycles = 3,
        scanner_width = 45
        ):
    '''Eye candy. Accepts arguments of time_delay, number_of_cycles, and scanner_width.
    Moves the console cursor back and forth at time_delay and length scanner_width.
    '''
    cycle = 1
    while cycle <= number_of_cycles:

        # Draw the spaces.
        for _ in range(scanner_width):
            print(' ', end='', flush=True)
            time.sleep(time_delay)

        # Draw the backspaces.
        for _ in range(scanner_width):
            print('\b', end='', flush=True)
            time.sleep(time_delay)
        
        cycle += 1


def main():

    # Get the json-formatted-dictionary response.
    json_response = submit_request_get_json()

    # Print response to review what we have.
    # print(json_response)
    # The request to https://icanhazdadjoke.com/ seems to result in a dictionary with keys 'id', 'joke', and 'status'.
    # {'id': '6MR79MJ6h', 'joke': 'My boss told me to have a good day... so I went home.', 'status': 200}

    string_to_print = f'''
        Joke ID: {json_response['id']}
        Joke: {json_response['joke']}
        '''
    
    print(string_to_print)
    # ########## Uses search word ##########
    # i_can_haz_search_url = 'https://icanhazdadjoke.com/search?term='
    # search_term = "hipster"
    
    # # 'results' is where the 'joke's are.
    # # Provides a list of 'joke' dictionaries. Keys are 'id' and 'joke'.
    # json_response = submit_search_request_get_json(i_can_haz_search_url, search_term)
    # #
    # the_jokes_list = json_response['results']

    # for joke in the_jokes_list:
    #     print(joke['joke'])

    # print(i_can_haz_search_url + search_term)  # https://icanhazdadjoke.com/search?term=hipster
    # ######################################

    pass

main()