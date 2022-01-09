# ********************************************* #
#         Test Backspace \n in Printout         #
#   See if we can delete characters in output   #
#                  Version: 1.0                 #
#              Author: Bruce Stull              #
#                   2022-01-09                  #
# ********************************************* #

import time
import random

# # Print a string with "end=''".
# print('first string', end='')

# # Print a string with '\b'.
# print('\bnext string')

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
    assert generate_random_index('') == 0
    assert 0 <= generate_random_index('abc') <= 2
    assert not 3 < generate_random_index('abc')
    assert not generate_random_index('abc') < 0
    assert 0 <= generate_random_index('abcdef') <= 5
    assert not 6 < generate_random_index('abcdef')

def main():

    # TODO: Break these operations out into functions.
    # to see if we can print a '\b' and replace the letter with different character.
    print_string = "abcdefghijk"
    # Use this when we want consistent time delay.
    # time_delay = .25
    # Create random int variable to be used for backspace position.
    # random_i = random.randint(0, len(print_string))
    # random_i = generate_random_index(print_string)
    # Use for loop to put time delay in between printing characters
    for i, character in enumerate(print_string):
        # Create random time delay value.
        # This can be used to simulate real typing.
        random_time_delay = generate_random_time_delay()
        # NOTE: Need the "end='', flush=True".
        print(character, end='', flush=True)
        time.sleep(random_time_delay)
        # Randomly print '\b' and '?'.
        # The effect is to backspace and replace a character with '?'.
        # This effect will not occur if current i is greater than generate_random_index(print_string).
        if i == generate_random_index(print_string):
            print('\b', end='', flush=True)
            time.sleep(random_time_delay)
            print('?', end='', flush=True)
            time.sleep(random_time_delay)
    
    # # This loop only moved the cursor and doesn't delete any characters.
    # for character in "\b\b\b":
    #     print(character, end='', flush=True)
    #     time.sleep(.1)
    
    # # This loop replaces the character, at the current position, with a space.
    # for character in "\b":
    #     print(character, end=' ', flush=True)
    #     time.sleep(.1)

main()