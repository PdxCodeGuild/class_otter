class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token


class Game:
    def __init__(self):
        self.board = {"7": " ", "8": " ", "9": " ",
        "4": " ", "5": " ", "6": " ",
        "1": " ", "2": " ", "3": " "
        }

    # __repr__() Returns a pretty string representation of the game self.board
    def __repr__(self):
        print(self.board["7"] + "|" + self.board["8"] + "|" + self.board["9"] + "|")
        print("-+-+-")
        print(self.board["4"] + "|" + self.board["5"] + "|" + self.board["6"] + "|")
        print("-+-+-")
        print(self.board["1"] + "|" + self.board["2"] + "|" + self.board["3"] + "|")


    # def verify_move(self):
    #     if self.board[number] = " ":


    # move(x, y, player) Place a player's token character string at a given coordinate (top-left is 0, 0), x is horizontal position, y is vertical position.
    def move(self, player):
        number = input("Where do you want to put?: ")
        self.board[number] = player.token
        


    # calc_winner() What token character string has won or None if no one has.
    def calc_winner(self):

        if self.board["7"] == self.board["8"] == self.board["9"]:
            return self.board["7"]
        elif self.board["4"] == self.board["5"] == self.board["6"]:
            return self.board["4"]
        elif self.board["1"] == self.board["2"] == self.board["3"]:
            return self.board["1"]
        elif self.board["1"] == self.board["4"] == self.board["7"]:
            return self.board["1"]
        elif self.board["2"] == self.board["5"] == self.board["8"]:
            return self.board["2"]
        elif self.board["3"] == self.board["6"] == self.board["9"]:
            return self.board["3"]
        elif self.board["1"] == self.board["5"] == self.board["9"]:
            return self.board["1"]
        elif self.board["3"] == self.board["5"] == self.board["7"]:
            return self.board["3"]
        else:
            return None

    # is_full() Returns true if the game self.board is full.
    def is_full(self):
        if self.board[number]:   #---------------------------------#
            return True
    
    # is_game_over() Returns true if the game self.board is full or a player has won.
    def is_game_over(self):
        winner = self.calc_winner()
        full = self.is_full()
        if winner or full:
            return True
        else:
            return False






game = Game()


 #---------------------------------#
def token2_(token1):
    while True:
        token1 = input("'X' or 'O'?: ").upper()

        if token1 != "X" and token1 != "O":
            print("That's not a valid command.")
        elif token1 == "X":    
            return "O"
        elif token1 =="O":
            return "X"
            


while True:

    name1 = input("Player1's name: ")
    token1 = input("'X' or 'O'?: ").upper()

    name2 = input("Player2's name: ")
    token2 = token2_(token1)

    player1 = Player(name1, token1)
    player2 = Player(name2, token2)

    turn = 0


 #---------------------------------#
    for i in range(10):
        turn += 1
        game.__repr__()

        if turn % 2 == 1:
            print("Player1's turn")
            game.move(player1)
            if game.is_game_over():
                print("game over")
        else:
            print("Player2's turn")
            game.move(player2)
            if game.is_game_over():
                print("s")
        

        # if game.is_full() == True:
        #     break

        # if game.is_game_over == True:
        #     break

        


