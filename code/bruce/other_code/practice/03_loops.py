

# Practice 3: While and For Loops
# Copy and paste this file into your own "03_loops.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 03_loops.py"

# Double Numbers
# Write a function that takes a list of numbers and returns a new list with every number doubled

def double_numbers(nums):
    result = []
    for number in nums:
        result.append(2 * number)
    return result

def test_double_numbers():
    assert double_numbers([1, 2, 3]) == [2, 4, 6]
    assert double_numbers([3, 6, 25]) == [6, 12, 50]
    assert double_numbers([1, 7, 13]) == [2, 14, 26]


# Stars
# Write a function that takes an integer and returns that number of asterisks in a string

def stars(n):
    result = n * '*'
    return result

def test_stars():
    assert stars(1) == '*'
    assert stars(2) == '**'
    assert stars(3) == '***'
    assert stars(4) == '****'
    assert stars(8) == '********'


# Extract Less Than Ten
# Write a function to move all the elements of a list with value less than 10 to a new list and return it.

def extract_less_than_ten(nums):
    result = []
    for number in nums:
        if number < 10:
            result.append(number)
    return result

def test_extract_less_than_ten():
    assert extract_less_than_ten([2, 8, 12, 18]) == [2, 8]
    assert extract_less_than_ten([6, 11, 37, 3, 7]) == [6, 3, 7]
    assert extract_less_than_ten([4, 9, 13, 2, 41]) == [4, 9, 2]



