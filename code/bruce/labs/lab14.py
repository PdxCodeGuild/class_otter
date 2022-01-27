# ********************************** #
#        Lab 14: Dad Joke API        #
#   request http GET response json   #
#            Version: 2.0            #
#        Author: Bruce Stull         #
#             2022-01-22             #
# ********************************** #

import time
import requests
import pprint
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


def submit_request_get_json(url='https://icanhazdadjoke.com/', **kwargs):
    '''Accepts argument of url. Submits request to website and, hopefully, returns json object.'''
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


def submit_search_request_get_json(search_word, url='https://icanhazdadjoke.com/search', search_limit=3, page=1, **kwargs):
# def submit_search_request_get_json(url='https://icanhazdadjoke.com/search', headers={}, params={}):
    '''Accepts argument of search term and search_word.
    Submits request to website and, hopefully, returns dictionary object.
    The result dictionary object is a dictionary with mostly integer values,
    except the 'results' value is a list of joke dictionaries with keys of 'id' and 'joke'.
    '''
    # add_search_term = f"term='{search_word}'"
    # add_search_limit = f"limit={search_limit}"
    # add_search_page = f"page=1"
    # query_string = f"{url}{add_search_term}&{add_search_limit}&{add_search_page}"

    params={
        'term': search_word,
        'limit': search_limit,
        'page': page
        }

    try:
        # Get response object.
        response = requests.get(
            url,
            headers=kwargs,
            # kwargs,
            params=params
            # headers={"Accept":"application/json", 'User-Agent': 'https://github.com/brucestull'}
            # kwargs
            # headers={"Accept":"application/json"}
            # headers
            )
        # Check for error handling.
        response.raise_for_status()
        # If response is successful, format response to json dictionary.
        json_response = response.json()
    except HTTPError as http_error:
        print(f'HTTP error occurred: {http_error}')
    except Exception as error:
        print(f'Other error occurred: {error}')
    # TODO: Add some sort of status check.
    return json_response


def console_display_scanner(
        scanner_width = 45,
        number_of_cycles = 2,
        time_delay = .007                
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
    # ########## A simple request ##########
    # # Get the json-formatted-dictionary response.
    # json_response = submit_request_get_json()

    # # Print response to review what we have.
    # # print(json_response)
    # # The request to https://icanhazdadjoke.com/ seems to result
    #     # in a dictionary with keys 'id', 'joke', and 'status'.
    # # {'id': '6MR79MJ6h', 'joke': 'My boss told me to have a good day... so I went home.', 'status': 200}

    # string_to_print = f'''
    #     Joke ID: {json_response['id']}
    #     Joke: {json_response['joke']}
    #     '''
    
    # print(string_to_print)
    # ######################################

    ########## Uses search word ##########
<<<<<<< Updated upstream
    page_requested = 1
=======
>>>>>>> Stashed changes
    while True:
        # Welcome user and tell them what we're doing here.
        welcome_string = "\nWelcome to icanhazdadjoke Searcherator 2022!"
        i_can_haz_request_url = 'https://icanhazdadjoke.com/'
        what_we_are_doing_here_string = f"Let's get some jokes from {i_can_haz_request_url}.\n"
        print(welcome_string)
        print(what_we_are_doing_here_string)

        # Prompt user to enter their search term.
        prompt_string = "What kind of dad jokes ya lookin for? "
        while True:
            search_word = input(prompt_string)
            if search_word != '':
                break
            else:
                print("To get the jokes, you gotta give us a word!")
                continue
        # Add blank line for visual clarity.
        print()

        # Display some eye candy.
        length_of_scanner = len(prompt_string + search_word)
        console_display_scanner(length_of_scanner)

<<<<<<< Updated upstream
        headers = {
            'Accept': 'application/json',
            'User-Agent': 'https://github.com/brucestull'
            }
        
        # search_limit = 3
        # page = page_requested
        # params={
        #     'term': search_word,
        #     'limit': search_limit,
        #     'page': page
        #     }
        
        # While loop to list the jokes on current page.
        while True:
            # Get the response from the API and return dictionary.
            json_response = submit_search_request_get_json(search_word, page=page_requested, **headers)
=======
        # Get the response from the API and return dictionary.
        json_response = submit_search_request_get_json(search_word)

        # Need to remember the keys for pages etc.
        # current_page : 1
        # limit : 20
        # next_page : 2
        # previous_page : 1
        # search_term : the
        # status : 200
        # total_jokes : 390
        # total_pages : 20

        # Display how many results and how many pages.
        search_results_display_string = f'''
        Search term: {json_response['search_term']}
        Total number of jokes: {json_response['total_jokes']}
        Pages total: {json_response['total_pages']}
        '''
        
        print(search_results_display_string)

        # The jokes are 'list' in the 'results' key.
        the_jokes_list = json_response['results']

        # print(f"{type(the_jokes_list)}{the_jokes_list}")
>>>>>>> Stashed changes

            # The jokes are in the 'results' key.
            the_jokes_list = json_response['results']

<<<<<<< Updated upstream
            if page_requested == 1:
                print(f"search_term: {json_response['search_term']}")
                print(f"Number of 'results' returned: {len(json_response['results'])}")
                print()
                print(f"total_pages: {json_response['total_pages']}")
                print(f"previous_page: {json_response['previous_page']}")
                print(f"current_page: {json_response['current_page']}")
                print(f"next_page: {json_response['next_page']}")
                print(f"status: {json_response['status']}")
                print(f"total_jokes: {json_response['total_jokes']}")
                print(f"limit: {json_response['limit']}")
                print()
            # While loop to list the jokes.
            while the_jokes_list:
                # Loop and display the jokes to user.
                # Don't delete or pop the jokes, allow user to cycle
                    # through them if they wish.
                for i in range(len(the_jokes_list)):
                    print(the_jokes_list[i]['joke'])
                    print()
                    while i < len(the_jokes_list) - 1:
                        input("Press <Enter> to continue to next joke. ")
                        if i == len(the_jokes_list) - 2:
                            print()
                            print()
                            print("And, last joke on current page:")                    
                        break
                    print()
                break
            
            # If there are more pages, prompt user to decide if they want to view next page.
            if json_response['total_pages'] > 1 and page_requested < json_response['total_pages']:
                get_the_next_page = input("Type [Y] to get the next page of jokes, anything else to quit: ").upper()
                print()
                if get_the_next_page == 'Y':
                    # Load next page.
                    page_requested += 1
                else:
                    break
                continue
            else:
                break
        print("Thanks for using icanhazdadjoke Searcherator 2022!")
        break
    ######################################
=======
        while the_jokes_list:
            # Loop and display the jokes to user.
            # Don't delete or pop the jokes, allow user to recycle
                # through them if they wish.
            for i in range(len(the_jokes_list)):
                print(f"Joke <{i + 1}>:")
                print(f"Joke ID: {the_jokes_list[i]['id']}")
                print(the_jokes_list[i]['joke'])
                print()
                # Display this 'continue' prompt until reaching the last joke.
                if i < len(the_jokes_list) - 1:
                    input("Press <Enter> to continue to next joke. ")
                print()
            break

        print(f"Sorry, out of jokes for search term: '{json_response['search_term']}'.")
        print()
        break
    ######################################

    pass
>>>>>>> Stashed changes

if __name__ == '__main__':
    main()