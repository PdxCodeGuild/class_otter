# **************************** #
#       Learning Slicing       #
#   square brackets and such   #
#         Version: 0.0         #
#     Author: Bruce Stull      #
#          2022-01-17          #
# **************************** #

def reverse_the_input(the_input = ''):
    '''Accepts single argument. Converts argument to string and returns the reversed string.'''
    the_input_as_string = str(the_input)
    result = the_input_as_string[::-1]
    return result

def test_reverse_the_input():
    assert reverse_the_input() == ''
    assert reverse_the_input(1100) == '0011'
    assert reverse_the_input('abc') == 'cba'
    assert reverse_the_input('a23') == '32a'

def remove_last_character(the_input = ''):
    '''Accepts single argument. Converts argument to string, removes the last character, and returns result.'''
    the_input_as_string = str(the_input)
    result = the_input_as_string[:-1]
    return result

def test_remove_last_character():
    assert remove_last_character() == ''
    assert remove_last_character(10) == '1'
    assert remove_last_character(100) == '10'
    assert remove_last_character('abcd') == 'abc'

def return_last_character(the_input = ''):
    '''Converts 'the_input' to string and returns the last character.'''
    the_input_as_string = str(the_input)
    result = the_input_as_string[-1::]
    return result

def test_return_last_character():
    assert return_last_character() == ''
    assert return_last_character(1) == '1'
    assert return_last_character('q') == 'q'
    assert return_last_character(1234) == '4'
    assert return_last_character('abcd') == 'd'

def return_first_three_reversed(the_input = ''):
    '''Accepts one argument. Converts the_input to string and returns the first three characters in reversed order.'''
    the_input_as_string = str(the_input)
    result = the_input_as_string[2::-1]
    return result
    
def test_return_first_three_reversed():
    assert return_first_three_reversed() == ''
    assert return_first_three_reversed('a') == 'a'
    assert return_first_three_reversed('bad') == 'dab'
    assert return_first_three_reversed('abcd') == 'cba'
    assert return_first_three_reversed(1001) == '001'
    assert return_first_three_reversed(1234) == '321'

def return_second(the_input = ''):
    '''Returns the second character.'''
    the_input_as_string = str(the_input)
    result = the_input_as_string[1:2]
    return result

def test_return_second():
    assert return_second() == ''
    assert return_second('a') == ''
    assert return_second(1) == ''
    assert return_second('ab') == 'b'
    assert return_second(12) == '2'
    assert return_second('abc') == 'b'
    assert return_second('abcd') == 'b'
    assert return_second(123) == '2'
    assert return_second(1234) == '2'

def return_second_to_last(the_input = ''):
    '''Accepts single argument. Converts the_input to string and returns the second to last character of input string.'''
    the_input_as_string = str(the_input)
    # result = the_input_as_string[len(the_input_as_string) - 2:len(the_input_as_string) - 1]
    result = the_input_as_string[-2:-1]
    return result

def test_return_second_to_last():
    assert return_second_to_last() == ''
    assert return_second_to_last('a') == ''
    assert return_second_to_last('ab') == 'a'
    assert return_second_to_last('abcde') == 'd'
    assert return_second_to_last(123456) == '5'
    assert return_second_to_last(1) == ''
    assert return_second_to_last(21) == '2'
    assert return_second_to_last(10) == '1'

def return_last_three_reversed(the_input = ''):
    '''Returns the last three characters in reversed order.'''
    the_input_as_string = str(the_input)
    result = the_input_as_string[-1:-4:-1]
    return result    

def test_return_last_three_reversed():
    assert return_last_three_reversed() ==''
    assert return_last_three_reversed('a') =='a'
    assert return_last_three_reversed(1) =='1'
    assert return_last_three_reversed('ab') =='ba'
    assert return_last_three_reversed(10) =='01'
    assert return_last_three_reversed('abcd') =='dcb'
    assert return_last_three_reversed(1234) =='432'

def remove_first_character(the_input = ''):
    the_input_as_string = str(the_input)
    result = the_input_as_string[1::1]
    return result    

def test_remove_first_character():
    assert remove_first_character() == ''
    assert remove_first_character('a') == ''
    assert remove_first_character(1) == ''
    assert remove_first_character('ab') == 'b'
    assert remove_first_character(12) == '2'
    assert remove_first_character('abcd') == 'bcd'

# Create a string to work with.
the_string = 'abcdefghij'

print_tests = True

if print_tests:
    print(f"Printing the tests on '{the_string}':")
    # Whole string:
    print(f"Whole string - the_string[:]: {the_string[:]}")

    # Get whole string:
    print(f"Whole string - the_string[:len(the_string)]: {the_string[:len(the_string)]}") # abcdefghij

    # Get whole string:
    print(f"Whole string - the_string[-len(the_string)::1]: {the_string[-len(the_string)::1]}")  # abcdefghij
    print(f"Returns last character since start is -1 - the_string[-1::1]: {the_string[-1::1]}")  # j

    # Print last character:
    print(f"Last character - the_string[-1::]: {the_string[-1::]}")

    # Remove last character:
    print(f"Remove last character - the_string[:-1]: {the_string[:-1]}")

    # Remove last two characters:
    print(f"Remove last two characters - the_string[:-2]: {the_string[:-2]}")

    # Get first three characters:
    print(f"First three characters - the_string[0:3]: {the_string[0:3]}")

    # # Get and reverse the first three characters:
    # print(the_string[3:0:-1])   # dcb

    # Reverse whole string:
    print(f"Reverse whole string - the_string[len(the_string)::-1]: {the_string[len(the_string)::-1]}")  # jihgfedcba

    # Get first three characters:
    print(f"First three characters - the_string[0:3]: {the_string[0:3]}")  # abc

    # Trying to figure out how to get last three characters reversed.
    print(f"Trying to reverse first three - the_string[3:0:-1]: {the_string[3:0:-1]}")  # dcb

    # Get and return the reverse of first three characters:
    print(f"Trying to reverse first three, returns empty string - the_string[2:-1:-1]: {the_string[2:-1:-1]}")  # <nothing>
    # Need to use an empty stop argument.
    print(f"Trying to reverse first three, Use empty stop argument to reverse and return first three - the_string[2::-1]: {the_string[2::-1]}")  # cba
    
    # Experimenting with switching start/stop from above.
    # print(f"Trying to reverse first three, Should return empty string: {the_string[:2:-1]}")
    print(f": {the_string[:2:-1]}")
    
    # Not sure how/why this works this way.
    print(f"Returns the reversed of fourth to end - the_string[:2:-1]: {the_string[:2:-1]}")


    print(f"Returns empty string since arguments don't make sense - the_string[0:2:-1]: '{the_string[0:2:-1]}' {type(the_string[0:2:-1])}")

else:
    print("Tests not printed.")

