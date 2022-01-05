# *********************** #
#     Number to Phrase    #
#      Roman Numerals     #
#       Version: 3.0      #
#   Author: Bruce Stull   #
#        2022-01-05       #
# *********************** #

# Assignment:
# https://github.com/PdxCodeGuild/class_otter/blob/main/1%20Python/labs/03%20Number%20To%20Phrase.md

# Roman numeral resource:
# https://www.britannica.com/topic/Roman-numeral
# Calculator:
# https://www.calculatorsoup.com/calculators/conversions/roman-numeral-converter.php

# Examples:
# MMMM      :   4000
# MMMCMXCIX :   3999

# Use 'while' loop to prompt user and verify input is usable.
while True:
    # Prompt user for input number.
    input_number_as_string = input("Please enter integer number (1 - 3999) to be converted to roman numerals: ")
    # If input is non-numeric:
    if not input_number_as_string.isnumeric() or int(input_number_as_string) > 3999 or int(input_number_as_string) < 1:
        print("Please enter an integer numeric value between 1 and 3999.")
        continue
    # Othewise, input is numeric so convert or round to integer.
    else:
        input_number_as_integer = int(input_number_as_string)
        break

print(f'''
Input string: {input_number_as_string} {type(input_number_as_string)}
Input integer: {input_number_as_integer} {type(input_number_as_integer)}
''')

# Determine how many thousands (M).
number_of_thousands = input_number_as_integer // 1000
remainder = input_number_as_integer % 1000

# # Determine how many five_hundreds (D).
# number_of_five_hundreds = remainder // 500
# remainder = remainder % 500

# Determine how many hundreds (C).
number_of_hundreds = remainder // 100
remainder = remainder % 100

# # Determine how many fifties (L).
# number_of_fifties = remainder // 50
# remainder = remainder % 50

# Determine how many tens (X).
number_of_tens = remainder // 10
remainder = remainder % 10

# # Determine how many fives (V).
# number_of_fives = remainder // 5
# remainder = remainder % 5

# Determine how many ones (I).
number_of_ones = remainder


print(f'''
Decimal:        {input_number_as_integer}
Thousands:      {number_of_thousands}
Five_Hundreds:  {'number_of_five_hundreds'}
Hundreds:       {number_of_hundreds}
Fifties:        {'number_of_fifties'}
Tens:           {number_of_tens}
Fives:          {'number_of_fives'}
Ones:           {number_of_ones}
''')

result = ''

# Add Thousands.
if number_of_thousands == 4:
    result += "MMMM"
elif number_of_thousands == 3:
    result += "MMM"
elif number_of_thousands == 2:
    result += "MM"
elif number_of_thousands == 1:
    result += "M"

# # Add Five_Hundreds.
# if number_of_five_hundreds == 1:
#     result += "D"

# Add Hundreds.
if number_of_hundreds == 9:
    result += "CM"
elif number_of_hundreds == 8:
    result += "DCCC"
elif number_of_hundreds == 7:
    result += "DCC"
elif number_of_hundreds == 6:
    result += "DC"
elif number_of_hundreds == 5:
    result += "D"
elif number_of_hundreds == 4:
    result += "CD"
elif number_of_hundreds == 3:
    result += "CCC"
elif number_of_hundreds == 2:
    result += "CC"
elif number_of_hundreds == 1:
    result += "C"

# # Add Fifties.
# if number_of_fifties == 1:
#     result += "L"

# Add Tens.
if number_of_tens == 9:
    result += "XC"
elif number_of_tens == 8:
    result += "LXXX"
elif number_of_tens == 7:
    result += "LXX"
elif number_of_tens == 6:
    result += "LX"
elif number_of_tens == 5:
    result += "L"
elif number_of_tens == 4:
    result += "XL"
elif number_of_tens == 3:
    result += "XXX"
elif number_of_tens == 2:
    result += "XX"
elif number_of_tens == 1:
    result += "X"

# # Add Fives.
# if number_of_fives == 1:
#     result += "V"

# Add Ones.
if number_of_ones == 9:
    result += "IX"
elif number_of_ones == 8:
    result += "VIII"
elif number_of_ones == 7:
    result += "VII"
elif number_of_ones == 6:
    result += "VI"
elif number_of_ones == 5:
    result += "V"
elif number_of_ones == 4:
    result += "IV"
elif number_of_ones == 3:
    result += "III"
elif number_of_ones == 2:
    result += "II"
elif number_of_ones == 1:
    result += "I"


print(f'''
Decimal:    {input_number_as_integer}
Roman:      {result}
''')