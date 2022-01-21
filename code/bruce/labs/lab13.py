# ***************************** #
#      Lab 13: Tic-Tac-Toe      #
#   classes methods variables   #
#          Version: 1.0         #
#      Author: Bruce Stull      #
#           2022-01-19          #
# ***************************** #

import random
import time

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

    def __str__(self) -> str:
        return f"{self.name} : {self.token}"
####################################################

################### The Game ###################
# TODO: Add functionality where size of board can be provided by a class variable.
class Game:
    def __init__(self):

        # # x:              0       1       2     0       1       2      0       1       2
        # # y:              0       0       0     1       1       1      2       2       2
        # self.__board = [['-','|','-','|','-'],['-', '|','-','|','-'],['-','|','-','|','-']]   # Do we need the '|'?

        # NOTE: Use something like:
        # [['O','-','-'],['-','X','-'],['-','-','-']]

        # x:            0   1   2     0   1   2     0   1   2
        # y:            0   0   0     1   1   1     2   2   2
        self.__board = [['-','-','-'],['-','-','-'],['-','-','-']]    # This is without the '|'. The '|' can be added at end in a '|'.join().
        
        # TODO: This move_history will be used in future expansions. Keep a history of the game so it can be replayed.
        # Store the Player.name, Player.token, Player.x, and Player.y as a list within a list.
        self.move_history = []
        
        ########################################## NOTE!!! ##########################################
        # Player positions are kept track of in self.__board
        # self.player_positions = [[],[]] <<== Not needed!!!
        #############################################################################################

    def __str__(self) -> str:
        '''Returns a representation of the board status at a current point in the game.'''
        
        # Join the sub-lists by '|'.
        row_strings = ['|'.join(sub_list) for sub_list in self.__board]
        # Join the lists by '\n'
        result_string = '\n'.join(row_strings)
        # return f"{'|'.join([column for column in self.__board[0]])}\n{'|'.join([column for column in self.__board[1]])}\n{'|'.join([column for column in self.__board[2]])}"
        return result_string

    # TODO: Add functionality to log game moves to move_history.
    def move(self, x, y, player):
        '''Checks if position x,y is available. If so, place the token for one of the players at x,y.'''
        if self.position_available(x, y):
            self.__board[y][x] = player.token
            return True
        return False

    def position_available(self, x, y):
        '''Check if position is available for play. Returns True if available, False is returned otherwise.'''
        if self.__board[y][x] == '-': 
            return True
        return False
    
    def calc_winner(self, player):
        '''Returns which token ('X' or 'O') has won, otherwise returns None.'''

        def transpose_list_of_lists(list_of_lists = [[],[]]):
            '''Accepts an argument of a list of lists. Returns a transposed version of the list. List has to be 'rectangular' (sub-lists are all same length) to work.'''
            trasposed_list_of_lists = [[(list_of_lists[i][j]) for i in range(len(list_of_lists))] for j in range(len(list_of_lists[0]))]
            return trasposed_list_of_lists
        
        # TODO: Add functionality where these 'token's can be referred by variable so that players can choose their own unique token.
        # i.e. p1.token = 'B'
        def row_win(board = self.__board):
            '''Returns player token for a row win, otherwise returns None.'''
            for row in board:
                if row[0] == row[1] == row[2] == player.token:
                    return player.token
                # if row == ['X','X','X']:
                #     return 'X'
                # elif row == ['O','O','O']:
                #     return 'O'
            return None
        
        def column_win():
            '''Returns player token for a column win, otherwise returns None'''
            board = transpose_list_of_lists(self.__board)
            result = row_win(board)
            return result
        
        def diagonal_win():
            '''Returns player token for diagonal win, otherwise returns None.'''
            check_list = [self.__board[i][i] for i in range(len(self.__board))]
            if check_list[0] == check_list[1] == check_list[2] == player.token:
                return player.token
            # if check_list == ['X','X','X']:
            #     return 'X'
            # elif check_list == ['O','O','O']:
            #     return 'O'
            return None

        def diagonal_cross_win():
            '''Returns player token for cross diagonal win, otherwise returns None.'''
            # Can we use something similar to the comprehension from diagonal win?
            # check_list = [self.__board[i][i] for i in range(len(self.__board))]
            check_list = [self.__board[0][2],self.__board[1][1],self.__board[2][0]]
            if check_list[0] == check_list[1] == check_list[2] == player.token:
                return player.token
            # if check_list == ['X','X','X']:
            #     return 'X'
            # elif check_list == ['O','O','O']:
            #     return 'O'            
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
        for row in self.__board:
            for column in row:
                # Game is not full if there are any remaining '-' on the board.
                if column == '-':
                    return False
        return True

    def is_game_over(self, player):
        '''Returns True if game board is full or a player has won.'''
        if self.is_full() or self.calc_winner(player) != None:
            return True
        return False
    
