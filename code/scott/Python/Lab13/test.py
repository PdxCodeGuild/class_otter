class player:     
    def __init__(self, name='', token= ''):
        self.name = name
        self.token = token
        return f'Player("{self.name}","{self.token}")'
    def __repr__(self):
            return f'Player("{self.name}","{self.token}")'


    

class game:     
    def __init__(self, board):#
        self.board = board
        def __repr__():
            print(board)

    def move(self, x, token_o, player_1):
    
    
    
    def calc_winner(self):

    def is_full(self,board):
        
    def is_game_over(self):




    #ask for player_name and select 1 or 2 to play as 'X' or 'O'

game = game()

def main():
    players = []
    player1=player(input("Please enter your name? You will be the 'X' Player:"), "X")
    player2=player(input("Please enter your name? You will be the 'O' Player:"), "O")
    players.append(player1)
    players.append(player2)
    print(players)



x = 1 # row number
y = 1 # column number

token_position = "| * |"

board = [["|   |" for x in range(3)] for y in range(3)]
# print(board)
board[x][y] = token_position


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
    board[x][token_o]="|   |"
    x -= 1
    board[x][token_o] = "| * |"
elif direction == "S": #Down
    board[x][token_o]="|   |"
    x += 1
    board[x][token_o]="| * |"
elif direction == "A": #Left
    board[x][token_o]= "|   |"
    y -= 1
    board[x][token_o]= "| * |"
elif direction == "D": #Right
    board[x][token_o]= "|   |"
    y += 1
    board[x][token_o]= "| * |"
elif direction == "X": #Place your Token
    board[x][token_o]= "| X |" #need logic to determine 'X' or 'O' 
    #and permanently place an 'X' or 'O' in the position
