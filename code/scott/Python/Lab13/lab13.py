# def display_board(board):

#     print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
#     print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
#     print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
#     print("\n")
#     print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
#     print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
#     print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
#     print("\n")
#     print(display_board(board))
board = {0: " ", 1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " "}
b = (board)
line1 = b[0] + " | " + b[1] + " | " + b[2] + "     1 | 2 | 3"
line2 = '-+-+-'
line3 = b[3] + " | " + b[4] + " | " + b[5] + "     4 | 5 | 6"
line4 = '-+-+-'
line5 = b[6] + " | " + b[7] + " | " + b[8] + "     7 | 8 | 9"
print(line1 + '\n' + line2 + '\n' + line3 + '\n' + line4 + '\n' + line5)
    


