# ********************************** #
#         Lab 15: Quotes API         #
#   HTTP request get response json   #
#            Version: 2.0            #
#        Author: Bruce Stull         #
#             2022-01-25             #
# ********************************** #

import requests
import pprint
from requests.exceptions import HTTPError

# Assignment:
# https://github.com/PdxCodeGuild/class_otter/blob/main/1%20Python/labs/15%20Quotes%20API.md

# Resources:
# https://github.com/PdxCodeGuild/class_otter/blob/main/1%20Python/docs/15%20Requests.md
# https://github.com/PdxCodeGuild/class_otter/blob/main/code/merritt/22-jan/requests_example.py

# My personal token.
# Authorization: Token token="YOUR_APP_TOKEN"
# Authorization: Token token="4f13816a758c95d727f9c205e27da41f"
# Python_Quote_Retreiver	4f13816a758c95d727f9c205e27da41f	

def submit_request_get_json(url, headers, **kwargs):
    '''Accepts argument of search term and search_word. Submits request to website and, hopefully, returns json object.'''
    try:
        # Get response object.
        response = requests.get(
            url,
            params = kwargs,
            headers = headers
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


# I want to add a '-' to the beginning of the author string.
# This is overkill, but one way to do it is using this self-made function.
def insert_string_into_string(input_string: str, string_to_insert: str, index: int) -> str:
    '''Accepts a 'input_string' argument and inserts 'string_to_insert' at 'index'.'''
    return input_string[:index] + string_to_insert + input_string[index:]

def main():
    
    # For a search of quotes:
    ################################################
    search_word = 'death'

    # Class provided token.
    headers = {
        'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"',
        # 'Content-Type': 'application/json',
        }
    
    params = {
        'page': '1',
        'filter': search_word
        }

    json_response = submit_request_get_json('https://favqs.com/api/quotes', headers, **params)
    
    pprint.pprint(json_response)

    quote_string = f"\n{json_response['quotes'][0]['body']}"
    quote_author_string = f"{json_response['quotes'][0]['author']}\n"

    quote_author_string = insert_string_into_string(quote_author_string, '-', 0)

    print(quote_string)
    print(quote_author_string.rjust(len(quote_string) - 1, ' '))
    ################################################

    
    # # For quote of the day:
    # ################################################
    # json_response = submit_request_get_json('https://favqs.com/api/qotd')

    # pprint.pprint(json_response)

    # quote_string = f"\n{json_response['quote']['body']}"
    # quote_author_string = f"{json_response['quote']['author']}\n"

    # quote_author_string = insert_string_into_string(quote_author_string, '-', 0)

    # print(quote_string)
    # print(quote_author_string.rjust(len(quote_string) - 1, ' '))
    # ################################################



if __name__ == '__main__':
    main()
    
# QOTD response:
# pprint.pprint(json_response)
# {'qotd_date': '2022-01-26T00:00:00.000+00:00',
#  'quote': {'author': 'George Carlin',
#            'author_permalink': 'george-carlin',
#            'body': "If it's true that our species is alone in the universe, "
#                    "then I'd have to say the universe aimed rather low and "
#                    'settled for very little.',
#            'dialogue': False,
#            'downvotes_count': 0,
#            'favorites_count': 0,
#            'id': 1709,
#            'private': False,
#            'tags': ['alone'],
#            'upvotes_count': 1,
#            'url': 'https://favqs.com/quotes/george-carlin/1709-if-it-s-true-t-'}}