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
# ############################################################
# board[0][1] = 'X'
# board[0][2] = 'X'

# print(f"board: {board}")

# # board = transpose_list_of_lists(board)

# board = [board[i][i] for i in range(len(board), 0, -1)]

# print(f"board: {board}")
# ############################################################




print(f"'-' in board: {'-' in board}")
print(f"'-' not in board: {'-' not in board}")