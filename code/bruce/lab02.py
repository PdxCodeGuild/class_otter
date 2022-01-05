# *********************** #
#   Author: Bruce Stull   #
#     Average Numbers     #
#       Version: 1.0      #
#        2022-01-05       #
# *********************** #

# Assignment:
# https://github.com/PdxCodeGuild/class_otter/blob/main/1%20Python/labs/02%20Average%20Numbers.md

# Provided list:
list_of_integers = [5, 0, 8, 3, 4, 1, 6]

## Iterate over list and add the current list element to the running_sum. ##
# Initialize variable:
running_sum = 0
# Define the 'for' loop, iterate over list_of_integers on each item.
# We are using this loop to add up all the values of the items in the list:
for item in list_of_integers:
    # Add the current item value to running_sum:
    running_sum += item

# Calculate the average, round the result to 2 decimal digits:
average_of_list = round(running_sum / len(list_of_integers), 2)

# Display the average:
print(f'''
The average of {list_of_integers} is: {average_of_list}.
''')