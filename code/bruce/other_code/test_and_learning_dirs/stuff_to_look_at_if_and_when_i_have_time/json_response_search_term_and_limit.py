# ************************************** #
#         JSON Resonse Learning          #
#   json response requests search HTTP   #
#              Version: 1.0              #
#          Author: Bruce Stull           #
#               2022-01-24               #
# ************************************** #

import requests
from requests.exceptions import HTTPError


# TODO: Figure out if it's possible to pass a headers dictionary through to requests.get().
def submit_search_request_get_json(search_word, url='https://icanhazdadjoke.com/search?', search_limit=2, **kwargs):
    '''Accepts argument of search term and search_word.
    Submits request to website and, hopefully, returns dictionary object.
    The result dictionary object is a dictionary with mostly integer values,
    except the 'results' value is a list of joke dictionaries with keys of 'id' and 'joke'.
    '''
    add_search_term = f"term='{search_word}'"
    add_search_limit = f"limit={search_limit}"
    add_search_page = f"page=2"
    
    # Limit search to 2 items.
    # search_limit = 2
    # add_search_limit = f"limit={search_limit}"
    # # total_jokes: 3
    # # limit: 2
    # # Number of results returned: 2
    
    # # What happens if we add the parameter, but use an empty string for the value?
    # # It seems the extraneous '&' doesn't cause request to crash, the 'limit' reverts to default (20).
    # search_limit = ''
    # add_search_limit = f"limit={search_limit}"
    # # total_jokes: 3
    # # limit: 20
    # # Number of results returned: 3

    query_string = f"{url}{add_search_term}&{add_search_limit}&{add_search_page}"

    try:
        # Get response object.
        response = requests.get(
            query_string,
            headers={"Accept":"application/json", "User-Agent": "https://github.com/brucestull"}
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
    return json_response


# # ['current_page', 'limit', 'next_page', 'previous_page', 'search_term', 'status', 'total_jokes', 'total_pages']
headers_dictionary = {"Accept":"application/json"}
json_response = submit_search_request_get_json('hipster')
print(f"search_term: {json_response['search_term']}")
print(f"Number of 'results' returned: {len(json_response['results'])}")
print(f"total_pages: {json_response['total_pages']}")
print(f"previous_page: {json_response['previous_page']}")
print(f"current_page: {json_response['current_page']}")
print(f"next_page: {json_response['next_page']}")
print(f"status: {json_response['status']}")
print(f"total_jokes: {json_response['total_jokes']}")
print(f"limit: {json_response['limit']}")

# the_new_json_response = submit_search_request_get_json('the')
the_new_json_response = {'current_page': 1, 'limit': 20, 'next_page': 2, 'previous_page': 1, 'results': [{'id': 'HeiqcaMRKBd', 'joke': 'What???s the longest word in the dictionary? Smiles. Because there???s a mile between the two S???s.'}, {'id': 'pzXvHl3EYg', 'joke': 'Why don???t seagulls fly over the bay? Because then they???d be bay-gulls!'}, {'id': 'yP7MRucFQCd', 'joke': 'Did you hear about the guy who invented Lifesavers? They say he made a mint.'}, {'id': 'ZDAIRn39prc', 'joke': "Ever wondered why bees hum? It's because they don't know the words."}, {'id': 'IRKJBQ7p4wc', 'joke': ' I never wanted to believe that my Dad was stealing from his job as a road worker. But when I got home, all the signs were there.\r\n\r\n'}, {'id': 'a218pbMmOmb', 'joke': "What's the best thing about elevator jokes? They work on so many levels."}, {'id': 'JJ61L61Lusc', 'joke': 'How many bones are in the human hand? A handful of them.'}, {'id': 'aMmbaFYTKBd', 'joke': "I finally bought the limited edition Thesaurus that I've always wanted. When I opened it, all the pages were blank.\r\nI have no words to describe how angry I am."}, {'id': 'JmjbxkGJBAd', 'joke': 'Egyptians claimed to invent the guitar, but they were such lyres.\ufeff'}, {'id': 'KJmrOKeNexc', 'joke': 'This morning I was wondering where the sun was, but then it dawned on me.'}, {'id': 'KmW8hFlV0ob', 'joke': 'A panda walks into a bar and says to the bartender ???I???ll have a Scotch and . . . . . . . . . . . . . . Coke thank you???. \r\n\r\n???Sure thing??? the bartender replies and asks ???but what???s with the big pause???? \r\n\r\nThe panda holds up his hands and says ???I was born with them???'}, {'id': 'caxscaMRnjb', 'joke': "Did you know the first French fries weren't actually cooked in France? They were cooked in Greece."}, {'id': 'ci311DtH6h', 'joke': 'I???ll tell you something about German sausages, they???re the wurst'}, {'id': 'u4Tvkba21wc', 'joke': 'Why did Sweden start painting barcodes on the sides of their battleships? So they could Scandinavian.'}, {'id': 'MZ82EIB5hFd', 'joke': 'Why did the melons plan a big wedding? Because they cantaloupe!'}, {'id': 'NZDlb299Uf', 'joke': 'Where do sheep go to get their hair cut? The baa-baa shop.'}, {'id': 'exXSCtkOKe', 'joke': 'Why do pirates not know the alphabet? They always get stuck at "C".'}, {'id': 'f211DdFBdxc', 'joke': "Did you hear about the chameleon who couldn't change color? They had a reptile dysfunction."}, {'id': '2giGYLeiGe', 'joke': 'Hear about the new restaurant called Karma? There???s no menu: You get what you deserve.'}, {'id': 'xAlOZ8pOmjb', 'joke': 'How do the trees get on the internet? They log on.'}], 'search_term': 'the', 'status': 200, 'total_jokes': 390, 'total_pages': 20}
# print(the_new_json_response)

the_json_response = {'current_page': 1, 'limit': 20, 'next_page': 2, 'previous_page': 1, 'results': [{'id': '69xAsrHYDAd', 'joke': 'Why did Mozart kill all his chickens?\r\nBecause when he asked them who the best composer was, they\'d all say "Bach bach bach!"\r\n'}, {'id': 'aMmbaFYTKBd', 'joke': "I finally bought the limited edition Thesaurus that I've always wanted. When I opened it, all the pages were blank.\r\nI have no words to describe how angry I am."}, {'id': 'lbU01DljGtc', 'joke': "I couldn't get a reservation at the library. They were completely booked."}, {'id': 'caxscaMRnjb', 'joke': "Did you know the first French fries weren't actually cooked in France? They were cooked in Greece."}, {'id': 'ci311DtH6h', 'joke': 'I???ll tell you something about German sausages, they???re the wurst'}, {'id': 'lyk3EIBQfxc', 'joke': 'I went to the zoo the other day, there was only one dog in it. It was a shitzu.'}, {'id': 'm3wPZoz51ob', 'joke': 'Did you hear the news? FedEx and UPS are merging. They???re going to go by the name Fed-Up from now on.'}, {'id': '82wHlbaapzd', 'joke': "Me: If humans lose the ability to hear high frequency volumes as they get older, can my 4 week old son hear a dog whistle?\r\n\r\nDoctor: No, humans can never hear that high of a frequency no matter what age they are.\r\n\r\nMe: Trick question... dogs can't whistle."}, {'id': 'mbpbapbhiyd', 'joke': 'Did you hear about the bread factory burning down? They say the business is toast.'}, {'id': '8hFYojqz5h', 'joke': "Why don't skeletons ride roller coasters? They don't have the stomach for it."}, {'id': 'nWvcUD5orrc', 'joke': 'I asked the surgeon if I could administer my own anesthetic, they said: go ahead, knock yourself out.'}, {'id': '9hiGeNZ0Tnb', 'joke': 'They tried to make a diamond shaped like a duck. It quacked under the pressure.'}, {'id': 'exXSCtkOKe', 'joke': 'Why do pirates not know the alphabet? They always get stuck at "C".'}, {'id': 'f211DdFBdxc', 'joke': "Did you hear about the chameleon who couldn't change color? They had a reptile dysfunction."}, {'id': '2giGYLeiGe', 'joke': 'Hear about the new restaurant called Karma? There???s no menu: You get what you deserve.'}, {'id': 'obahq4MJtzd', 'joke': 'I had a rough day, and then somebody went and ripped the front and back pages from my dictionary. It just goes from bad to worse.'}, {'id': 'A5MCY821gib', 'joke': "Why do bees hum? Because they don't know the words."}, {'id': 'AAIYo4MJmrc', 'joke': 'A magician was driving down the street and then he turned into a driveway.'}, {'id': 'AXnrrcNmyAd', 'joke': 'Why do bananas have to put on sunscreen before they go to the beach? Because they might peel!'}, {'id': 'pjyA59MRusc', 'joke': 'There???s a new type of broom out, it???s sweeping the nation.'}], 'search_term': 'the', 'status': 200, 'total_jokes': 390, 'total_pages': 20}

keys_object = the_json_response.keys()

the_keys = []
for key in keys_object:
    the_keys.append(key)

# print(the_keys)
# # These are the keys() of the dictionary 'the_json_response'.
# # ['current_page', 'limit', 'next_page', 'previous_page', 'results', 'search_term', 'status', 'total_jokes', 'total_pages']

# # What type are the values for the keys?
# type_key_list = []
# for key in the_keys:
#     type_key_string = f"{type(the_json_response[key])}: {key}"
#     type_key_list.append(type_key_string)
# for string_ in type_key_list:
#     print(string_)
# # These are the type() of the key's values' and the corresponding key.
# # They all make sense:
#     # 'int' for the stats elements
#     # 'list' for the joke list
#     # 'str' for the search term
# # <class 'int'>: current_page
# # <class 'int'>: limit
# # <class 'int'>: next_page
# # <class 'int'>: previous_page
# # <class 'list'>: results
# # <class 'str'>: search_term
# # <class 'int'>: status
# # <class 'int'>: total_jokes
# # <class 'int'>: total_pages

# Pop the key 'results' from the list and see what remains. 'results' is the key which holds the jokes.
the_keys.pop(the_keys.index('results'))

# NOTE: There are no 'keys' for the 'results' 'joke_keys_object'. It is a LIST of dictionaries.
# joke_keys_object = the_json_response['results'].keys()
# print(joke_keys_object)

# How to loop through the provided jokes?


# print(the_keys)
# # ['current_page', 'limit', 'next_page', 'previous_page', 'search_term', 'status', 'total_jokes', 'total_pages']

# for key in the_keys:
#     print(f"{key} : {the_json_response[key]}")
# # current_page : 1
# # limit : 20
# # next_page : 2
# # previous_page : 1
# # search_term : the
# # status : 200
# # total_jokes : 390
# # total_pages : 20

# Get the jokes from the json.
# NOTE: The 'results' key holds a list of 'joke' dictionaries.
the_jokes = the_json_response.pop('results')

# # How many jokes do we have? It seems the default return number of jokes is 20.
# print(type(the_jokes), len(the_jokes))
# # <class 'list'> 20



# # 'https://icanhazdadjoke.com/' + 'search?term=' + search_word
# def submit_search_request_get_json(search_word, url='https://icanhazdadjoke.com/search?', search_limit=5, **kwargs):
# # def submit_search_request_get_json(search_word, url='https://icanhazdadjoke.com/', **kwargs):
#     '''Accepts argument of search term and search_word. Submits request to website and, hopefully, returns json object.'''
#     # string_between_url_and_search_term = 'search?term='

#     add_search_term = f"term='{search_word}'"
#     add_search_limit = f"limit={search_limit}"

#     query_string = f"{url}{add_search_term}&{add_search_limit}"

#     try:
#         # Get response object.
#         response = requests.get(
#             # f"{url}{string_between_url_and_search_term}{search_word}",
#             query_string,
#             headers={"Accept":"application/json"}
#             )
#         # Check for error handling.
#         response.raise_for_status()
#         # If response is successful, format response to json dictionary.
#         json_response = response.json()
#     except HTTPError as http_error:
#         print(f'HTTP error occurred: {http_error}')
#     except Exception as error:
#         print(f'Other error occurred: {error}')
#     return json_response