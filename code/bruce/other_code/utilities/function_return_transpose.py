# ************************************* #
#           Function Transpose          #
#   return transpose of list of lists   #
#              Version: 1.0             #
#          Author: Bruce Stull          #
#               2022-01-20              #
# ************************************* #

# Link to notes:
# https://github.com/PdxCodeGuild/class_otter/blob/bruce/code/bruce/other_code/copy_pad/copy_pad_20220119.py

# Create the function which transposes list of lists:
def transpose_list_of_lists(list_of_lists):
    '''Accepts an argument of a list of lists. Returns a transposed version of the list. List has to be 'rectangular' (sub-lists are all same lenght) to work.'''
    trasposed_list_of_lists = [[(list_of_lists[i][j]) for i in range(len(list_of_lists))] for j in range(len(list_of_lists[0]))]
    return trasposed_list_of_lists


# Test data:
letters = [['a','b'],['c','d'],['e','f']]

# Process the test data:
print(f"letters: {letters}")

list_of_letters = transpose_list_of_lists(letters)

print(f"list_of_letters: {list_of_letters}")