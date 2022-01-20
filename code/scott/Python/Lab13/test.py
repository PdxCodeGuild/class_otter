token_x = 1 # row number
token_y = 1 # column number

token_position = "| * |"

board = [["|   |" for x in range(3)] for y in range(3)]
# print(board)
board[token_x][token_y] = token_position


while True:#
    for i in board:
        print("----- ----- -----")
        print(" ".join(i))
        print("----- ----- -----")

print("Instructions:")
print("up: W")
print("Down: S")
print("Left: A")
print("Right: D")
print("Place Your Token: X")

direction = input(please enter one of the options to )
if direction == "W": #UP
    board[token_x][token_y]="|   |"
    token_x -= 1
    board[token_x][token_y] = "| * |"
elif direction == "S": #Down
    board[token_x][token_y]="|   |"
    token_x += 1
    board[token_x][token_y]="| * |"
elif direction == "A": #Left
    board[token_x][token_y]= "|   |"
    token_y -= 1
    board[token_x][token_y]= "| * |"
elif direction == "D": #Right
    board[token_x][token_y]= "|   |"
    token_y += 1
    board[token_x][token_y]= "| * |"
elif direction == "X": #Place your Token
    board[token_x][token_y]= "| X |" #need logic to determine 'X' or 'O' 
    #and permanently place an 'X' or 'O' in the position
