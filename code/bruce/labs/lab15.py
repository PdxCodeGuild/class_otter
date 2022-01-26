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
        return json_response
    except HTTPError as http_error:
        print(f'HTTP error occurred: {http_error}')
    except Exception as error:
        print(f'Other error occurred: {error}')


# I want to add a '-' to the beginning of the author string.
# This is overkill, but one way to do it is using this self-made function.
def insert_string_into_string(input_string: str, string_to_insert: str, index: int) -> str:
    '''Accepts a 'input_string' argument and inserts 'string_to_insert' at 'index'.'''
    return input_string[:index] + string_to_insert + input_string[index:]

def main():
    
    ################################################
    # For a search of quotes:
    ################################################
    search_word = 'death'

    # Class provided token.
    headers = {
        'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"',
        }
    
    favorite_quote_url = 'https://favqs.com/api/quotes'

        
    # Welcome user.
    print(f"Let's get some quotes from {favorite_quote_url}.")

    get_next_group = False

    on_last_page = True

    page = 1

    while True:

        if get_next_group == True and on_last_page == False:
            page += 1
            print("That's the end of this group of pages.")
            done_with_group_want_another_batch = input(f"Do you want to fetch another batch for this same word, '{search_term}', <Enter> or [Q]uit? ").upper()
            print()
            if done_with_group_want_another_batch == 'Q':
                break
        
        else:
            print()
            search_term = input("Please enter your search term: ")
            print()
        
        if not search_term.isalpha():
            search_term = 'happiness'

        # Add the search term into the params dictionary.
        params = {
            'page': str(page),
            'filter': search_term
            }

        # Send the HTTPRequest
        json_response = submit_request_get_json(favorite_quote_url, headers, **params)
        # pprint.pprint(json_response)

        # Variable to hold if we're on last page.
        on_last_page = json_response['last_page']

        # If no quotes were found, notify user and prompt for new search term.
        if json_response['quotes'][0]['body'] == 'No quotes found':
            print(f"Sadly, we have no quotes regarding '{search_term}'.")
            continue
        
        # Get just the quotes.
        just_the_quotes = json_response['quotes']
        print()
        print(f"Number of '{search_term}' quotes returned: {len(just_the_quotes)}")
        print(f"Group: {json_response['page']}")

        # Prompt user for how many quotes per page. Convert to int or set to 5.
        quotes_per_page = input("How many quotes do you want to display per page? ")
        if not quotes_per_page.isnumeric():
            quotes_per_page = 5
        else:
            quotes_per_page = int(quotes_per_page)
        
        # Loop through the returned quotes.
        for i in range(len(just_the_quotes)):

            # print(get_next_group)

            # Get each quote from just_the_quotes.
            print()
            quote_string = f"{json_response['quotes'][i]['body']}"
            quote_author_string = f"{json_response['quotes'][i]['author']}"
            print()
            # Add a '-' in front of author attribution.
            quote_author_string = insert_string_into_string(quote_author_string, '-', 0)

            # Format and print the result.
            print(quote_string)
            print(quote_author_string.rjust(len(quote_string) - 1, ' '))

            
            if i == len(just_the_quotes) - 1:
                get_next_group = True
                break
            
            # Display the quotes in json_response in pages of size quotes_per_page.
            if (i + 1) % quotes_per_page != 0:
                continue

            # Prompt user for response.
            user_response = input("Press <Enter> for next page, [N]ew search, or [Q]uit: ").upper()
            print()
            if user_response == 'Q' or user_response == 'N':
                break
        
        # Go back to beginning if user wants a new search.
        if user_response == 'N':
            continue
        
        # Break and exit if user wishes.
        if user_response == 'Q':
            break

        # If we are not on the last search group, go back to the beginning and get next batch.
        if json_response['last_page'] == False:
            continue

        break
    print(f"Thanks for visiting quotes from {favorite_quote_url}.")
    print()

    ################################################

    
    # ################################################
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
    
# # QOTD response:
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


# {'last_page': False,
#  'page': 1,
#  'quotes': [{'author': 'Oscar Wilde',
#              'author_permalink': 'oscar-wilde',
#              'body': 'My own business always bores me to death. I prefer other '
#                      "people's.",
#              'dialogue': False,
#              'downvotes_count': 0,
#              'favorites_count': 2,
#              'id': 606,
#              'private': False,
#              'tags': ['funny'],
#              'upvotes_count': 1,
#              'url': 'https://favqs.com/quotes/oscar-wilde/606-my-own-business-'},
#             {'author': 'Simone de Beauvoir',
#              'author_permalink': 'simone-de-beauvoir',
#              'body': 'It is old age, rather than death, that is to be '
#                      "contrasted with life. Old age is life's parody, whereas "
#                      'death transforms life into a destiny: in a way it '
#                      'preserves it by giving it the absolute dimension. Death '
#                      'does away with time.',
#              'dialogue': False,
#              'downvotes_count': 0,
#              'favorites_count': 0,
#              'id': 1034,
#              'private': False,
#              'tags': ['age', 'death'],
#              'upvotes_count': 0,
#              'url': 'https://favqs.com/quotes/simone-de-beauvoir/1034-it-is-old-age--'}]}