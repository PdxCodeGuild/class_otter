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

units_roman_numeral = {
    0: '',
    1: 'I',
    2: 'II',
    3: 'III',
    4: 'IV',
    5: 'V',
    6: 'VI',
    7: 'VII',
    8: 'VIII',
    9: 'IX' }

tens_roman_numeral = {
    0: '',
    1: 'X',
    2: 'XX',
    3: 'XXX',
    4: 'XL',
    5: 'L',
    6: 'LX',
    7: 'LXX',
    8: 'LXXX',
    9: 'XC' }

hundreds_roman_numeral = {
    0: '',
    1: 'C',
    2: 'CC',
    3: 'CCC',
    4: 'CD',
    5: 'D',
    6: 'DC',
    7: 'DCC',
    8: 'DCCC',
    9: 'CM' }


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


def convert_num_to_roman_numeral(num):
    hundreds_digit = num // 100
    tens_digit = (num - (hundreds_digit * 100)) // 10
    units_digit = num % 10

    return f"{hundreds_roman_numeral[hundreds_digit]}{tens_roman_numeral[tens_digit]}{units_roman_numeral[units_digit]}"

def test_convert_num_to_roman_numeral():
    assert convert_num_to_roman_numeral(4) == "IV"
    assert convert_num_to_roman_numeral(5) == "V"
    assert convert_num_to_roman_numeral(6) == "VI"
    assert convert_num_to_roman_numeral(9) == "IX"
    assert convert_num_to_roman_numeral(10) == "X"
    assert convert_num_to_roman_numeral(39) == "XXXIX"
    assert convert_num_to_roman_numeral(160) == "CLX"
    assert convert_num_to_roman_numeral(207) == "CCVII"
    assert convert_num_to_roman_numeral(246) == "CCXLVI"
    assert convert_num_to_roman_numeral(789) == "DCCLXXXIX"
    assert convert_num_to_roman_numeral(999) == "CMXCIX"


def convert_time_to_phrase(time):
    time_values = time.split(":")
    hours = int(time_values[0])
    minutes = int(time_values[1])
    
    result = convert_num_to_phrase(hours)

    if minutes == 0:
        result += " o'clock"
    else:
        result += f" {convert_num_to_phrase(minutes)}"

    return result


def test_convert_time_to_phrase():
    assert convert_time_to_phrase("12:00") == "twelve o'clock"
    assert convert_time_to_phrase("1:37") == "one thirty-seven"
    assert convert_time_to_phrase("9:59") == "nine fifty-nine"
