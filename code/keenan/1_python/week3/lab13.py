# Lab 13: Tic-Tac-Toe
# 01/20/22


# Tic Tac Toe is a game. Players take turns placing tokens (a 'O' or 'X') into a 3x3 grid. Whoever gets three in a row first wins.
# You will write a Player class and Game class to model Tic Tac Toe, and a function main that models gameplay taking in user inputs through REPL.

# The Player class has the following properties:
# name = player name
# token = 'X' or 'O'

class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token


# The Game class has the following methods:


class Game:
    def __init__(self):
        # the locations will be described as '1' (top left), '2' (top center), '3' (top right), '4' (mid left), '5' (center), '6' (mid right), '7' (bottom left) etc.
        self.board = {
            "1": " ", "2": " ", "3": " ",
            "4": " ", "5": " ", "6": " ",
            "7": " ", "8": " ", "9": " ",
        }


# __repr__() Returns a pretty string representation of the game board
# >>> print(board)
    def __repr__(self):
        print(self.board["1"] + "|" + self.board["2"] + "|" + self.board["3"])
        print(self.board["4"] + "|" + self.board["5"] + "|" + self.board["6"])
        print(self.board["7"] + "|" + self.board["8"] + "|" + self.board["9"])   
    

# move(x, y, player) Place a player's token character string at a given coordinate (top-left is 0, 0), x is horizontal position, y is vertical position.
# >>> board.move(2, 1, player_1)
    def move(self, player):
        while True:                
            move = input("Where do you want to move: ")
            if self.board[move] != " ":
                print('invalid move')
                continue
            else:
                self.board[move] = player.token
                break

# calc_winner() What token character string has won or None if no one has.
    def calc_winner():
        pass

# is_full() Returns true if the game board is full.
    def is_full():
        pass

# is_game_over() Returns true if the game board is full or a player has won.
    def is_game_over():
        pass

# is_full() Returns true if the game board is full.
    def is_full():
        pass

#start by getting the game to print the board.
# continue by adding the basic name functionality
# add moves
# add checks

def main():
    game = Game()

    player1name = input(f"Player one please enter your name: ")
    player2name = input(f"Player two please enter your name: ")
    
    player1_token = input(f"Select 'X' or 'O' as your token: ").upper()
    
    if player1_token != "X" and player1_token != "O":
        print("that is not a valid token.")
    elif player1_token == "X":
            player2_token = "O"
    else:
            player2_token = "X"

    player1 = Player(player1name, player1_token)
    player2 = Player(player2name, player2_token)
    # game.__repr__()

    turn = 0
    
    for i in range(10):
        turn +=1

        if turn % 2 == 1:
            print(f"{player1.name}'s turn.")
            game.move(player1)
        else:
            print(f"{player2.name}'s turn.")
            game.move(player2)

        game.__repr__()


main()