# ************************ #
#         Copy Pad         #
#   Support for lab13.py   #
#       Version: 0.0       #
#   Author: Bruce Stull    #
#        2022-01-20        #
# ************************ #

def transpose_list_of_lists(list_of_lists = [[],[]]):
    '''Accepts an argument of a list of lists. Returns a transposed version of the list. List has to be 'rectangular' (sub-lists are all same lenght) to work.'''
    trasposed_list_of_lists = [[(list_of_lists[i][j]) for i in range(len(list_of_lists))] for j in range(len(list_of_lists[0]))]
    return trasposed_list_of_lists

board = [['-','-','-'],['-','-','-'],['-','-','-']]
num_board = [['1','2','3'],['4','5','6'],['7','8','9']]

# print(f"board: {board}")
# print(f"num_board: {num_board}")
############################################################
board[0][0] = 'o'
board[0][1] = 'O'
board[0][2] = 'X'

# Join the sub-lists by '|'.
row_strings = ['|'.join(sub_list) for sub_list in board]
# Join the lists by '\n'
board_string = '\n'.join(row_strings)

# print(f"board: {board}")
print(board_string)

board = transpose_list_of_lists(board)

# Join the sub-lists by '|'.
row_strings = ['|'.join(sub_list) for sub_list in board]
# Join the lists by '\n'
board_string = '\n'.join(row_strings)

# print(f"board: {board}")
print()
print(board_string)

############################################################



# These are checking if '-' is one of the sub-elements. That's why we get False when we expect True. The sub-elements are lists, not a string '_'.
# print(f"'-' in board: {'-' in board}")
# print(f"'-' not in board: {'-' not in board}")

two_by_three = [['a','b'],['c','d'],['e','f']]

row_strings = ['|'.join(sub_list) for sub_list in two_by_three]
two_by_three_string = '\n'.join(row_strings)

print()
print(two_by_three_string)

three_by_two = transpose_list_of_lists(two_by_three)

row_strings = ['|'.join(sub_list) for sub_list in three_by_two]
three_by_two_string = '\n'.join(row_strings)

print()
print(three_by_two_string)