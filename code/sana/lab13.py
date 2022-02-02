# board
    #list
    # display board
# win
# loss
# turn
# tie
# check rows
# check column
# check diagonals

def resetboard():
    board = [['-', '-', '-'],['-', '-', '-'],['-', '-', '-']]
    print(f"{board[0][0]} {board[0][1]} {board[0][2]}\n{board[1][0]} {board[1][1]} {board[1][2]}\n{board[2][0]} {board[2][1]} {board[2][2]}")
    return board
board = [['-', '-', '-'],['-', '-', '-'],['-', '-', '-']]
print(board[0])
print(board[1])
print(board[2])
resetboard()
def choosexo():
    chosen = input('x or o?')
    if chosen == 'x' or chosen == 'o':
        return True
while choosexo() == True:
    print('worked')
    break