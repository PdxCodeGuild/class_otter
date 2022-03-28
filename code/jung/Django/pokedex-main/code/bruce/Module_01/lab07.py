# ********************************* #
#         Lab 7 - ROT Cipher        #
#   Lists, Encryption, Decryption   #
#            Version: 2.1           #
#        Author: Bruce Stull        #
#             2022-01-10            #
# ********************************* #

# Assignment:
# https://github.com/PdxCodeGuild/class_otter/blob/bruce/1%20Python/labs/07%20ROT13.md

# Thinking:
# ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25']
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',  'l',  'm',  'n',  'o',  'p',  'q',  'r',  's',  't',  'u',  'v',  'w',  'x',  'y',  'z']
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',  'l',  'm',  'n',  'o',  'p',  'q',  'r',  's',  't',  'u',  'v',  'w',  'x',  'y',  'z']

import string

# String of alphabet letters.
# abcdefghijklmnopqrstuvwxyz
alphabet = string.ascii_lowercase

# Create list of alphabet letters.
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cipher_list_alpha = list(alphabet)

# schema 1:
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a']

# schema 5:
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# ['f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e']

# schema 13:
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']

# TODO: Add preservation of numbers, or, actually, encoding of numbers in addition to letters.

# Added functionality to filter out special characters like ',' '.' '!' '?' etc.
def filter_to_letters_and_spaces(input_string = ''):
    '''Accepts a string. Returns the string with special characters removed, spaces should be preserved.'''
    # Try to use list comprehension to filter out everything except for ascii letters and spaces.
    filtered_list = [character.lower() for character in input_string if (character in string.ascii_letters) or (character == ' ')]
    result_string = ''.join(filtered_list)
    return result_string

def test_filter_to_letters_and_spaces():
    assert filter_to_letters_and_spaces() == ''
    assert filter_to_letters_and_spaces("a!") == 'a'
    assert filter_to_letters_and_spaces("a b") == 'a b'
    assert filter_to_letters_and_spaces("!@g") == 'g'
    assert filter_to_letters_and_spaces("!@ g") == ' g'
    assert filter_to_letters_and_spaces("G") == 'g'
    assert filter_to_letters_and_spaces(",/ G") == ' g'

def encode_letter(code, schema = 13, cipher_list = cipher_list_alpha):
    '''Accepts arguments of code character, schema, and cipher cipher_list. Returns the coded letter.'''
    # Raw index of letter 'a' is 0.
    # Raw index of letter 'b' is 1.
    # code = 'a' >> letter = 'n'
    # Handle ' ' (space character).
    if code == ' ':
        return ' '
    # Use code to get a number. Use 'index()'.
    translation = cipher_list.index(code.lower())
    # Do something with that number.
    resolution = (translation + schema) % 26
    # Use the new number to get the letter.
    letter = cipher_list[resolution]
    return letter

def test_encode_letter():
    assert encode_letter(' ') == ' '
    # code = 'a', default cipher list, and schema 0 results in 'a'.
    assert encode_letter('a', 0) == 'a'
    assert encode_letter('a') == 'n'
    assert encode_letter('k') == 'x'
    assert encode_letter('a', 1) == 'b'
    assert encode_letter('y', 1) == 'z'
    assert encode_letter('e', 13) == 'r'
    assert encode_letter('t', 13) == 'g'
    assert encode_letter('b', 5) == 'g'
    assert encode_letter('B', 5) == 'g'

def decode_letter(code, schema = 13, cipher_list = cipher_list_alpha):
    '''Accepts encoded character, schema, and cipher cipher_list. Returns decoded character.'''
    # Handle ' ' (space character).
    if code == ' ':
        return ' '
    translation = cipher_list.index(code.lower())
    resolution = (translation - schema) % 26
    letter = cipher_list[resolution]
    return letter

def test_decode_letter():
    assert decode_letter(' ') == ' '
    assert decode_letter('a') == 'n'
    assert decode_letter('a', 5) == 'v'
    assert decode_letter('r', 13) == 'e'
    assert decode_letter('a', 1) == 'z'

def encode_message(message, schema = 13, cipher_list = cipher_list_alpha):
    '''Accepts message, schema, and cipher cipher_list. Returns encoded message string.'''
    message = filter_to_letters_and_spaces(message)
    encoded_message_as_list = [encode_letter(character, schema, cipher_list) for character in message]
    encoded_message_as_string = ''.join(encoded_message_as_list)
    return encoded_message_as_string

def test_encode_message():
    assert encode_message('') == ''
    assert encode_message(' ') == ' '
    assert encode_message('hi') == 'uv'
    assert encode_message('hi ho') == 'uv ub'
    assert encode_message('hi') == 'uv'
    assert encode_message('hi', 0) == 'hi'
    assert encode_message('hi ho', 5) == 'mn mt'

def decode_message(message, schema = 13, cipher_list = cipher_list_alpha):
    '''Accepts coded message, schema, and cipher cipher_list. Returns decoded message string.'''
    message = filter_to_letters_and_spaces(message)
    decoded_message_as_list = [decode_letter(character, schema, cipher_list) for character in message]
    decoded_message_as_string = ''.join(decoded_message_as_list)
    return decoded_message_as_string

def test_decode_message():
    assert decode_message('') == ''
    assert decode_message(' ') == ' '
    assert decode_message('yo') == 'lb'
    assert decode_message('yo lo') == 'lb yb'
    assert decode_message('dun', 0) == 'dun'
    assert decode_message('dun', 5) == 'ypi'


def main():
    
    # TODO: Add functionality where user can encode and decode as many messages as they want in the same session.
    # ############ Hard coded text ############
    # plain_text_message = "Soopur, seKret mEssige!"
    # encryption_schema = 13
    # rotation = encryption_schema
    # print(f"Plain text message:             {plain_text_message}")
    # print(f"Encoded message with schema {rotation}: {encode_message(plain_text_message, rotation)}")
    # print(f"Decoded message with schema {rotation}: {decode_message(encode_message(plain_text_message, rotation), rotation)}")
    # #########################################

    ########### User provided message and schema ###########
    # REPL
    # Prompt user for choice of encode/decode.
    # Start dialog for appropriate process.
    # Prompt user for message.
    # Process message according to user inputs.
    # Display results of process.

    while True:
        decode_or_encode = input("Please choose [E]ncode or [D]ecode: ").lower()
        if decode_or_encode not in ['e','d']:
            continue
        break
    if decode_or_encode == 'e':
        # User input of message and schema, and display of results:
        while True:
            plain_text_message = input("Please input message to be encryted: ")
            while True:
                encryption_schema_as_string = input("Please choose a numeric encryption schema (rotation): ")
                if not encryption_schema_as_string.isnumeric():
                    continue
                else:
                    encryption_schema = int(encryption_schema_as_string)
                    break
            rotation = encryption_schema
            print(f"Plain text message: {plain_text_message}")
            print(f"Encoded message with schema {rotation}: {encode_message(plain_text_message, rotation)}")
            break
    elif decode_or_encode == 'd':
        encrypted_message = input("Please input message to be decryted: ")
        while True:
            encryption_schema_as_string = input("Please choose a numeric encryption schema (rotation): ")
            if not encryption_schema_as_string.isnumeric():
                continue
            else:
                encryption_schema = int(encryption_schema_as_string)
                break
        rotation = encryption_schema
        print(f"Decoded message with schema {rotation}: {decode_message(encrypted_message, rotation)}")
    # else:
    #     continue
    ########################################################

main()