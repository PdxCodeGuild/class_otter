# ********************************* #
#   Lab 6: Credit Card Validation   #
#      Using List Comprehension     #
#            Version: 1.0           #
#        Author: Bruce Stull        #
#             2022-01-10            #
# ********************************* #

# Assignment
# https://github.com/PdxCodeGuild/class_otter/blob/bruce/1%20Python/labs/06%20Credit%20Card%20Validation.md

'''
Let's write a function which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:

1. Convert the input string into a list of ints
2. Slice off the last digit.  That is the **check digit**.
3. Reverse the digits.
4. Double every other element in the reversed list (starting with the first number in the list).
5. Subtract nine from numbers over nine.
6. Sum all values.
7. Take the second digit of that sum.
8. If that matches the check digit, the whole card number is valid.

Here is a valid credit card number to test with: 4556737586899855

For example, the worked out steps would be:

1. `4  5  5  6  7  3  7  5  8  6  8  9  9  8  5  5`
2. `4  5  5  6  7  3  7  5  8  6  8  9  9  8  5`
3. `5  8  9  9  8  6  8  5  7  3  7  6  5  5  4`
4. `10 8  18 9  16 6  16 5  14 3  14 6  10 5  8`
5. `1  8  9  9  7  6  7  5  5  3  5  6  1  5  8`
6. 85
7. 5
8. Valid!
'''

# TODO: Add exception handling for non-numeric input.
def convert_input_string_to_list_of_ints(string = ''):
    '''Accepts string of integers argument and returns list of the individual integers.'''
    return [int(character) for character in string]

def test_convert_input_string_to_list_of_ints():
    assert convert_input_string_to_list_of_ints() == []
    assert convert_input_string_to_list_of_ints('101') == [1,0,1]
    assert convert_input_string_to_list_of_ints('1010') == [1,0,1,0]
    assert convert_input_string_to_list_of_ints('202') == [2,0,2]
    assert convert_input_string_to_list_of_ints('4556737586899855') == [4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5, 5]

def remove_and_save_last_digit_of_list(nums = []):
    '''Accepts list of integers. Returns both the last integer and the remaining list with last element removed.'''
    try:
        check_digit = nums.pop(-1)
        return check_digit, nums
    except IndexError:
        check_digit = 0
        return check_digit, nums

def test_remove_and_save_last_digit_of_list():
    assert remove_and_save_last_digit_of_list() == (0, [])
    assert remove_and_save_last_digit_of_list([1,2,3]) == (3, [1,2])
    assert remove_and_save_last_digit_of_list([4,5,6]) == (6, [4,5])

def reverse_digits(nums = []):
    # nums.reverse()
    # [::-1]
    nums = nums[::-1]
    return nums

def test_reverse_digit():
    assert reverse_digits([1,2,3]) == [3,2,1]
    assert reverse_digits([2,3,4]) == [4,3,2]
    assert reverse_digits(['a','b','c']) == ['c', 'b', 'a']
    assert reverse_digits() == []

def double_every_other(nums = []):
    
    # Execute the statement (num * 2 if i % 2 == 0 else num) for each i, num in enumerate(nums)
    return [(num * 2 if i % 2 == 0 else num) for i, num in enumerate(nums)]
    
    # Multiply every other number, starting at '0', by 2.
    # for i in range(0, len(nums), 2):
    #     nums[i] *= 2
    # return nums

    # nums[i]
    # return [(nums[i] * 2 if i % 2 == 0 else nums[i]) for i, num in enumerate(nums)] # Works as needed but I prefer above method.

def test_double_every_other():
    assert double_every_other() == []
    assert double_every_other([1,2,3,4]) == [2,2,6,4]
    assert double_every_other([4,5,6,7]) == [8,5,12,7]

def reduce_by_nine(nums):
    return [(num - 9 if num > 9 else num) for num in nums]

def test_reduce_by_nine():
    assert reduce_by_nine([11,5,15,4]) == [2,5,6,4]
    assert reduce_by_nine([3,19,5,13]) == [3,10,5,4]

def sum_all_elements(nums = []):
    # reduce()
    return sum(nums)

def test_sum_all_elements():
    assert sum_all_elements() == 0
    assert sum_all_elements([1,2,3]) == 6
    assert sum_all_elements([4,5,6]) == 15

def return_ones_digit(num = 0):
    try:
        # Previous method: Used num_as_string = str(num) >> num_as_string = str(num) >> return int(ones_digit) before.
        return num % 10
    except TypeError:
        return 0

def test_return_ones_digit():
    assert return_ones_digit() == 0
    assert return_ones_digit(123) == 3
    assert return_ones_digit(456) == 6
    assert return_ones_digit('g') == 0
    assert return_ones_digit(111) == 1

def compare_check_digit(check_digit,ones_digit):
    return check_digit == ones_digit

def test_compare_check_digit():
    assert compare_check_digit(1,1) == True
    assert compare_check_digit(2,3) == False

def card_valid(card):
    '''Returns True for valid card number. Otherwise, returns False.'''
    list_of_ints = convert_input_string_to_list_of_ints(card)
    check_digit, nums = remove_and_save_last_digit_of_list(list_of_ints)
    nums_reversed = reverse_digits(nums)
    doubled_nums = double_every_other(nums_reversed)
    reduced_numbers = reduce_by_nine(doubled_nums)
    sum_of_elements = sum_all_elements(reduced_numbers)
    returned_ones_digit = return_ones_digit(sum_of_elements)
    result = compare_check_digit(check_digit,returned_ones_digit)
    return result


def main():
    # card = input("Please enter card number: ")
    valid_card = "4556737586899855"
    test_invalid_card_01 = "4556737585899855"
    test_invalid_card_01 = "4656737586899855"
    
    is_card_valid = card_valid(valid_card)
    print(is_card_valid)

main()