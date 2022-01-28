# Full Stack Bootcamp - Unit 01 Lab 13
# Justin Hammond, 01/11/2022


'''
Lab 13: Tic-Tac-Toe
Tic Tac Toe is a game. Players take turns placing tokens (a 'O' or 'X')
into a 3x3 grid. Whoever gets three in a row first wins.

You will write a Player class and Game class to model Tic Tac Toe, and a
function main that models gameplay taking in user inputs through REPL.

The Player class has the following properties:

name = player name
token = 'X' or 'O'
The Game class has the following properties:

board = your representation of the board
You can represent the board however you like, such as a 2D list, tuples,
or dictionary.


The Game class has the following methods:

__repr__() Returns a pretty string representation of the game board
>>> print(board)
X| | 
O|X|O
 | | 

move(x, y, player) Place a player's token character string at a given
coordinate (top-left is 0, 0), x is horizontal position, y is vertical
position.
>>> board.move(2, 1, player_1)
 | | 
 | |X
 | | 

calc_winner() What token character string has won or None if no one has.
X| | 
O|X|O
 | |X
>>> board.calc_winner()
X

is_full() Returns true if the game board is full.
X|O|X
X|X|O
O|O|X
>>> board.is_full()
True

is_game_over() Returns true if the game board is full or a player has won.
X|O|X
X|X|O
O|O|X
>>> board.is_game_over()
True

X|O|
 | |X
 | |
>>> board.is_game_over()
False
'''

class Player:
    def __init__(self, player_name, player_token):
        self.name = player_name
        self.token = player_token


class Game:
    def __init__(self):
        self.board = []
        for _ in range(3):
            self.board.append([' ' for _ in range(3)])

        self._separator = ' | '
        self._border = ' +-----------+\n'
        self._positions_remaining = 9
    
    def __repr__(self):
        result = self._border
        for y in range(3):
            for x in range(3):
                result += f'{self._separator}{self.board[x][y]}'
            result += f'{self._separator}\n'
        result += self._border
        return result
    
    def _is_position_available(self, x, y):
        return self.board[x][y] == ' '

    def _check_diagonal(self, board_layout):
        first_position = board_layout[0][0]
        if first_position == ' ':
            return None

        for x in range(2):
            x += 1
            if board_layout[x][x] != first_position:
                return None
        
        return first_position

    def _check_row(self, board_layout, row):
        first_position = board_layout[0][row]
        if first_position == ' ':
            return None

        for x in range(2):
            x += 1
            if board_layout[x][row] != first_position:
                return None
        
        return first_position

    def _transpose(self, board_layout):
        transposed_board_layout = []
        for _ in range(3):
            transposed_board_layout.append([' ' for _ in range(3)])

        for y in range(3):
            for x in range(3):
                transposed_board_layout[x][y] = board_layout[y][x]

        return transposed_board_layout


    def move(self, x, y, player):
        if self._is_position_available(x, y):
            self.board[x][y] = player.token
            self._positions_remaining -= 1
            return True
        return False

    def calc_winner(self):
        current_board = self.board
        winner = self._check_diagonal(current_board)
        if winner != None:
            return winner

        for i in range(3):
            winner = self._check_row(current_board, i)
            if winner != None:
                return winner

        transposed_board = self._transpose(current_board)
        winner = self._check_diagonal(transposed_board)
        if winner != None:
            return winner

        for i in range(3):
            winner = self._check_row(transposed_board, i)
            if winner != None:
                return winner

        return None

    def is_full(self):
        return self._positions_remaining <= 0

    def is_game_over(self):
        is_full = self.is_full()
        winner = self.calc_winner()
        return self.is_full() or self.calc_winner() != None


def main():
    def get_user_move():
        class OutOfRangeError(Exception):
            # Used when coordinate value exceeds allowable range
            pass

        while True:
            user_input = input("Where to move? [x, y]: ")
            user_input = user_input.split(',')
            results = []
            try:
                for i in range(2):
                    value = int(user_input[i].strip())
                    if value < 0 or value > 2:
                        raise OutOfRangeError
                    results.append(value)
                return results
            except OutOfRangeError as e:
                print("Values must fall in the range [0-2]")
            except:
                print("Enter your coordinates as a comma-separated pair of numbers")

    player_1 = Player('Player 1', 'X')
    player_2 = Player('Player 2', 'O')
    game = Game()

    is_player_1_turn = True
    while (game.is_game_over() != True):
        print(f'{player_1.name if is_player_1_turn else player_2.name}\'s turn')
        user_move = get_user_move()
        if not game.move(user_move[0], user_move[1], player_1 if is_player_1_turn else player_2):
            print("Invalid position")
            continue
        is_player_1_turn = not is_player_1_turn
        print(game)
    
    print(f'Winner: {game.calc_winner()}')

main()