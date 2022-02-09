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

# TODO: Create version where D, L, and V are calculated like the the M, C, X, and I.

# Determine how many thousands (M).
number_of_thousands = input_number_as_integer // 1000
remainder = input_number_as_integer % 1000

# Determine how many hundreds (C), which might be combined with D, M, or X.
number_of_hundreds = remainder // 100
remainder = remainder % 100

# Determine how many tens (X), which might be combined with C, L or V.
number_of_tens = remainder // 10
remainder = remainder % 10

# Determine how many ones (I).
number_of_ones = remainder


print(f'''
Decimal:        {input_number_as_integer}
Thousands:      {number_of_thousands}
Hundreds:       {number_of_hundreds}
Tens:           {number_of_tens}
Ones:           {number_of_ones}
''')

# Dictionaries for mapping decimal to roman characters.
thousands = {
    4: "MMMM",
    3: "MMM",
    2: "MM",
    1: "M",
    0: ""
}

hundreds = {
    9: "CM",
    8: "DCCC",
    7: "DCC",
    6: "DC",
    5: "D",
    4: "CD",
    3: "CCC",
    2: "CC",
    1: "C",
    0: ""
}

tens = {
    9: "XC",
    8: "LXXX",
    7: "LXX",
    6: "LX",
    5: "L",
    4: "XL",
    3: "XXX",
    2: "XX",
    1: "X",
    0: ""
}

ones = {
    9: "IX",
    8: "VIII",
    7: "VII",
    6: "VI",
    5: "V",
    4: "IV",
    3: "III",
    2: "II",
    1: "I",
    0: ""
}

# Concatenate the roman characters.
result = f"{thousands[number_of_thousands]}{hundreds[number_of_hundreds]}{tens[number_of_tens]}{ones[number_of_ones]}"

# Display results.
print(f'''
Decimal:    {input_number_as_integer}
Roman:      {result}
''')