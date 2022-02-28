"""
Utilities for Short.
"""

import random, string

SOURCE_OF_CHARACTERS = string.ascii_letters + string.digits

DEFAULT_CODE_SIZE = 7

def create_short_code(number_of_characters=DEFAULT_CODE_SIZE):
    """
    Generate and return an alphanumeric sequence of length
    NUMBER_OF_CHARACTERS.
    """
    code_sequence_list = (
        [random.choice(SOURCE_OF_CHARACTERS) for _ in range(number_of_characters)]
    )
    code_sequence_string = ''.join(code_sequence_list)
    return code_sequence_string

def print_meta_data_to_console_return_meta_data_dictionary(request, print_stuff=True):
    """
    Prints the request.META key and value pairs to console.
    """
    meta_data = request.META
    # print(type(meta_data))
    # # <class 'dict'>
    meta_data_keys = meta_data.keys()
    # print(type(meta_data_keys))
    # # <class 'dict_keys'>
    if print_stuff:
        print('\nStart printing "meta_data"')
        print(f"Request method: {request.method}")
        for key in meta_data_keys:
            print(f"{key} : {meta_data[key]}")
        print('End printing "meta_data"\n')
    return meta_data

def print_post_data_to_console_return_post_data_dictionary(request, print_stuff=True):
    """
    Prints the request.POST key and value pairs to console.
    """
    post_data = request.POST
    # post_data = request.GET
    # print(type(post_data))
    # # <class 'dict'>
    post_data_keys = post_data.keys()
    # print(type(post_data_keys))
    # # <class 'dict_keys'>
    if print_stuff:
        print('\nStart printing "post_data"')
        for key in post_data_keys:
            print(f"{key} : {post_data[key]}")
        print('End printing "post_data"\n')
    return post_data