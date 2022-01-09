# ********************************************* #
#         Test Backspace \n in Printout         #
#   See if we can delete characters in output   #
#                  Version: 1.0                 #
#              Author: Bruce Stull              #
#                   2022-01-09                  #
# ********************************************* #

# Import 'time' to use 'sleep()' later.
import time
# Import 'random' to use 'randint()' later.
import random

def generate_random_time_delay(time = .5, low = 0, hi = 10):
    '''Generates a random value between 0/10 and 10/10 of time.'''
    return time * (random.randint(low, hi) / 10)

def test_generate_random_time_delay():
    # generate_random_time_delay(), with no arguments, should be between 0 and .5.
    assert 0 <= generate_random_time_delay() <= .5
    assert .5 <= generate_random_time_delay(1, 5, 10) <= 1
    # generate_random_time_delay(1, 5, 10) should not be between 0 and .49.
    assert not 0 <= generate_random_time_delay(1, 5, 10) <= .49
    # generate_random_time_delay(1, 0, 5) should not be between .51 and 1.
    assert not .51 <= generate_random_time_delay(1, 0, 5) <= 1

def generate_random_index(string = ''):
    '''Generates random index value between 0 and len(string) - 1. Needs import of 'random' module.'''
    if string == '':
        return 0
    return random.randint(0, len(string) - 1)
    # return random.choice(range(len(string)))

def test_generate_random_index():
    # Empty string argument should return 0.
    assert generate_random_index('') == 0
    # Argument string of length 3 should return number between 0 inclusive and 2 inclusive.
    assert 0 <= generate_random_index('abc') <= 2
    # generate_random_index('abc') should not be greater than or equal to 3.
    assert not 3 <= generate_random_index('abc')
    # generate_random_index('abc') should not be less than 0.
    assert not generate_random_index('abc') < 0
    # generate_random_index('abcdef') should be between 0 inclusive and 5 inclusive.
    assert 0 <= generate_random_index('abcdef') <= 5
    # generate_random_index('abcdef') should not be greater than or equal to 6 inclusive.
    assert not 6 <= generate_random_index('abcdef')

def main():

    # TODO: Break these operations out into functions.
    print_string = "abcdefghijk"
    # Use for loop to put time delay in between printing characters.
    for i, character in enumerate(print_string):
        # Create random time delay value.
        # This can be used to simulate real typing.
        random_time_delay = generate_random_time_delay()
        # NOTE: Need the "end='', flush=True".
        print(character, end='', flush=True)
        time.sleep(random_time_delay)
        # Loop to add a randomly-placed delete of character and replace with '?'.
        if i == generate_random_index(print_string):
            print('\b', end='', flush=True)
            time.sleep(random_time_delay)
            print('?', end='', flush=True)
            time.sleep(random_time_delay)

main()