# *********************** #
#      Function Args      #
#    *args and **kwargs   #
#       Version: 0.0      #
#   Author: Bruce Stull   #
#        2022-01-16       #
# *********************** #

from django.http import response
import requests
import pprint
from requests.exceptions import HTTPError

# Resources:
# https://github.com/PdxCodeGuild/class_otter/blob/main/1%20Python/docs/10%20Functions.md

# def print_movie_ratings(username, *args, **kwargs):
#     """Update the user’s ratings for movies.
#     Update movies from *args that are keys in **kwargs.
#     """
#     # '*args' results in a tuple within the function.
#     # '**kwargs', as input, asssigns dictionary values to the 'key's in '*args'.
#     # One utility of this functional usage is there are no errors if there are missing '*arg' or '**kwargs'.
#     film_and_ratings = {}
#     for film in args:  # Loop through the tuple `args`
#         if film in kwargs:  # Loop through keys of the `kwargs` dictionary
#             a_key, a_value = film, kwargs[film]
#             film_and_ratings[a_key] = a_value
#             print(a_key, a_value)
#     print(film_and_ratings)
    
# # # NOTE: 'Fargo' is not in '*args', and 'Transformers' is not in **kwargs. Yet we still get no error.
# # print_movie_ratings('jane', 'Sharknado', 'Frozen', 'Transformers', Sharknado=3, Frozen=2, Fargo=5)

# def create_film_and_rating_dictionary(username = '', *args, **kwargs):
#     '''Accepts arguments of username, and *args and **kwargs. Returns a dictionary of film ratings.'''
#     film_rating_dictionary = {}
#     for arg in args:
#         if arg in kwargs:
#             film, rating = arg, kwargs[arg]
#             film_rating_dictionary[film] = rating
#     print(film_rating_dictionary)
#     return film_rating_dictionary

# # create_film_and_rating_dictionary('jane', 'Sharknado', 'Frozen', 'Transformers', Sharknado=3, Frozen=2, Fargo=5)
# movies = ['jane', 'Sharknado', 'Frozen', 'Transformers']
# movie_ratings = {'Sharknado':3, 'Frozen':2, 'Fargo':5}
# # create_film_and_rating_dictionary(*movies, **movie_ratings)
# # {'Sharknado': 3, 'Frozen': 2}

# def create_kittens_dictionary(*args,**kwargs):
#     '''Creates dictionary of kittens and their color.'''
#     kittens = {}
#     print(f"the_kwargs: {kwargs}")
#     print(f"the_args: {args}")
#     for arg in args:
#         if arg in kwargs:
#             kitten, color = arg, kwargs[arg]
#             kittens[kitten] = color
#     print(kittens)
#     return kittens


# def test_create_kittens_dictionary():
#     assert create_kittens_dictionary(*kittens, **kitten_attributes) == {'dezzi':'grey','bunbun':'tortoise'}


# kittens = ['dezzi', 'greta', 'bunbun']
# kitten_attributes = {'dezzi':'grey', 'bunbun':'tortoise', 'shinx':'black'}



# # create_kittens_dictionary(*kittens, **kitten_attributes)
# # {'dezzi': 'grey', 'bunbun': 'tortoise'}


# # See if I can pass two separate **kwargs into function
# def a_list_and_multiple_dictionaries(*args, **kwargs):
#     headers = kwargs['headers']
#     params = kwargs['params']
#     print(headers, params)

# word_to_search = 'potato'
# input_dictionary = {
#     'headers': {'Accept': 'thing_to_accept'},
#     'params': {'item': word_to_search}
# }
# a_list_and_multiple_dictionaries(**input_dictionary)


# # From an online example:
# def process_data(a, b, c, d):
#     print(a, b, c, d)

# x = {'a': 1, 'b': 2}
# y = {'c': 3, 'd': 4}

# # process_data(**x, **y)
# # process_data(**x, c=23, d=42)

# Can I pass both the 'headers' and 'params' through as a kwarg? I have tried a couple methods but have not succeeded.
def submit_search_request_get_json(url='https://icanhazdadjoke.com/search', **kwargs):

    # params={
    #     'term': search_word,
    #     'limit': search_limit,
    #     'page': page
    #     }

    try:
        # Get response object.
        response = requests.get(
            url,
            params = kwargs,
            headers={"Accept":"application/json",
            # headers={"Accept":"text/plain",
                'User-Agent': 'https://github.com/brucestull'
                }
            # headers=kwargs,
            # params=params,
            )

        response.raise_for_status()
        json_response = response.json()
        # json_response = response
    except HTTPError as http_error:
        print(f'HTTP error occurred: {http_error}')
    except Exception as error:
        print(f'Other error occurred: {error}')
    return json_response

search_word = 'house'
search_limit = 3
page = 1

params={
    'term': search_word,
    'limit': search_limit,
    'page': page
    }

json_response = submit_search_request_get_json(**params)

# print(json_response.text)
# My wife is on a tropical fruit diet, the house is full of stuff. It is enough to make a mango crazy.Why did the house go to the doctor? It was having window panes.Someone broke into my house last night and stole my limbo trophy. How low can you go?

print(json_response)
# {'current_page': 1, 'limit': 3, 'next_page': 2, 'previous_page': 1, 'results': [{'id': 'mO7hqWvsPCd', 'joke': 'My wife is on a tropical fruit diet, the house is full of stuff. It is enough to make a mango crazy.'}, {'id': 'fNZTCdFBImb', 'joke': 'Why did the house go to the doctor? It was having window panes.'}, {'id': 'TvzdxXSCdFd', 'joke': 'Someone broke into my house last night and stole my limbo trophy. How low can you go?'}], 'search_term': 'house', 'status': 200, 'total_jokes': 7, 'total_pages': 3}
pprint.pprint(json_response)
# {'current_page': 1,
#  'limit': 3,
#  'next_page': 2,
#  'previous_page': 1,
#  'results': [{'id': 'mO7hqWvsPCd',
#               'joke': 'My wife is on a tropical fruit diet, the house is full '
#                       'of stuff. It is enough to make a mango crazy.'},
#              {'id': 'fNZTCdFBImb',
#               'joke': 'Why did the house go to the doctor? It was having '
#                       'window panes.'},
#              {'id': 'TvzdxXSCdFd',
#               'joke': 'Someone broke into my house last night and stole my '
#                       'limbo trophy. How low can you go?'}],
#  'search_term': 'house',
#  'status': 200,
#  'total_jokes': 7,
#  'total_pages': 3}



#  'results': [{'id': 'SSnW8xsrrjb',
#               'joke': 'How does a penguin build it’s house? Igloos it '
#                       'together.'},
#                       "one's on the house"},
#              {'id': 'HQZorO7pWnb',
#               'joke': 'Coffee has a tough time at my house, every morning it '
#                       'gets mugged.'},
#              {'id': 'mO7hqWvsPCd',
#               'joke': 'My wife is on a tropical fruit diet, the house is full '
#                       'of stuff. It is enough to make a mango crazy.'},
#              {'id': 'fNZTCdFBImb',
#               'joke': 'Why did the house go to the doctor? It was having '
#                       'window panes.'},
#              {'id': 'TvzdxXSCdFd',
#               'joke': 'Someone broke into my house last night and stole my '
#                       'limbo trophy. How low can you go?'},
#              {'id': '2gFIBX82Etc',
#               'joke': 'Do I enjoy making courthouse puns? Guilty'}]


