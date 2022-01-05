# *********************** #
#     Number to Phrase    #
#      Roman Numerals     #
#       Version: 3.0      #
#   Author: Bruce Stull   #
#        2022-01-05       #
# *********************** #

# Assignment:
# https://github.com/PdxCodeGuild/class_otter/blob/main/1%20Python/labs/03%20Number%20To%20Phrase.md

# Use 'while' loop to prompt user and verify input is usable.
while True:
    # Prompt user for input number.
    input_number_as_string = input("Please enter integer number (1 - 999) to be converted to raman numerals: ")
    # If input is non-numeric:
    if not input_number_as_string.isnumeric():
        print("Please enter an integer numeric value.")
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

# Determine how many five_hundreds (D).
number_of_five_hundreds = remainder // 500
remainder = remainder % 500

# Determine how many hundreds (C).
number_of_hundreds = remainder // 100
remainder = remainder % 100

# Determine how many fifties (L).
number_of_fifties = remainder // 50
remainder = remainder % 50

# Determine how many tens (X).
number_of_tens = remainder // 10
remainder = remainder % 10

# Determine how many fives (V).
number_of_fives = remainder // 5
remainder = remainder % 5

# Determine how many ones (I).
number_of_ones = remainder


print(f'''
Decimal:        {input_number_as_integer}
Thousands:      {number_of_thousands}
Five_Hundreds:  {number_of_five_hundreds}
Hundreds:       {number_of_hundreds}
Fifties:        {number_of_fifties}
Tens:           {number_of_tens}
Fives:          {number_of_fives}
Remainder:      {number_of_ones}
''')