################################################


################### Testing ###################
def test_position_available():
    g1 = Game()
    assert g1.position_available(0, 0) == True

    g2 = Game()
    g2._Game__board[0][0] = 'X'
    assert g2.position_available(0, 0) == False

    g3 = Game()
    g3._Game__board[0][0] = 'O'
    assert g3.position_available(0, 0) == False

def test_move():
    g1 = Game()
    p1 = Player('Cornelius','C')

    g1._Game__board[1][1] = 'X'
    assert g1.move(1, 1, p1) == False

    g2 = Game()
    assert g2.move(1, 1, p1) == True

def test_is_full():
    g1 = Game()
    g1._Game__board = [['X','X','X'],['X','X','X'],['X','X','X']]
    assert g1.is_full() == True

    g2 = Game()
    g2._Game__board = [['O','O','O'],['O','O','O'],['O','O','O']]
    assert g2.is_full() == True

    g3 = Game()
    g3._Game__board = [['-','-','-'],['-','-','-'],['-','-','-']]
    assert g3.is_full() == False

    g4 = Game()
    g4._Game__board = [['X','X','X'],['X','X','-'],['X','X','X']]
    assert g4.is_full() == False

    g5 = Game()
    g5._Game__board = [['X','-','X'],['X','X','X'],['X','X','X']]
    assert g5.is_full() == False

    g6 = Game()
    g6._Game__board = [['X','X','X'],['X','X','X'],['X','X','-']]
    assert g6.is_full() == False

def test_calc_winner():
    g1 = Game()
    p1 = Player('JakeBrake','X')
    g1._Game__board = [['X','X','X'],['-','-','-'],['-','-','-']]
    assert g1.calc_winner(p1) == 'X'

    g2 = Game()
    p2 = Player('Olander','O')
    g2._Game__board = [['O','O','O'],['-','-','-'],['-','-','-']]
    assert g2.calc_winner(p2) == 'O'

    g3 = Game()
    p3 = Player('Cobb','O')
    g3._Game__board = [['O','-','-'],['O','-','-'],['O','-','-']]
    assert g3.calc_winner(p3) == 'O'

    g4 = Game()
    p4 = Player('Yennifer','O')
    g4._Game__board = [['O','-','-'],['-','O','-'],['-','-','O']]
    assert g4.calc_winner(p4) == 'O'

    g5 = Game()
    p5 = Player('Petra','O')
    g5._Game__board = [['-','-','O'],['-','O','-'],['O','-','-']]
    assert g5.calc_winner(p5) == 'O'

def test_is_game_over():
    g1 = Game()
    p1 = Player('Cavill','X')
    assert g1.is_game_over(p1) == False

    g2 = Game()
    g2._Game__board = [['O','-','-'],['-','O','-'],['-','-','O']]
    assert g2.is_game_over(p1) == False

    g3 = Game()
    g3._Game__board = [['X','X','X'],['X','X','X'],['X','X','X']]
    assert g3.is_game_over(p1) == True

###############################################



