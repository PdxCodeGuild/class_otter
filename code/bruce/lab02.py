# *********************** #
#   Author: Bruce Stull   #
#     Average Numbers     #
#       Version: 2.0      #
#        2022-01-05       #
# *********************** #

# Assignment:
# https://github.com/PdxCodeGuild/class_otter/blob/main/1%20Python/labs/02%20Average%20Numbers.md

## Loop to prompt user to enter values to average. ##
# Initialize the list.
list_of_numbers = []
# 'while' loop to prompt user for input.
while True:
    # Prompt user for input.
    user_input_value_as_string = input("Please enter a number to add to the list to be averaged (type 'done' when completed): ")
    
    # If user input is 'done':
    if user_input_value_as_string == 'done':
        # Break out of loop and send to calculator.
        break
    
    # If user input is not numeric:
    # Can use 'elif' here.
    if not user_input_value_as_string.isnumeric():
        # Remind user of acceptable input values.
        print("Please enter a numeric value or 'done'.")
        # Go back to beginning of while loop.
        continue
    
    # User input is not "done" and user input is numeric, so add the numeric value to the list.
    list_of_numbers.append(float(user_input_value_as_string))

## Iterate over list and add the current list element to the running_sum. ##
# Initialize variable:
running_sum = 0
# Define the 'for' loop, iterate over list_of_numbers on each item.
# We are using this loop to add up all the values of the items in the list:
for item in list_of_numbers:
    # Add the current item value to running_sum:
    running_sum += item

# Handle case where list_of_numbers is empty.
if len(list_of_numbers) == 0:
    result = "No numbers entered so there is no average value."
# Otherwise, list contains some non-zero quantity of elements.
else:
    # Calculate the average, round the result to 2 decimal digits:
    result = round(running_sum / len(list_of_numbers), 2)

# Display the average:
print(f'''
The list of numbers: {list_of_numbers}

The average: {result}.
''')