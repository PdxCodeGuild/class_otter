# *********************** #
#   Author: Bruce Stull   #
#     Number to Phrase    #
#       Version: 2.0      #
#        2022-01-05       #
# *********************** #

# Assignment:
# https://github.com/PdxCodeGuild/class_otter/blob/main/1%20Python/labs/03%20Number%20To%20Phrase.md
# Convert a given number into its english representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-999.

# Use 'while' loop to prompt user and verify input is usable.
while True:
    # Prompt user for input number.
    input_number_as_string = input("Please enter integer number (0 - 999) to be converted to words: ")
    # If input is non-numeric:
    if not input_number_as_string.isnumeric():
        print("Please enter an integer numeric value.")
        continue
    # Othewise, input is numeric so convert or round to integer.
    else:
        input_number_as_integer = int(input_number_as_string)
        break

## This dictionary not needed. Leaving it here so I can see later why it's not used.
# # Dictionary to map 'hundreds' place numbers to word form.
# # NOTE: TODO: May just need to concatenate 'Hundred' onto the end for these and not need separate dictionary.
# # Dictionary seems to be same/similar to 'ones' dictionary.
# hundreds_dict = {
#     9   : "Nine Hundred",
#     8   : "Eight Hundred",
#     7   : "Seven Hundred",
#     6   : "Six Hundred",
#     5   : "Five Hundred",
#     4   : "Four Hundred",
#     3   : "Three Hundred",
#     2   : "Two Hundred",
#     1   : "One Hundred"
# }

# Dictionary to map 'tens' place numbers to word form.
tens_dict = {
    9   : 'Ninety',
    8   : 'Eighty',
    7   : 'Seventy',
    6   : 'Sixty',
    5   : 'Fifty',
    4   : 'Forty',
    3   : 'Thirty',
    2   : 'Twenty',
    1   : 'What happened???'
}

# Dictionary to handle the 'teens'.
teens = {
    19  : 'Nineteen',
    18  : 'Eighteen',
    17  : 'Seventeen',
    16  : 'Sixteen',
    15  : 'Fifteen',
    14  : 'Fourteen',
    13  : 'Thirteen',
    12  : 'Twelve',
    11  : 'Eleven',
    10  : 'Ten'
}

# Dictionary to handle 'ones'.
ones = {
    9   : 'Nine',
    8   : 'Eight',
    7   : 'Seven',
    6   : 'Six',
    5   : 'Five',
    4   : 'Four',
    3   : 'Three',
    2   : 'Two',
    1   : 'One',
    0   : 'Zero'
}

def numbers_to_words(input_integer):
    '''Converts integer numbers between 0 and 99 to word numbers.'''

    # Determine the numbers in each of 'hundreds', 'tens', and 'ones' places.
    hundreds_place = input_integer // 100
    tens_place = input_integer % 100 // 10
    ones_place = input_integer % 10

    # print(f'''
    # Hundreds: {hundreds_place}
    # Tens: {tens_place}
    # Ones: {ones_place}
    # ''')

    ## Convert integer number to word number. ##
    if hundreds_place == 0:

        # If tens_place is 0 (number <= 9), we use only 'ones'.
        if tens_place == 0:
            result = ones[ones_place]
        # If tens_place is 1, we use teens.
        elif tens_place == 1:
            result = teens[input_integer]
        # Tens place is 2 or greater.
        # Determine word for 'tens' place.
        else:
            tens_word = tens_dict[tens_place]
            ones_word = ones[ones_place]
            if ones_place == 0:
                result = tens_word
            else:
                result = f"{tens_word} {ones_word}"
    else:
        hundreds_word = f"{ones[hundreds_place]} Hundred"
        # If tens_place is 0 (number <= 9), we use only 'ones'.
        if tens_place == 0:
            if ones_place == 0:
                result = f"{hundreds_word}"
            else:
                result = f"{hundreds_word} {ones[ones_place]}"
        # If tens_place is 1, we use teens.
        elif tens_place == 1:
            result = f"{hundreds_word} {teens[input_integer]}"
        # Tens place is 2 or greater.
        # Determine word for 'tens' place.
        else:
            tens_word = tens_dict[tens_place]
            ones_word = ones[ones_place]
            if ones_place == 0:
                result = f"{hundreds_word} {tens_word}"
            else:
                result = f"{hundreds_word} {tens_word} {ones_word}"

    # Print result.
    print(f'''
    Integer as number: {input_integer}
    Integer as word: {result}
    ''')

numbers_to_words(input_number_as_integer)