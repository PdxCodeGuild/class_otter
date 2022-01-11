

# Practice 4: Strings
# Copy and paste this file into your own "04_strings.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 04_strings.py"

# Loud Text
# Capitalize text and insert dashes between each letter

def loud_text(text):
    text_upper = text.upper()
    text_list = list(text_upper)
    result = '-'.join(text_list)
    return result

def test_loud_test():
    assert loud_text('hello') == 'H-E-L-L-O'
    assert loud_text('this is loud text') == 'T-H-I-S- -I-S- -L-O-U-D- -T-E-X-T'
    assert loud_text('the text here') == 'T-H-E- -T-E-X-T- -H-E-R-E'



# Double Letters
# Get a string from the user, print out another string, doubling every letter.

def double_letters(word):
    result = ''
    for character in word:
        result += 2 * character
    return result

def test_double_letters():
    assert double_letters('hello') == 'hheelllloo'
    assert double_letters('astring') == 'aassttrriinngg'
    assert double_letters('nada') == 'nnaaddaa'

# Count Letter
# Count the number of letter occurances in a string

def count_letter(letter, word):
    # return word.count(letter)
    result = 0
    for character in word:
        if character == letter:
            result += 1
    return result
        

def test_count_letter():
    assert count_letter('i', 'antidisestablishmentterianism') == 5
    assert count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis') == 2


# Latest Letter
# Return the letter that appears the latest in the english alphabet.

def latest_letter(word):
    word_list = list(word)
    word_list.sort()
    # We want the last letter in the list.
    return word_list[len(word_list) - 1]

def test_latest_letter():
    assert latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis') == 'v'
    assert latest_letter('poiwehrnsgdfoiuewth') == 'w'


# Count Hi
# Write a function that returns the number of occurances of 'hi' in a given string.

def count_hi(text):
    result = 0
    for i, character in enumerate(text):
        # Break out of loop at end so we don't have an index out of range.
        if i == len(text) - 1:
            break
        # Check if i follows an h.
        if character == 'h':
            if text[i + 1] == 'i':
                result += 1
    return result

def test_count_hi():
    assert count_hi('hihi') == 2
    assert count_hi('hello hi llama hill') == 2
    assert count_hi('hihi hh hillh') == 3


# Snake Case
# Write a function that converts text to snake case (all lowercase, underscores for spaces, no special characters).

def snake_case(text):
    with_spaces = ''
    text = text.lower()
    for character in text:
        if character.isalpha() or character == ' ':
            with_spaces += character
    no_spaces = with_spaces.replace(' ', '_')
    return no_spaces

def test_snake_case():
    assert snake_case('Hello World!') ==  'hello_world'
    assert snake_case('This is another example.') == 'this_is_another_example'
    assert snake_case('a different! string') == 'a_different_string'

# Camel Case
# Write a function that converts text to camel case (no spaces, no special characters, leading capitals except the first).

def camel_case(text):
    list_of_words = []
    working_object = []

    with_spaces = ''
    text = text.lower()
    for character in text:
        if character.isalpha() or character == ' ':
            with_spaces += character
    
    # Create list of words.
    list_of_words = with_spaces.split(' ')
    # Append the first word of the input to the working_object, since it's case wont be changed.
    working_object.append(list_of_words[0].lower())
    
    # Capitalize the first letter of the remaining words of input string.
    for index in range(1, len(list_of_words)):
        working_word = list_of_words[index].capitalize()
        # Add the caplitalized word to the the working_object.
        working_object.append(working_word)
    
    # Join the working_object list into a single string.
    result_string = ''.join(working_object)

    # Return the result string.
    return result_string

def test_camel_case():
    assert camel_case('Hello World!') == 'helloWorld'
    assert camel_case('This is another example.') == 'thisIsAnotherExample'
    assert camel_case('The assortment of words')

## Alternating Case
# Write a function that converts text to alternating case.

def alternating_case(text):
    result = ''
    for i, character in enumerate(text):
        if i == 0:
            result += character.upper()
        elif i % 2 == 1:
            result += character.lower()
        else:
            result += character.upper()
    return result
        
    ...

def test_alternating_case():
    assert alternating_case('Hello World!') ==  'HeLlO WoRlD!'
    assert alternating_case('This is another example.') == 'ThIs iS AnOtHeR ExAmPlE.'
