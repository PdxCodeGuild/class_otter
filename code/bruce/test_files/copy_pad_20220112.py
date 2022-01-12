# *********************** #
#   Copy Pad 2022-01-12   #
#                         #
#       Version: 0.0      #
#   Author: Bruce Stull   #
#        2022-01-12       #
# *********************** #

import random

nums_list = [1,2,3,4]
more_numbers = [7,8,9]

########################################################
# Functions which return 'None'.
########################################################

# print(nums_list)
# print(print(nums_list))

# print(nums_list)                        # [1, 2, 3, 4]
# nums_list.extend(more_numbers)
# print(nums_list.extend(more_numbers))   # None
# print(nums_list)                        # [1, 2, 3, 4, 7, 8, 9, 7, 8, 9]

########################################################

# print('########################################################')

########################################################
# Functions which 'return' a value versus 'print' a value.
########################################################
# Define a variable 'a_number' and assign the integer value '6' to it.
a_number = 6

# Print out the value of the variable 'a_number'.
print(a_number)

# Define a variable and assign a random integer between 0 and 10 to it.
random_integer = random.randint(0,10)
# Print out the value of the 'random_integer'.
print(random_integer)

# What happens if we try to print out a print statement?
# print(print())
# Or, another way to do that is assign 'print()' to some variable, and then print the value of the variable.
return_value_of_print = print()
# print(return_value_of_print)
# 'print()' has no return statement in it's definition so the returned value of any print() statement is 'None'.
########################################################





# Function examples.
########################################################
def add(a,b):
    return a + b
# print(add(2,3))

def test_add():
    assert add(2,3) == 5
    assert print(add(2,3)) == 5
    assert add(4,5) == 8
########################################################




########################################################
# Function definition - we define a function.
########################################################
# This is where we specify:
# 'def' means we are defining a function.
# 'multiply_nums' means we are giving the function a name of 'multiply_nums'.
# The stuff inside the parentheses 'argument_01, argument_02' mean we are required to provide two parameters when we 'call' the function.
def multiply_nums(argument_01, argument_02):
    # We use the variables provided in the function definition to do the logic on those arguments.
    return argument_01 * argument_02
########################################################





########################################################
# Function calling - we call the function
########################################################
# Specify a couple values we are going to be processing through 'multiply_nums()'.
first_number = 3
second_number = 7
# We are calling the function 'multiply_nums()'.
# We are providing two parameters for the function 'first_number' and 'second_number' and separating the parameters by commas.
# The result of the 'calling' of 'multiply_nums()' with parameters 'first_number' and 'second_number' is then assigned to the variable 'multiplication_result'.
multiplication_result = multiply_nums(first_number, second_number)
########################################################





########################################################
# Function calling - we call the function
########################################################
# Here we call the 'print()' function.
# The 'print()' function arguments are optional.
# That's why we can execute the literal 'print()' without any provided parameters and it will execute without error.
# The optional argument is printed to the console. But... There is nothing 'returned' to the function caller. So we can't really 'do' anything with the result.
# print("Goodbuy!")
########################################################






########################################################
# Statement execution - we run something but don't assign it to anything
########################################################
# This line will 'execute' without error, but the result of 'multiply_nums(9,8)' is not assigned to a variable or passed to any other function.
# So we aren't really doing anything with the logic here.
# To actually 'use' the logic, we need to assign variables and/or return the values to other calling functions.
multiply_nums(9,8)
########################################################




########################################################
# Let's break this down into finer steps and try to see what's going on.
# Here, we define a function. Use keyword 'def', give function a name 'add',
# provide the required parameters 'a' and 'b' inside the '()'.
def add(c,d):
    # Do the logic and set the result to some variable 'the_sum'.
    # The statement/operation 'c + d' is executed and then that value is assigned to 'the_sum'.
    the_sum = c + d
    # Use keyword 'return' to provide the result of the logic 'the_sum' back to
    # whatever function is 'calling' the 'add()' function.
    # The 'add()' function will be called when we execute the line "sum_of_the_numbers = add(3,4)".
    return the_sum

# This line executes 'add(3,4)' and then assigns that value to 'sum_of_the_numbers'.
sum_of_the_numbers = add(3,4)

# This line will print out the value which is stored in the variable 'sum_of_the_numbers'.
# print(sum_of_the_numbers)
########################################################




########################################################
# We can place the 'e + f' operation directly after the 'return' keyword.
# The reason we can do this: the 'e + f' statement/operation will be executed before it's used by 'return'.
def add(e,f):
    # So, we can pack some logic on the same line as 'return' as long as it is after the 'return' keyword.
    return e + f

# We can pack the function call 'add(3,6)' inside the 'print()' statement/function since the stuff inside the () will be executed and then the result will be given to 'print()'.
# print(add(3,6))
########################################################







def add(a,b):
    '''Accepts arguments 'a' and 'b'. Returns the value of 'a' added to 'b'.'''
    the_sum = a + b
    return the_sum

