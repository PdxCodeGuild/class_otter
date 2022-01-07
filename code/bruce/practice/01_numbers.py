
# Practice 1: Numbers & Arithmetic
# Copy and paste this file into your own "01_numbers.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 01_numbers.py"

# Is Even
# Write a function returns whether a number is even or odd (hint, compare a/2 and a//2, or use a%2)

def is_even(a):
    '''Returns True when argument is even and returns False otherwise.'''
    # How do we tell if an integer is even?
    # We divide a by 2 and remainder is 0 if a is even.
    # a % 2 == 0
    result = a % 2 == 0
    return result

def test_is_even():
    assert is_even(5) == False
    assert is_even(6) == True
    assert is_even(11) == False
    assert is_even(6) == True
    assert is_even(19) == False

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


