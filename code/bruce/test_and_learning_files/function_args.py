# *********************** #
#      Function Args      #
#    *args and **kwargs   #
#       Version: 0.0      #
#   Author: Bruce Stull   #
#        2022-01-16       #
# *********************** #

# Resources:
# https://github.com/PdxCodeGuild/class_otter/blob/main/1%20Python/docs/10%20Functions.md

def print_movie_ratings(username, *args, **kwargs):
    """Update the user’s ratings for movies.
    Update movies from *args that are keys in **kwargs.
    """
    # '*args' results in a tuple within the function.
    # '**kwargs', as input, asssigns dictionary values to the 'key's in '*args'.
    # One utility of this functional usage is there are no errors if there are missing '*arg' or '**kwargs'.
    film_and_ratings = {}
    for film in args:  # Loop through the tuple `args`
        if film in kwargs:  # Loop through keys of the `kwargs` dictionary
            a_key, a_value = film, kwargs[film]
            film_and_ratings[a_key] = a_value
            print(a_key, a_value)
    print(film_and_ratings)
    
# # NOTE: 'Fargo' is not in '*args', and 'Transformers' is not in **kwargs. Yet we still get no error.
# print_movie_ratings('jane', 'Sharknado', 'Frozen', 'Transformers', Sharknado=3, Frozen=2, Fargo=5)

def create_film_and_rating_dictionary(username, *args, **kwargs):
    '''Accepts arguments of username, and *args and **kwargs. Returns a dictionary of film ratings.'''
    film_rating_dictionary = {}
    for arg in args:
        if arg in kwargs:
            film, rating = arg, kwargs[arg]
            film_rating_dictionary[film] = rating
    print(film_rating_dictionary)
    return film_rating_dictionary

# create_film_and_rating_dictionary('jane', 'Sharknado', 'Frozen', 'Transformers', Sharknado=3, Frozen=2, Fargo=5)

def create_kittens_dictionary(*args,**kwargs):
    '''Creates dictionary of kittens and their color.'''
    kittens = {}
    for arg in args:
        if arg in kwargs:
            kitten, color = arg, kwargs[arg]
            kittens[kitten] = color
    print(kittens)
    return kittens

create_kittens_dictionary('dezzi', 'greta', 'bunbun', dezzi='grey', bunbun='tortoise', shinx='black')
