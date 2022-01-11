# Full Stack Bootcamp - Unit 01 Lab 06
# Justin Hammond, 01/06/2022


'''
Write a function which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:

    Convert the input string into a list of ints
    Slice off the last digit. That is the check digit.
    Reverse the digits.
    Double every other element in the reversed list (starting with the first number in the list).
    Subtract nine from numbers over nine.
    Sum all values.
    Take the second digit of that sum.
    If that matches the check digit, the whole card number is valid.

Here is a valid credit card number to test with: 4556737586899855

For example, the worked out steps would be:

    4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
    4 5 5 6 7 3 7 5 8 6 8 9 9 8 5
    5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
    10 8 18 9 16 6 16 5 14 3 14 6 10 5 8
    1 8 9 9 7 6 7 5 5 3 5 6 1 5 8
    85
    5
    Valid!
'''

def convert_to_int_list(int_string):
    results = []
    if int_string.isdigit():
        for character in int_string:
            results.append(int(character))
        return results
    else:
        return None

def test_convert_to_int_list():
    assert convert_to_int_list('4556737586899855') == [4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5, 5]
    assert convert_to_int_list('4556737.586899855') == None
    assert convert_to_int_list('HeLlO WoRlD!') == None
    assert convert_to_int_list('1234567890123456') == [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6]

def slice_check_digit(number_list):
    check_digit = number_list[len(number_list) - 1]
    return check_digit, number_list[:-1]

def test_slice_check_digit():
    number_list = [4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5, 5]
    check_digit, number_list = slice_check_digit(number_list)

    assert check_digit == 5
    assert number_list == [4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5]

def double_even_elements(number_list):
    for index in range(len(number_list)):
        if index % 2 == 0:
            number_list[index] *= 2
    return number_list

def test_double_even_elements():
    assert double_even_elements([5, 8, 9, 9, 8, 6, 8, 5, 7, 3, 7, 6, 5, 5, 4]) == [10, 8, 18, 9, 16, 6, 16, 5, 14, 3, 14, 6, 10, 5, 8]
    
def reduce_to_single_digits(number_list):
    for index in range(len(number_list)):
        if number_list[index] > 9:
            number_list[index] -= 9
    return number_list

def test_reduce_to_single_digits():
    assert reduce_to_single_digits([10, 8, 18, 9, 16, 6, 16, 5, 14, 3, 14, 6, 10, 5, 8]) == [1, 8, 9, 9, 7, 6, 7, 5, 5, 3, 5, 6, 1, 5, 8]
    
def validate_sum(sum, check_digit):
    if sum > 99:
        sum = int(sum / 10)

    digit_to_validate = sum % 10

    return digit_to_validate == check_digit

def test_validate_sum():
    assert validate_sum(85, 5) == True
    assert validate_sum(99, 9) == True
    assert validate_sum(61, 1) == True
    assert validate_sum(37, 7) == True
    assert validate_sum(94, 4) == True
    assert validate_sum(135, 3) == True
    assert validate_sum(101, 0) == True
    assert validate_sum(165, 6) == True


def main():
    number_to_validate = '4556737586899855'

    numbers_as_list = convert_to_int_list(number_to_validate)
    check_digit, numbers_as_list = slice_check_digit(numbers_as_list)
    numbers_as_list.reverse()
    numbers_as_list = double_even_elements(numbers_as_list)
    numbers_as_list = reduce_to_single_digits(numbers_as_list)
    number_list_sum = sum(numbers_as_list)

    print(f"{number_to_validate} is {'valid!' if validate_sum(number_list_sum, check_digit) else 'invalid.'}")

main()



