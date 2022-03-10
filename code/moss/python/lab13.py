import random

class TicTacToe:

    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def get_random_first_player(self):
        return random.randint(0, 1)

    def fix_spot(self, row, col, player):
        self.board[row][col] = player

    def is_player_win(self, player):
        win = None

        n = len(self.board)

        # checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # checking diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):
        self.create_board()

        player = 'X' if self.get_random_first_player() == 1 else 'O'
        while True:
            print(f"Player {player} turn")

            self.show_board()

            # taking user input
            row, col = list(
                map(int, input("Enter row and column numbers to fix spot: ").split()))
            print()

            # fixing the spot
            self.fix_spot(row - 1, col - 1, player)

            # checking whether current player is won or not
            if self.is_player_win(player):
                print(f"Player {player} wins the game!")
                break

            # checking whether the game is draw or not
            if self.is_board_filled():
                print("Match Draw!")
                break

            # swapping the turn
            player = self.swap_player_turn(player)

        # showing the final view of board
        print()
        self.show_board()


# starting the game
tic_tac_toe = TicTacToe()
tic_tac_toe.start()



# class player:

#     def __init__(self, name, token):
        
#         self.name = name
#         self.token = token
    
#     def __repr__(self):
#         return self.name

# class Game:
    
#     def __init__(self):
        
#         self,board = {"1": " ", "2": " ", "3": " ", "4": " ",
#         "5": " ", "6": " ", "7": " ", "8": " ", "9": " "}

#     def __repr__(self):
        
#         print(self.board["1"] + "|") + self.board["2"] + "|" + self.board["3"] + "|")
#         print("-+-+-")
#         print(self.board["4"] + "|" + self.board["5"] + "|" + self.board["6"] + "|")
#         print("-+-+-")
#         print(self.board["7"] + "|" + self.board["8"] + "|" + self.board["9"] + "|")
#         print("-+-+-")
#         print(self.board["10"] + "|" + self.board["11"] + "|" + self.board["12"] + "|")
    
#     def move(self, player):
    
#     def calc_winner(self)

#     def is_full(self)
    
#     def is_game_over(self)

    







