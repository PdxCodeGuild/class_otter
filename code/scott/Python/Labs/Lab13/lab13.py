'''
*********************************************
*              PDXCode Guild                *
*  Full-Stack Python/JavaScript Day Class   *
*               Class_Otter                 *
*              Scott Madden                 *
*           Lab 13 - Tic-Tac-Toe            *
*              22/January/2022              *
*                                           *
*********************************************
'''



class Player:     
    def __init__(self, name='', token= ''):
        self.name = name
        self.token = token
        
    def __repr__(self):
            return f'Player("{self.name}","{self.token}")'
        
        
        
class Game:
    def __init__(self):
        self.board = {"7": " ", "8": " ", "9": " ", "4": " ", "5": " ", "6": " ", "1": " ", "2": " ", "3": " "} 
        
   # __repr__() Returns a representation of the game self.board
    def __repr__(self):
        print(self.board["7"] + "|" + self.board["8"] + "|" + self.board["9"] + "|")
        print("-+-+-")
        print(self.board["4"] + "|" + self.board["5"] + "|" + self.board["6"] + "|")
        print("-+-+-")
        print(self.board["1"] + "|" + self.board["2"] + "|" + self.board["3"] + "|")


    def move(self, player):
        # self.position = position
        # self.player = player
   
        while True:
            num = input('enter a number position (1-9) to place your token: ')     
            if self.board[num] != " ":
                print("Chose an unoccupied position from 1 - 9:")
                continue
            else:
                self.board[num] = player.token
                break

    
    #calculates which player wins
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
 
        
    # is_full() Returns True if the game self.board is full.
    def is_full(self):
        for i in self.board:
            if self.board[i] == " ": 
                return False
        return True

    def is_game_over(self):
        winner = self.calc_winner()
        full = self.is_full()
        
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

game = Game()
while True:
    print("This is tic-tac-toe!")
    play = input("Do you want to play a game? Y or N: ").upper()
    if play == "Y":
        p_name1 = input("Please enter Player1's name: ")
        while True:
            token1 = input("'X' or 'O'?: ").upper()
            if token1 != "X" and token1 != "O":
                print("That isn't a valid game token. please select either 'X' or 'O':")
            elif token1 == "X" or token1 == "O": 
                break
            else:
                continue
            
        p_name2 = input("Please enter Player2's name: ")
        token2 = token2_(token1)

        player1 = Player(p_name1, token1)
        player2 = Player(p_name2, token2)
            
        turn = 0
        
        for i in range(10):
            turn += 1
            print(game.__repr__())
        

            if turn % 2 == 1:
                print("Player1's turn")
                game.move(player1)
                current_player = p_name1
                
            else:
                print("Player2's turn")
                game.move(player2)
                current_player = p_name2

            if game.is_game_over():
                game.__repr__()
                print(f"{game.calc_winner()} won!")
                break
        else:
            print("Good bye!")
    break
        
