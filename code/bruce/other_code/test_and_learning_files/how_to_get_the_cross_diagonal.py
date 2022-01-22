
board = [['-','-','-'],['-','-','-'],['-','-','-']]

# print(board)    # [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

# Insert '|' between elements in sub-lists.
row_strings = ['|'.join(sub_list) for sub_list in board]
# Join the lists by '\n' for pretty print.
result_string = '\n'.join(row_strings)
print(f"\nBoard layout before adding 'O's:\n{result_string}")

# Add 'O's in the positions I want to retreive.
board[0][2] = 'O'
board[1][1] = 'O'
board[2][0] = 'O'

# Insert '|' between elements in sub-lists.
row_strings = ['|'.join(sub_list) for sub_list in board]
# Join the lists by '\n' for pretty print.
result_string = '\n'.join(row_strings)
print(f"\nBoard layout after adding 'O's:\n{result_string}")

# Print board which has the 'O's.
# print(board)    # [['-', '-', 'O'], ['-', 'O', '-'], ['O', '-', '-']]

# - - O
# - O -
# O - -

# ################## Doesn't work as needed ##################
# # for i in range(len()): with board[i][-i] doesn't do what we need. It would produce the following.
# board[0][-0] = 'O'
# board[1][-1] = 'O'
# board[2][-2] = 'O'
# print(board)    # [['O', '-', '-'], ['-', '-', 'O'], ['-', 'O', '-']]
# # O - -
# # - - O
# # - O -
# ############################################################

####################### Doesn't quite work as needed #######################
# # Results in ['O', '-', '-', '-', 'O', '-', '-', '-', 'O']
# cross_diagonal = []
# for i in range(len(board)):
#     for j in range(len(board) - 1, -1, -1):
#         cross_diagonal.append(board[i][j])
# print(cross_diagonal)   # ['O', '-', '-', '-', 'O', '-', '-', '-', 'O']
############################################################################


# Need something like: [board[0][2],board[1][1],board[2][0]]

# Try list comprehension with opposing (complimentary) pairs in the sub-tuples.
# This works but we don't need the 'if x + y == len(board) - 1' since that would only be needed if we nested loops.
# cross_diagonal = [board[x][y] for x,y in ((0,2),(1,1),(2,0)) if x + y == len(board) - 1]
# print(cross_diagonal)   # ['O', 'O', 'O']

# Found how to get a programatically obtained ((0,2),(1,1),(2,0)) of arbitrary length.
# This method results in list of tuples, but still functions as needed. TODO: Figure out how to make it a tuple of tuples.
# Either of these will work, one is just the reversed list of the other.
# range(len(board) - 1, - 1, - 1) ==>> (2, 1, 0)
# range(len(board)) ==>> (0, 1, 2)

# These three options succeed in producing the needed list(s)/tuple(s).
# the_special_list_of_tuples = list(zip(range(len(board)),range(len(board) - 1, - 1, - 1)))   # [(0, 2), (1, 1), (2, 0)]
# the_special_list_of_tuples = list(zip(range(len(board) - 1, - 1, - 1),range(len(board))))   # [(2, 0), (1, 1), (0, 2)]    # Uses list()
the_special_list_of_tuples = tuple(zip(range(len(board) - 1, - 1, - 1),range(len(board))))   # ((2, 0), (1, 1), (0, 2)) # Uses tuple()
print(f"\nGenerated the_special_list_of_tuples: {the_special_list_of_tuples}")

cross_diagonal = [board[x][y] for x, y in the_special_list_of_tuples]
print(f"\n[board[x][y] for x, y in the_special_list_of_tuples]: {cross_diagonal}\n")   # ['O', 'O', 'O']

