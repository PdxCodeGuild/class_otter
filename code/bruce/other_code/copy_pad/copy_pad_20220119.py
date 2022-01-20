# the_list = [index for index in range(3)]
# print(the_list)

the_board = [['-','-','-'],['-','-','-'],['-','-','-']]
num_board = [['1','2','3'],['4','5','6'],['7','8','9']]
the_board[0][0] = 'X'
the_board[1][1] = 'X'

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

# Print rows of num_board.
for row in num_board:
    print(row)

# Print columns of num_board.
# for space in num_board[][]
for row in range(len(num_board)):
    for column in range(len(num_board)):
        print(num_board[column][row])