# Lab 13: Tic-Tac-Toe
# 01/20/22


# Tic Tac Toe is a game. Players take turns placing tokens (a 'O' or 'X') into a 3x3 grid. Whoever gets three in a row first wins.
# You will write a Player class and Game class to model Tic Tac Toe, and a function main that models gameplay taking in user inputs through REPL.

# The Player class has the following properties:
# name = player name
# token = 'X' or 'O'

# The Game class has the following properties:
# board = your representation of the board
# You can represent the board however you like, such as a 2D list, tuples, or dictionary.

# The Game class has the following methods:
# __repr__() Returns a pretty string representation of the game board
# >>> print(board)
# X| | 
# O|X|O
#  | | 

# move(x, y, player) Place a player's token character string at a given coordinate (top-left is 0, 0), x is horizontal position, y is vertical position.
# >>> board.move(2, 1, player_1)
#  | | 
#  | |X
#  | | 
# calc_winner() What token character string has won or None if no one has.
# X| | 
# O|X|O
#  | |X
# >>> board.calc_winner()
# X
# is_full() Returns true if the game board is full.
# X|O|X
# X|X|O
# O|O|X
# >>> board.is_full()
# True
# is_game_over() Returns true if the game board is full or a player has won.
# X|O|X
# X|X|O
# O|O|X
# >>> board.is_game_over()
# True

# X|O|
#  | |X
#  | |
# >>> board.is_game_over()
# False

class Player:
    def __init__(self, name = '', Token = ''):
        self.name = input('What is your player name? ')
        self.Token = input('Will you play as "X" or "O" ')
    
    
class Game:
    def __init__(self, board = []):
        self.board = board

    
    