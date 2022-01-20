# the_list = [index for index in range(3)]
# print(the_list)

# the_board = [['-','-','-'],['-','-','-'],['-','-','-']]
# num_board = [['1','2','3'],['4','5','6'],['7','8','9']]
# the_board[0][0] = 'X'
# the_board[1][1] = 'X'

# print(the_board)
# print(num_board)

# print(f"{'|'.join([column for column in the_board[0]])}\n{'|'.join([column for column in the_board[1]])}\n{'|'.join([column for column in the_board[2]])}")

# # Join the sub-lists by '|'.
# the_string = ['|'.join(item) for item in the_board]
# # Join the lists by '\n'
# the_string = '\n'.join(the_string)
# print(the_string)


# data_csv_output = [",".join(line) for line in data_csv_output]
# data_csv_output = "\n".join(data_csv_output)

# ########################################
# # Print rows of num_board.
# for row in num_board:
#     print(row)

# # Print columns of num_board.
# # for space in num_board[][]
# num_list = []
# for row in range(len(num_board)):
#     for column in range(len(num_board)):
#         num_list.append(num_board[column][row])
#         print(num_board[column][row])

# print(num_list)

# num_list = []
# for row in range(len(num_board)):
#     for column in range(len(num_board[row])):
#         # num_list[row][column] = num_board[column][row]
#         num_list.append(num_board[column][row])
#         print(num_board[column][row])

# print(num_list)
# ########################################


# #################################################
# letters = ['a','b','c']

# print(letters)

# # list_of_letters = []
# # for element in letters:
# #     list_of_letters.append([element])

# list_of_letters = [[element] for element in letters]


# print(list_of_letters)
# #################################################

# #################################################
# letters = [['a','b'],['c','d'],['e','f']]

# print(f"letters: {letters}")
# print(f"letters[0]: {letters[0]}")
# print(f"letters[1]: {letters[1]}")
# print(f"letters[0][1]: {letters[0][1]}")

# # We need to grab the first element of each sub-list and create a new sublist from that.
# list_of_letters = [(sub_list[0]) for sub_list in letters]   # ['a', 'c', 'e']
# # Now we need to grab the second.
# list_of_letters = [(sub_list[1]) for sub_list in letters]   # ['b', 'd', 'f']
# # Make the sub-list a list.
# list_of_letters = [[sub_list[1]] for sub_list in letters]   # [['b'], ['d'], ['f']]
# # Try to grab the first and second elements.
# # list_of_letters = [<list comprehension on first elements of sub-lists>] for sub_list in letters]
# # list_of_letters = [(letters[0][0],letters[1][0]) for sub_list in letters]   # [('a', 'c'), ('a', 'c'), ('a', 'c')]
# list_of_letters = [[sub_list[1]] for sub_list in letters]

# # How to get ['a','c'] from letters?
# print(f"letters[0][0], letters[1][0]: {letters[0][0]}, {letters[1][0]}")
# # Use list comprehension with i?
# list_of_letters = [(letters[i][0]) for i in range(len(letters[0]))] # list_of_letters: ['a', 'c']

# # list_of_letters = [[(letters[i][j]) for i in range(len(letters[j]))] for j in range(len(letters))]
# # # Traceback (most recent call last):
# # #   File "C:\Users\Bruce\Programming\class_otter\code\bruce\other_code\copy_pad\copy_pad_20220119.py", line 87, in <module>
# # #     list_of_letters = [[(letters[i][j]) for i in range(len(letters[j]))] for j in range(len(letters))]
# # #   File "C:\Users\Bruce\Programming\class_otter\code\bruce\other_code\copy_pad\copy_pad_20220119.py", line 87, in <listcomp>
# # #     list_of_letters = [[(letters[i][j]) for i in range(len(letters[j]))] for j in range(len(letters))]
# # #   File "C:\Users\Bruce\Programming\class_otter\code\bruce\other_code\copy_pad\copy_pad_20220119.py", line 87, in <listcomp>
# # #     list_of_letters = [[(letters[i][j]) for i in range(len(letters[j]))] for j in range(len(letters))]
# # # IndexError: list index out of range

# list_of_letters = [(letters[0][i]) for i in range(len(letters[0]))] # list_of_letters: ['a', 'b']
# list_of_letters = [(letters[i][0]) for i in range(len(letters))] # list_of_letters: ['a', 'c', 'e']

# list_of_letters = [[(letters[i][j]) for i in range(len(letters))] for j in range(len(letters[0]))]  # list_of_letters: [['a', 'c', 'e'], ['b', 'd', 'f']]



# print(f"list_of_letters: {list_of_letters}")
# #################################################

############### DING DING DING!!! WINNER WINNER!!! ###############
letters = [['a','b'],['c','d'],['e','f']]
print(f"letters: {letters}")
# list_of_letters = [[(letters[i][j]) for i in range(len(letters))] for j in range(len(letters[0]))]  # list_of_letters: [['a', 'c', 'e'], ['b', 'd', 'f']]

# Create the function which does the above list comprehension.
def transpose_list_of_lists(list_of_lists):
    list_of_letters = [[(list_of_lists[i][j]) for i in range(len(list_of_lists))] for j in range(len(list_of_lists[0]))]
    return list_of_letters

list_of_letters = transpose_list_of_lists(letters)

print(f"list_of_letters: {list_of_letters}")
##################################################################

the_board = [['-','-','-'],['-','-','-'],['-','-','-']]
num_board = [['1','2','3'],['4','5','6'],['7','8','9']]

print(f"the_board: {the_board}")
print(f"num_board: {num_board}")

the_board[0][0] = 'X'
the_board[1][1] = 'X'

print(f"the_board: {the_board}")
print(f"num_board: {num_board}")
