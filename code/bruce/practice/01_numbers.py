
# Practice 1: Numbers & Arithmetic
# Copy and paste this file into your own "01_numbers.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 01_numbers.py"

# Is Even
# Write a function returns whether a number is even or odd (hint, compare a/2 and a//2, or use a%2)

def is_even(a):
    '''Returns True when argument is even and returns False otherwise.'''
    # put some logic here and make it 'result'.
    # We have to use the parameter 'as' somewhere in this logic.
    # If a is even == True
    # list_of_evens = [0, 2, 4, 6, 8, 10, 12, 14]
    # Cycles through list_of_evens.
    # for even_number in list_of_evens:
    #     # Compares the input value 'a' to even_number.
    #     if a == even_number:
    #         # We KNOW KNOW KNOW that a is even.
    #         # How can we make is so 'result' = True
    #         result = True
    #     elif a != even_number:
    #         result = False
    # WE have a list of evens.
    # Lets pick another way to see if a is in list_of_evens.
    if a % 2 == 0:
        # We KNOW KNOW KNOW that 'a' is even.
        print(a)
        print(a % 2)
        print(a % 2 == 0)
        # print(f'This is even: {a}')
        result = True
    elif a % 2 != 0:
        result = False
    return result

the_number = 6
the_result_is = is_even(the_number)
# print(the_result_is)

# print(is_even(57))




def test_is_even():
    assert is_even(5) == False
    assert is_even(6) == True
    assert is_even(11) == False
    assert is_even(6) == True
    assert is_even(19) == False
    assert is_even(30) == True
    assert is_even(5344) == True
    assert is_even(5001) == False

# Ones Digit
# Write a function that returns the ones digit of a number

def ones_digit(num):
    '''Returns the ones digit of a provided integer argument greater than 0.'''
    if num < 1:
        return False
    if num < 10:
        return num
    # Let's use string methods. Twil be a bit more verbose but so much more fun.
    else:
        return int((str(num))[len(str(num))-1])

def test_ones_digit():
    assert ones_digit(3) == 3
    assert ones_digit(56) == 6
    assert ones_digit(812) == 2
    assert ones_digit(9715) == 5


# Percentage
# Write a function that takes two integers, a value and a maximum, and returns a string representing the percentage as an integer

def percentage(v, max):
    result = float(v / max) * 100
    return f"{round(result)}%"

def test_precentage():
    assert percentage(1, 10) == '10%'
    assert percentage(600, 1200) == '50%'
    assert percentage(1, 3) == '33%'


