# ********************************************** #
#   Lab 9: Compute Automated Readability Index   #
#         regex, file I/O, dictionaries          #
#                  Version: 1.0                  #
#              Author: Bruce Stull               #
#                   2022-01-12                   #
# ********************************************** #

import string
import math
import time

LIST_OF_LETTERS = string.ascii_letters      # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
LIST_OF_PUNCTUATION = string.punctuation    # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
LIST_OF_DIGITS = string.digits              # 0123456789

# Assignment:
# https://github.com/PdxCodeGuild/class_otter/blob/bruce/1%20Python/labs/09%20ARI.md

# Dictionary with ARI scale, ages, and grade levels.
ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

def get_number_of_characters(text):
    '''Accepts a string 'text' and returns the number of letters and numbers in 'text'.'''
    # Convert text string to list so we can filter out everything but letters and numbers.
    text_as_list = list(text)
    # Use list comprehension to get list of letters and numbers. This filters out anything other than letters and numbers.
    letters_and_numbers = [character for character in text_as_list if (character in LIST_OF_LETTERS or character in LIST_OF_DIGITS)]
    # Use len() t0 get number of characters in list.
    count_of_letters_and_numbers = len(letters_and_numbers)
    return count_of_letters_and_numbers

def test_get_number_of_characters():
    assert get_number_of_characters("the") == 3
    assert get_number_of_characters("t6e") == 3
    assert get_number_of_characters("the ") == 3
    assert get_number_of_characters("t 'he") == 3

def get_number_of_spaces(text):
    '''Accepts a string 'text' and returns the number of spaces in the text string.'''
    number_of_spaces = text.count(' ')
    return number_of_spaces

def test_get_number_of_spaces():
    assert get_number_of_spaces('') == 0
    assert get_number_of_spaces('d') == 0
    assert get_number_of_spaces(' ') == 1
    assert get_number_of_spaces('a b ') == 2
    assert get_number_of_spaces('  4  ') == 4

def get_number_of_sentences(text):
    '''Accepts a string 'text' and returns the number of sentence-ending characters (.!?).'''
    sentence_count = 0
    for character in text:
        if character in ".!?":
            sentence_count += 1
    return sentence_count

def test_get_number_of_sentences():
    assert get_number_of_sentences('') == 0
    assert get_number_of_sentences('abc3') == 0
    assert get_number_of_sentences('a bc3.') == 1
    assert get_number_of_sentences('? 4 ') == 1
    assert get_number_of_sentences('a! bc3') == 1
    assert get_number_of_sentences('a! bc3?') == 2

def open_file_save_text_as_string_close_file(file, mode = 'r'):
    '''Open 'file', read contents, closes the 'file', and returns 'contents'.'''
    with open(file, mode) as the_file:
        contents = the_file.read()
    return contents

def test_open_file_save_text_as_string_close_file():
    assert open_file_save_text_as_string_close_file(r'.\data\empty_file.txt') == ''
    assert open_file_save_text_as_string_close_file(r'.\data\ten_char_file.txt') == '0123456789'
    assert open_file_save_text_as_string_close_file(r'.\data\three_sentence_three_space_file.txt') == 'this. is three. sentences.'

def write_contents_to_file(file, text, mode = 'w'):
    '''Open 'file' whether it exists or not, overwrite 'text' to 'file', close 'file'.'''
    with open(file, mode) as the_file:
        the_file.write(text)

def test_write_contents_to_file():
    write_contents_to_file(r".\data\write_file.txt", 'the text')
    time.sleep(.1)
    assert open_file_save_text_as_string_close_file(r".\data\write_file.txt") == 'the text'

    time.sleep(.1)

    write_contents_to_file(r".\data\write_file.txt", 'the new text')
    time.sleep(.1)
    assert open_file_save_text_as_string_close_file(r".\data\write_file.txt") == 'the new text'

def calculate_ari_of_text(characters, words, sentences):
    '''Accepts parameters: characters, words, and sentences. Returns the ARI for provided parameters.'''
    # Some conversion constants.
    FOUR_SEVEN_ONE = 4.71
    POINT_FIVE = .5
    TWO_ONE_POINT_FOUR_THREE = 21.43
    # ari = ((characters / words) * 4.71 + (words / sentences) * .5 - 21.43)
    ari = math.ceil((characters / words) * FOUR_SEVEN_ONE + (words / sentences) * POINT_FIVE - TWO_ONE_POINT_FOUR_THREE)
    return ari

def main():
    # Either style of slash works on my Windows PC.
    input_files = [r"./data/gettysburg_address_archive_org.txt", r"./data/gettysburg_address_umd_edu.txt", r"./data/medicine_info.txt"]
    # input_files = [r".\data\gettysburg_address_archive_org.txt", r".\data\gettysburg_address_umd_edu.txt", r".\data\medicine_info.txt"]

    # Modified since '”' not registering properly. Doesn't seem to register as 'double quote' '"'.
    # But seems to 'render' properly after replacing '”' with '"'.
    # input_files = [r"./data/gettysburg_address_archive_org.txt", r"./data/gettysburg_address_umd_edu.txt", r"./data/medicine_info.txt"]

    # As provided by Liz:
    # input_files = [r”./data/gettysburg_address_archive_org.txt”, r”./data/gettysburg_address_umd_edu.txt”, r”./data/medicine_info.txt”]

    # file_we_are_analyzing = "gettysburg_address_archive_org.txt"
    # file_we_are_analyzing = "gettysburg_address_umd_edu.txt"

    for file in input_files:
        the_text_we_have = open_file_save_text_as_string_close_file(file)
        characters = get_number_of_characters(the_text_we_have)
        words = get_number_of_spaces(the_text_we_have)
        sentences = get_number_of_sentences(the_text_we_have)
        the_ari = calculate_ari_of_text(characters, words, sentences)

        print(f'''
        ARI:        {the_ari}
        Filename:   {file}
        Recommended grade level is {ari_scale[the_ari]['grade_level']}.
        Suitable ages for reading are {ari_scale[the_ari]['ages']}.
        Characters: {characters}
        Words:      {words}
        Sentences:  {sentences}
        
        ''')


main()


