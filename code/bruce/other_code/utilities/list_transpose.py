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
# def transpose_list_of_lists(list_of_lists):
#     '''Accepts an argument of a list of lists. Returns a transposed version of the list. List has to be 'rectangular' (sub-lists are all same lenght) to work.'''
#     trasposed_list_of_lists = [[(list_of_lists[i][j]) for i in range(len(list_of_lists))] for j in range(len(list_of_lists[0]))]
#     return trasposed_list_of_lists

def transpose_list_of_lists(input_list_of_lists):
    '''Accepts an argument of a list of lists. Returns a transposed version of the list. List has to be 'rectangular' (sub-lists are all same lenght) to work.'''
    trasposed_list_of_lists = []
    for j in range(len(input_list_of_lists[0])):
        sub_list = []
        for i in range(len(input_list_of_lists)):
            # j : first and second element of each sub-lists of original list of lists.
            # i : first, second, and third sub-lists in original list of lists.
            # appends first through ith element of each sub-list of original list to new sub-list.
            sub_list.append(input_list_of_lists[i][j])
        # append the new jth sub-list to the working list.
        trasposed_list_of_lists.append(sub_list)
    return trasposed_list_of_lists


# Test data:
letters = [['a','b'],['c','d'],['e','f']]

# Process the test data:
print(f"letters: {letters}")

letters = transpose_list_of_lists(letters)

print(f"list_of_letters: {letters}")