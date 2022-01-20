# ***************************** #
#      Lab 13: Tic-Tac-Toe      #
#   classes methods variables   #
#          Version: 1.0         #
#      Author: Bruce Stull      #
#           2022-01-19          #
# ***************************** #

# Assignment:
# https://github.com/PdxCodeGuild/class_otter/blob/main/1%20Python/labs/13%20Tic%20Tac%20Toe.md

# Board layout:
# (0,0)(1,0)(2,0)
# (0,1)(1,1)(2,1)
# (0,2)(1,2)(2,2)

# Board example status:
# X| | 
#  |O| 
# O|X| 


# # My own printing function:
# from os import name


def print_variable_and_description(variable_under_review, description_of_logic = '', print_logic_results = True):
    '''Accepts three arguments: A variable we are examining, a description of the logic we are examining, and a print flag.'''
    __name__ = print_variable_and_description
    string_result = f"{print_variable_and_description.__name__}: {description_of_logic}: {variable_under_review}"
    if print_logic_results:
        print(string_result)

# It seems we keep player position in Game rather than Player?
#################### The Player ####################
class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token  # Token will be either 'X' or 'O'.
        # self.x = x
        # self.y = y

    def __str__(self) -> str:
        return f"{self.name}:{self.token}"
    
    # def get_position(self):
    #     return self.x, self.y
####################################################

################### The Game ###################
# TODO: Add functionality where size of board can be provided by a class variable.
class Game:
    def __init__(self):
        # self.board = board
        # # x:              0       1       2     0       1       2      0       1       2
        # # y:              0       0       0     1       1       1      2       2       2
        # self.board = [['-','|','-','|','-'],['-', '|','-','|','-'],['-','|','-','|','-']]   # Do we need the '|'?

        # x:            0   1   2     0   1   2     0   1   2
        # y:            0   0   0     1   1   1     2   2   2
        self.board = [['-','-','-'],['-','-','-'],['-','-','-']]    # This is without the '|'. The '|' can be added at end in a '|'.join().
        
        # TODO: This will be used in future expansions. Keep a history of the game so it can be replayed.
        # Store the Player.name, Player.token, Player.x, and Player.y as a list within a list.
        self.move_history = []
        
        # V 1.0
        # self.board_as_string = f"{'|'.join([column for column in self.board[0]])}\n{'|'.join([column for column in self.board[1]])}\n{'|'.join([column for column in self.board[1]])}"
        # V 1.1 TODO: Can we compact this?
        # self.board_as_string = f"{'|'.join([column for column in self.board[0]])}\n{'|'.join([column for column in self.board[1]])}\n{'|'.join([column for column in self.board[1]])}"

        # self.player1position = [x,y]
        # self.player2position = [x,y]
        # Do we need to instantiate player positions on game start?
        # No, we do not want to do that, it wouldn't make sense, since instantiating requires some value.
        # We can probably just grab position from Player?
        
        ########################################## NOTE!!! ##########################################
        # Player positions are kept track of in self.board
        #############################################################################################
        # self.player_positions = [[],[]] <<== Not needed!!!

        # NOTE: Use something like:
        # [['O','-','-'],['-','X','-'],['-','-','-']]

    def __str__(self) -> str:
        '''Returns a representation of the board status at a current point in the game.'''
        # return f"{self.board_as_string}"
        # Can use loop to print each line individually.
        
        # Join the sub-lists by '|'.
        row_strings = ['|'.join(sub_list) for sub_list in self.board]
        # Join the lists by '\n'
        result_string = '\n'.join(row_strings)
        # return f"{'|'.join([column for column in self.board[0]])}\n{'|'.join([column for column in self.board[1]])}\n{'|'.join([column for column in self.board[2]])}"
        return result_string

    def move(self, x, y, token):
        '''Checks if position x,y is available. If so, place the token for one of the players at x,y.'''
        if self.position_available(x, y):
            self.board[y][x] = token
            # This will later be changed to an entry in a list for future playback.
            # return f"{token} placed at: {x},{y}"
            return True
        # This will later be changed to an entry in a list for future playback.
        # return f"{token} not placed at: {x},{y}"
        return False
    
    def position_available(self, x, y):
        '''Check if position is available for play. Returns True if available, A string is returned otherwise.'''
        if self.board[y][x] == '-': 
            return True
        return False
    
    def calc_winner(self):
        '''Returns which token ('X' or 'O') has won, otherwise returns None.'''
        def row_win():
            '''Returns player token for a row win, otherwise returns None.'''
            for row in self.board:
                if row == ['X','X','X']:
                    return 'X'
                elif row == ['Y','Y','Y']:
                    return 'Y'
                else:
                    return None
        
        def column_win():
            '''Returns player token for a column win, otherwise returns None'''
            for column in range(3):
                for row in range(3):

            
        return False
    
    def is_full(self):
        '''Returns True if gameboard is full. Otherwise returns False.'''
        if '-' not in self.board:
            return False
        return True
    
    def is_game_over(self):
        '''Returns True if game board is full or a player has won.'''
        if self.is_full() or self.calc_winner() != None:
            return True
        return False
    
################################################


################### Testing ###################
def test_position_available():
    g1 = Game()
    assert g1.position_available(0, 0) == True

    g2 = Game()
    g2.board[0][0] = 'X'
    assert g2.position_available(0, 0) == False

    g3 = Game()
    g3.board[0][0] = 'O'
    assert g3.position_available(0, 0) == False

def test_move():
    g1 = Game()
    g1.board[1][1] = 'X'
    assert g1.move(1, 1, 'O') == "O not placed at: 1,1"

    g2 = Game()
    assert g2.move(1, 1, 'X') == "X placed at: 1,1"

###############################################


def main():

    g1 = Game()

    p1 = Player('Dezzi', 'X')
    p2 = Player('Bunbun', 'O')
    
    # Set whos turn to player one.
    players = [p1, p2]
    players_turn = 0

    print(g1)

    while True:
        # Is game over.

        # Prompt player n for their move.
        print(f"{players[players_turn].token}:{players[players_turn].name}'s turn!")
        desired_x_position = int(input(f"Choose your column: "))
        desired_y_position = int(input(f"Choose your row: "))
        # Move if available.
        if not g1.move(desired_x_position, desired_y_position, players[players_turn].token):
            continue
        print(g1)
        # print(g1.board)
        # Check for win.
        # Is game over.
        # Display board.
        # Prompt player m for their move.
        # Move if available.
        # Check for win.
        # Is game over.
        # Display board.
        
        # Toggle player turn to other player.
        if players_turn == 0:
            players_turn = 1
        else:
            players_turn = 0



    # p1 = Player("Earl",'X')
    # p2 = Player("Dezzi",'O')
    # print(p1)
    # print(p2)

    # g1 = Game()
    # # print(g1)
    # # g1.board[0][0] = 'X'
    # # print(g1)
    
    # print(g1)
    # # print(f"g1.position_available(p1.token, 0, 0): {g1.position_available(p1.token, 0, 0)}")
    # # print(f"g1.move('X',x,y): {g1.move('X', 0, 0)}")
    # print(g1.move('X', 0, 0))
    # print(g1.move('X', 0, 0))
    # print(g1.move('X', 1, 1))

    # # print(f"g1.position_available(p1.token, 0, 0): {g1.position_available(p1.token, 0, 0)}")
    # # print(f"g1.move('X',x,y): {g1.move('X', 0, 0)}")
    # # print(f"g1.move('X',x,y): {g1.move('X', 1, 1)}")
    # print(g1)



main()