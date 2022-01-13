# Lab 6: Credit Card Validation
# 01/11/2022

# Let's write a function credit_card_validator which returns whether a string containing 
# a credit card number is valid as a boolean. The steps are as follows:

# Convert the input string into a list of ints
# Slice off the last digit. That is the check digit.
# Reverse the digits.
# Double every other element in the reversed list (starting with the first number in the list).
# Subtract nine from numbers over nine.
# Sum all values.
# Take the second digit of that sum.
# If that matches the check digit, the whole card number is valid.
# Here is a valid credit card number to test with: 4556737586899855

# For example, the worked out steps would be:

# 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
# 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5
# 5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
# 10 8 18 9 16 6 16 5 14 3 14 6 10 5 8
# 1 8 9 9 7 6 7 5 5 3 5 6 1 5 8
# 85
# 5
# True Valid!

# Note: This lab is much easier if performed with list comprehensions.

def credit_card_validator(demo_card):
    # cast the input string into a list of integers
    integer_card = [int(num) for num in demo_card]
    
    # slice off the last digit 
    check_digit = integer_card.pop()
    
    # reverse the digits, we must use the reversed function here, because reverse()
    #  changes the original function and does not return an iterable list
    reversed_card = list(reversed(integer_card))

    # this line below can be done using the enumerate fxn
    # WIP - doubled_reversed_card = X*2 for x in reversed_card if reversed_card[] 

    for i in range(len(reversed_card)):
        if i % 2 == 0:
            reversed_card[i] *= 2
 
    # subtract nine from all numbers over nine
    # the if and else statements must come before the 'for' 
    subtract_9 = [x - 9 if x > 9 else x for x in reversed_card]

    # sum all the values
    digit_sum = sum(subtract_9)

    # take the second digit of the sum
    second_digit = digit_sum % 10

    # if the second digit matches the check digit, the card number is valid
    return second_digit == check_digit

print(credit_card_validator("4556737586899855"))


