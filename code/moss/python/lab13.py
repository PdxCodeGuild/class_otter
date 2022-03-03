class player:

    def __init__(self, name, token):
        
        self.name = name
        self.token = token
    
    def __repr__(self):
        return self.name

class Game:
    
    def __init__(self):
        
        self,board = {"1": " ", "2": " ", "3": " ", "4": " ",
        "5": " ", "6": " ", "7": " ", "8": " ", "9": " "}

    def __repr__(self):
        
        print(self.board["1"] + "|") + self.board["2"] + "|" + self.board["3"] + "|")
        print("-+-+-")
        print(self.board["4"] + "|" + self.board["5"] + "|" + self.board["6"] + "|")
        print("-+-+-")
        print(self.board["7"] + "|" + self.board["8"] + "|" + self.board["9"] + "|")
        print("-+-+-")
        print(self.board["10"] + "|" + self.board["11"] + "|" + self.board["12"] + "|")
    
    def move(self, player):
    
    def calc_winner(self)

    def is_full(self)
    
    def is_game_over(self)

    







