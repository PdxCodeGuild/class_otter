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

        def transpose_list_of_lists(list_of_lists = [[],[]]):
            '''Accepts an argument of a list of lists. Returns a transposed version of the list. List has to be 'rectangular' (sub-lists are all same lenght) to work.'''
            trasposed_list_of_lists = [[(list_of_lists[i][j]) for i in range(len(list_of_lists))] for j in range(len(list_of_lists[0]))]
            return trasposed_list_of_lists
        
        # TODO: Add functionality where these 'token's can be referred by variable so that players can choose their own unique token.
        # i.e. p1.token = 'B'
        def row_win(board = self.board):
            '''Returns player token for a row win, otherwise returns None.'''
            for row in board:
                if row == ['X','X','X']:
                    return 'X'
                elif row == ['O','O','O']:
                    return 'O'
            return None
        
        def column_win():
            '''Returns player token for a column win, otherwise returns None'''
            board = transpose_list_of_lists(self.board)
            result = row_win(board)
            return result
        
        def diagonal_win():
            '''Returns player token for diagonal win, otherwise returns None.'''
            check_list = [self.board[i][i] for i in range(len(self.board))]
            if check_list == ['X','X','X']:
                return 'X'
            elif check_list == ['O','O','O']:
                return 'O'
            return None

        def diagonal_cross_win():
            '''Returns player token for cross diagonal win, otherwise returns None.'''
            # Can we use something similar to the comprehension from diagonal win?
            # check_list = [self.board[i][i] for i in range(len(self.board))]
            check_list = [self.board[0][2],self.board[1][1],self.board[2][0]]
            if check_list == ['X','X','X']:
                return 'X'
            elif check_list == ['O','O','O']:
                return 'O'            
            return None

        # Check for wins.
        row_result = row_win()
        if row_result:
            return row_result

        column_result = column_win()
        if column_result:
            return column_result
        
        diagonal_result = diagonal_win()
        if diagonal_result:
            return diagonal_result
        
        diagonal_cross_result = diagonal_cross_win()
        if diagonal_cross_result:
            return diagonal_cross_result
        
        return None
    
    def print_player_info(self, player):
        print(f"Player info: {player}")

    def is_full(self):
        '''Returns True if gameboard is full. Otherwise returns False.'''
        # Is board full?
        if '-' not in self.board:
            return True
        return False
    
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

    g1.print_player_info(p1)
    g1.print_player_info(p2)
    
    # Set whos turn to player one.
    players = [p1, p2]
    players_turn = 0

    print(g1)
    print()

    while True:

        # Manual moves.
        # g1.move(0,2,'O')
        # g1.move(1,1,'O')
        # g1.move(2,0,'O')

        # g1.move(0,0,'O')
        # g1.move(1,1,'O')
        # g1.move(2,2,'O')

        # g1.move(0,0,'X')
        # g1.move(1,0,'X')
        # g1.move(2,0,'X')

        # g1.move(0,0,'O')
        # g1.move(0,1,'O')
        # g1.move(0,2,'O')

        # No winner.
        # g1.move(0,0,'O')
        # g1.move(0,1,'X')
        # g1.move(0,2,'O')

        # ###### Prompt for input and attempt move ######
        # while True:
        #     # Prompt player n for their move.
        #     print(f"{players[players_turn].token} : {players[players_turn].name}'s turn!")
        #     y_input = input(f"Choose your row: ")
        #     x_input = input(f"Choose your column: ")
        #     # If not valid, go back and re-prompt.
        #     if not x_input.isnumeric() or not y_input.isnumeric():
        #         print("Please enter numeric values between 0 and 2.")
        #         continue
        #     desired_x_position = int(x_input)
        #     desired_y_position = int(y_input)
        #     break
            
        # # Move if available.
        # if not g1.move(desired_x_position - 1, desired_y_position - 1, players[players_turn].token):
        #     continue
        # ###############################################

        # ############ Check for winner ############
        # print(f"g1.calc_winner(): {g1.calc_winner()}")
        # calc_winner_result = g1.calc_winner()
        # if calc_winner_result:
        #     print(f"g1.calc_winner(): {calc_winner_result}")
        # ##########################################
        
        ############### Test is_full() ###############
        print(g1)

        g1.board = [['X','X','X'],['X','X','X'],['X','X','X']]
        print(g1)
        print(f"g1.is_full(): {g1.is_full()}")

        g1.board = [['X','X','O'],['X','X','X'],['X','X','X']]
        print(g1)
        print(f"g1.is_full(): {g1.is_full()}")

        g1.board = [['X','-','O'],['X','X','X'],['X','X','X']]
        print(g1)
        print(f"g1.is_full(): {g1.is_full()}")

        break
        ##############################################


        
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



# main()