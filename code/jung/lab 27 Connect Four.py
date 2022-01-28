# row_count = 6
# column_count = 7

class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Game:
    ROWS = 7
    COLUMNS = 6

    def __init__(self):
        self.board = []
        for i in range(6):
            row = []
            for j in range(7):
                row.append(" ")
            self.board.append(row)
        # return self.board

     
    def __repr__(self):
        for k in self.board:
            print("|" + "|".join(k) + "|")


    def get_height(self, position):
        for k in range(self.COLUMNS -1, -1, -1)
        if self.board[k][position] == " ":
            return k
        return False

    def place_piece(self, player_color, position):
        player = Player()
        height = self.get_height(position)
        if type(height) == bool:
            print("Columns are full. Select another: ")
            return False
        self.board[height][position] = Player(player_color)

    def check_win(self):
        


        

    # def is_valid(board, col):
    #     return board[5][col] == " "


        

    # def move(self, player, position):
    
    # def calc_winner(self):
    
    # def is_full(self):
    
    # def is_game_over(self):


game = Game()

print(game.__repr__())


# game_over = False
# turn = 0

# while not game_over:
#     if turn == 0: 
#         col = int(input("Player 1 Make your selection (0-6): "))

#     else:
#         col = int(input("Player 2 Make your selection (0-6): "))

#     turn += 1
#     turn = turn % 2