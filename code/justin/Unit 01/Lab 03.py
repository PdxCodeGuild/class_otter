# Full Stack Bootcamp - Unit 01 Lab 03
# Justin Hammond, 01/05/2022


# Convert a given number into its english representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.

small_number_names = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen' }

tens_place_names = {
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety' }

def convert_num_to_phrase(num):
    if num == 0:
        return 'zero'

    if num < 20:
        return small_number_names[num]

    result = ''
    if num > 99:
        hundreds_digit = num // 100
        result = f"{small_number_names[hundreds_digit]} hundred "
        num -= hundreds_digit * 100

    if num < 1:
        return result[:-1]
    elif num > 19:
        result += f"{tens_place_names[num // 10]}"
    else:
        return result + f"{small_number_names[num]}"

    ones_digit = num % 10

    if ones_digit != 0:
        result += f"-{small_number_names[ones_digit]}"
    
    return result

def test_convert_num_to_phrase():
    assert convert_num_to_phrase(0) == 'zero'
    assert convert_num_to_phrase(5) == 'five'
    assert convert_num_to_phrase(11) == 'eleven'
    assert convert_num_to_phrase(13) == 'thirteen'
    assert convert_num_to_phrase(45) == 'forty-five'
    assert convert_num_to_phrase(67) == 'sixty-seven'
    assert convert_num_to_phrase(99) == 'ninety-nine'
    assert convert_num_to_phrase(100) == 'one hundred'
    assert convert_num_to_phrase(101) == 'one hundred one'
    assert convert_num_to_phrase(337) == 'three hundred thirty-seven'
    assert convert_num_to_phrase(619) == 'six hundred nineteen'
    assert convert_num_to_phrase(811) == 'eight hundred eleven'
    assert convert_num_to_phrase(999) == 'nine hundred ninety-nine'