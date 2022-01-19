# *********************** #
#    Function Practice    #
#                         #
#       Version: 1.0      #
#   Author: Bruce Stull   #
#        2022-01-13       #
# *********************** #

# Resources:
# https://github.com/PdxCodeGuild/class_otter/blob/main/1%20Python/docs/10%20Functions.md

# These two below functions have the same result (do the same thing). Try to understand why.
def one_way_to_add_two_numbers(a, b):
    return a + b

def another_way_to_add_two_numbers(c,d):
    result = c + d
    return result

# These are some foundational concepts. If you can breeze through these, you will be good.
# Some tasks for you:
# Try to understand how to use the two adding functions above. Do they actually do the same thing? Why? How?

# Call the function one_way_to_add_two_numbers() with parameters/arguments of 4 and 5, but don't do anything with the result.

# Call the function another_way_to_add_two_numbers() with parameters/arguments of 2 and 3, but don't do anything with the result.

# Call the function one_way_to_add_two_numbers() with parameters/arguments 6 and 7, and set that result (returned value) to a new variable with name 'result_of_add_6_and_7'.

# Call the function another_way_to_add_two_numbers() with parameters/arguments of 8 and 9, and set the result (returned value) to a new variable with name 'result_of_add_8_and_9'.

# Hints:
# How can we see the results of a function to know it is working?
    # We can use print(), but that doesn't really let us do any further processing of the result.
    # One solution is to set/assign the result (returned value) of the function to a variable so that we can use it later.

# Example:
# Use the function sum() to add a couple numbers 1, 2, and 3.
# This line calls the function but doesn't do anything with the result.
sum(1,2,3)

# This line calls the sum() function with some parameters and then assigns the returned value to a variable the_sum_of_the_numbers.
# We do this so that we can use the information/process/logic of the result of calling sum() with the parameters 1, 2, and 3 to do more logic on the result.
the_sum_of_the_numbers = sum(1,2,3)

# We are only using the print() function here to see what the value of the_sum_of_the_numbers is. But, it only displays the result in console.
print(the_sum_of_the_numbers)

# We need to understand how to use the above functions and variables to further process the information and eventually do more complicated tasks.
# Some more tasks for you:
# 1. Multiply the_sum_of_the_numbers by 6 and assign the result to a variable named 'the_sum_of_the_numbers_times_6'.

# 2. Define a function named 'multiply_by_six' which accepts one parameter 'input_number' and returns the value of 'input_number' times 6.
    # Actually, do two functions:
        # One named 'multiply_by_six_compact' which does the logic on the same line as the 'return' keyword.
            # Something like the following:
            # return <all the logic here>
# Your function here:
            
        # One named 'multiply_by_six' which does the logic above the 'return' line and assigns the logic to a variable named 'result'. Then uses the 'result' variable on the 'return' line.
            # Something like the following:
            # result = <all the logic here>
            # return result
# Your function here:

# 3. Use your functions multiply_by_six_compact() and multiply_by_six():
    # Call each function with whatever parameters you decide and assign the returned value to new variables with your preferred names.