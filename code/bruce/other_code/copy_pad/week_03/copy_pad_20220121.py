# ******************************* #
#          Transpose List         #
#   for loop list comprehension   #
#           Version: 0.0          #
#       Author: Bruce Stull       #
#            2022-01-22           #
# ******************************* #

# import string
# print(string.ascii_letters)
# print(string.punctuation)
# print(string.digits)

# Revisit how to transpose the list of lists, or using list comprehension.
def list_transpose_using_list_comp(input_list_of_lists):
    trasposed_list_of_lists = [[(input_list_of_lists[i][j]) for i in range(len(input_list_of_lists))] for j in range(len(input_list_of_lists[0]))]
    return trasposed_list_of_lists

# Transpose function using for loop.
def list_transpose_using_for(input_list_of_lists):
    trasposed_list_of_lists = []    # This row is not needed for list-comprehension
    for j in range(len(input_list_of_lists[0])):
        sub_list = []   # This row is not needed for list-comprehension
        for i in range(len(input_list_of_lists)):
            sub_list.append(input_list_of_lists[i][j])  # This row is not needed for list-comprehension
        trasposed_list_of_lists.append(sub_list)    # This row is not needed for list-comprehension
    return trasposed_list_of_lists

board = [['-','-','-'],['-','-','-'],['-','-','-']]

board[0][0] = 'O'
board[0][1] = 'O'
board[0][2] = 'O'

# Join the sub-lists by '|'.
row_strings = ['|'.join(sub_list) for sub_list in board]
# Join the lists by '\n'
board_string = '\n'.join(row_strings)

print()
print(board_string)

board = list_transpose_using_list_comp(board)

# Join the sub-lists by '|'.
row_strings = ['|'.join(sub_list) for sub_list in board]
# Join the lists by '\n'
board_string = '\n'.join(row_strings)

print()
print(board_string)

board = list_transpose_using_for(board)

# Join the sub-lists by '|'.
row_strings = ['|'.join(sub_list) for sub_list in board]
# Join the lists by '\n'
board_string = '\n'.join(row_strings)

print()
print(board_string)