def main():

    # games = {}
    # game_counter = 1
    # ###
    # Insert while loop start here. Indent rest of existing primary while loop.
    # # run these at end of game when someone wants to play another.
    # Will need to change 'g1' to 'games[game_counter]' to be using the current game.
    # games[game_counter] = Game()
    # game_counter += 1
    # ###

    g1 = Game()

    #############################################################################################
    # See if we can figure out how to have users input the values for the Player object name.
    # Also, Game object name. Probably not possible.
    # Don't think it is possible or trivial for the Game instance. We could add a 'name' member variable for Game to identify each game.
    # But should be able to prompt user for 'name' and 'token' for their instances.
    #############################################################################################

    # p1 = Player('Dezzi', 'X')
    # p2 = Player('Bunbun', 'O')

    # Allow user input for names and tokens.
    print("First player:")
    p1_name = input("Name: ")
    p1_token = input("Enter your token symbol: ")

    p1 = Player(p1_name,p1_token)

    print("Second player:")
    p2_name = input("Name: ")
    p2_token = input("Enter your token symbol: ")

    p2 = Player(p2_name,p2_token)

    g1.print_player_info(p1)
    g1.print_player_info(p2)
    
    # A dictionary of player names and Player objects, used below in some logic.
    players = {p1.name: p1, p2.name: p2}

    # Added functionality where a random generator picks who goes first.
    # Display candy to show the random selector is 'thining'.
    print("Setting up board and choosing start player.")
    cycle = 1
    number_of_cycles = 3
    while cycle <= number_of_cycles:
        scanner_width = 45
        # scanner_field = ' ' * scanner_width
        time_delay = .005
        # Draw the spaces.
        for _ in range(scanner_width):
            print(' ', end='', flush=True)
            time.sleep(time_delay)
        # Draw the backspaces.
        for _ in range(scanner_width):
            print('\b', end='', flush=True)
            time.sleep(time_delay)
        cycle += 1

    # Using random to choose one of the players.
    player_chosen = random.choice([p1.name, p2.name])
    print(f"First up: {player_chosen}!")
    players_turn = player_chosen

    # Print the initial board.
    print(g1)

    while True:

        ###### Prompt for input and attempt move ######
        while True:
            # Prompt player n for their move.
            print()
            print(f"{players[players_turn].token} : {players[players_turn].name}'s turn.")
            y_input = input(f"Choose your row: ")
            x_input = input(f"Choose your column: ")
            # TODO: Move this logic to function, maybe?
            # Verify numeric and in proper range.
            # If not valid, go back and re-prompt.
            if not x_input.isnumeric() or not y_input.isnumeric():
                print("Please enter numeric values.")
                continue
            desired_x_position = int(x_input)
            desired_y_position = int(y_input)
            if not (1 <= desired_x_position <= 3) or not (1 <= desired_y_position <= 3):
                print("Please enter numbers between and including 1 and 3.")
                continue
            break
            
        # Move if available.
        if not g1.move(desired_x_position - 1, desired_y_position - 1, players[players_turn]):
            print("Space already occupied. Please try another position.")
            continue
        ###############################################

        print(g1)

        # Check for win:
            # If win:
                # Announce winner
                # End game
            # Else:
                # Proceed
        ############ Check for winner ############
        calc_winner_result = g1.calc_winner(players[players_turn])
        if calc_winner_result:
            print(f"WINNER: {players[players_turn].token} : {players[players_turn].name}!!!")
            break
        ##########################################

        # Check for full board:
            # If full:
                # Announce game is 'draw' or 'cat'
                # End game
            # Else:
                # Proceed
        ##########################################
        if g1.is_full():
            print("Game is a draw.\nCat's game! MEOW!!!")
            break
        ##########################################

        # Check is_game_over:
            # If over:
                # Announce game is over
                # End game.
            # Else:
                # Proceed
        ##########################################
        if g1.is_game_over(players[players_turn]):
            print("Game over!")
            break
        ##########################################

        # Toggle player turn
        ##########################################
        # Toggle player turn to other player.
        if players_turn == p1.name:
            players_turn = p2.name
        # elif players_turn == p2.name:
        #     players_turn = p1.name
        else:
            players_turn = p1.name
        ##########################################

main()