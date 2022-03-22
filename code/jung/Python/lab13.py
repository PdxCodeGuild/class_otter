class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token
    
    def __repr__(self):
        return self.name


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



    # move(x, y, player) Place a player's token character string at a given coordinate (top-left is 0, 0), x is horizontal position, y is vertical position.
    def move(self, player):
        while True:
            number = input("Where do you want to put?: ")
            if self.board[number] != " ":
                print("Other place")
                continue
            else:
                self.board[number] = player.token
                break
            



        


    # calc_winner() What token character string has won or None if no one has.
    def calc_winner(self):

        if self.board["7"] == self.board["8"] == self.board["9"] != " ":
            return self.board["7"]
        elif self.board["4"] == self.board["5"] == self.board["6"] != " ":
            return self.board["4"]
        elif self.board["1"] == self.board["2"] == self.board["3"] != " ":
            return self.board["1"]
        elif self.board["1"] == self.board["4"] == self.board["7"] != " ":
            return self.board["1"]
        elif self.board["2"] == self.board["5"] == self.board["8"] != " ":
            return self.board["2"]
        elif self.board["3"] == self.board["6"] == self.board["9"] != " ":
            return self.board["3"]
        elif self.board["1"] == self.board["5"] == self.board["9"] != " ":
            return self.board["1"]
        elif self.board["3"] == self.board["5"] == self.board["7"] != " ":
            return self.board["3"]
        else:
            return None

    # is_full() Returns true if the game self.board is full.
    def is_full(self):
        for i in self.board:
            if self.board[i] == " ": 
                return False
        return True
    #if you find any blank spaces, return false: otherwise return True

    # is_game_over() Returns true if the game self.board is full or a player has won.
    def is_game_over(self):
        winner = self.calc_winner()
        full = self.is_full()

        # if self.calc_winner():
        #     # print(f"{self.calc_winner()} won")

        if winner or full:
            return True
        else:
            return False





def token2_(token1):
    while True:
        if token1 == "X":    
            return "O"
        elif token1 =="O":
            return "X"



while True:
    game = Game()   
    ask = input("Do you want to play a game? Y or N: ").upper()
    # print(ask)
    if ask == "Y":
        name1 = input("Player1's name: ")
        while True:
            token1 = input("'X' or 'O'?: ").upper()
            if token1 != "X" and token1 != "O":
                print("That's not a valid command.")
            elif token1 == "X" or token1 == "O": 
                break
            else:
                continue
            
        name2 = input("Player2's name: ")
        token2 = token2_(token1)

        player1 = Player(name1, token1)
        player2 = Player(name2, token2)

        turn = 0


        for i in range(10):
            turn += 1
            game.__repr__()


            if turn % 2 == 1:
                print("Player1's turn")
                game.move(player1)
                current_player = name1
                
            else:
                print("Player2's turn")
                game.move(player2)
                current_player = name2

            if game.is_game_over():
                game.__repr__()
                print(f"{game.calc_winner()} won!")
                break
    else:
        print("Good job!")
        break




