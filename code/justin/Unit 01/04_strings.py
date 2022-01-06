# Full Stack Bootcamp - Unit 01 Practice 04
# Justin Hammond, 01/04/2022


# Practice 4: Strings
# Copy and paste this file into your own "04_strings.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 04_strings.py"

# Loud Text
# Capitalize text and insert dashes between each letter

def loud_text(text):
    text = text.upper()

    result = ''
    for letter in text:
        result += letter + '-'

    return result[:len(result) - 1]

def test_loud_test():
    assert loud_text('hello') == 'H-E-L-L-O'
    assert loud_text('this is loud text') == 'T-H-I-S- -I-S- -L-O-U-D- -T-E-X-T'


# Double Letters
# Get a string from the user, print out another string, doubling every letter.

def double_letters(word):
    result = ''
    for letter in word:
        result += letter * 2

    return result

def test_double_letters():
    assert double_letters('hello') == 'hheelllloo'

# Count Letter
# Count the number of letter occurances in a string

def count_letter(letter, word):
    count = 0
    for current_letter in word:
        if current_letter == letter:
            count += 1
    return count

def test_count_letter():
    assert count_letter('i', 'antidisestablishmentterianism') == 5
    assert count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis') == 2


# Latest Letter
# Return the letter that appears the latest in the english alphabet.

def latest_letter(word):
    latest_value = -1
    word = word.lower()
    for letter in word:
        letter_value = ord(letter)
        latest_value = letter_value if letter_value > latest_value else latest_value

    return chr(latest_value)

def test_latest_letter():
    assert latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis') == 'v'


# Count Hi
# Write a function that returns the number of occurances of 'hi' in a given string.

def count_hi(text):
    return text.count('hi')

def test_count_hi():
    assert count_hi('hihi') == 2
    assert count_hi('hello hi llama hill') == 2


# Snake Case
# Write a function that converts text to snake case (all lowercase, underscores for spaces, no special characters).

def snake_case(text):
    result = ''
    word_list = text.lower().split(' ')
    for word in word_list:
        result += ''.join(letter for letter in word if letter.isalnum()) + '_'

    return result[:len(result) - 1]

def test_snake_case():
    assert snake_case('Hello World!') ==  'hello_world'
    assert snake_case('This is another example.') == 'this_is_another_example'

# Camel Case
# Write a function that converts text to camel case (no spaces, no special characters, leading capitals except the first).

def camel_case(text):
    result = ''
    word_list = text.split(' ')
    word_count = 0
    for word in word_list:
        if word_count == 0:
            result += ''.join(letter for letter in word.lower() if letter.isalnum())
        else:
            result += ''.join(letter for letter in word.capitalize() if letter.isalnum())
        word_count += 1
        

    return result

def test_camel_case():
    assert camel_case('Hello World!') == 'helloWorld'
    assert camel_case('This is another example.') == 'thisIsAnotherExample'

## Alternating Case
# Write a function that converts text to alternating case.

def alternating_case(text):
    result = ''
    letter_count = 0
    for letter in text:
        if letter_count % 2 == 0:
            result += letter.upper()
        else:
            result += letter.lower()
        letter_count += 1

    return result
    

def test_alternating_case():
    assert alternating_case('Hello World!') ==  'HeLlO WoRlD!'
    assert alternating_case('This is another example.') == 'ThIs iS AnOtHeR ExAmPlE.'