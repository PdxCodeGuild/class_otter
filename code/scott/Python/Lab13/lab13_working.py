class Player:     
    def __init__(self, name='', token= ''):
        self.name = name
        self.token = token
        return f'Player("{self.name}","{self.token}")'
    def __repr__(self):
            return f'Player("{self.name}","{self.token}")'
        
        
        
class Game:
    def __init__(self, board):
        self.board = board
        board = {0: " ", 1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " "}

        b = self.board
        line1 = b[0] + " | " + b[1] + " | " + b[2] + "     1 | 2 | 3"
        line2 = '-+-+-'
        line3 = b[3] + " | " + b[4] + " | " + b[5] + "     4 | 5 | 6"
        line4 = '-+-+-'
        line5 = b[6] + " | " + b[7] + " | " + b[8] + "     7 | 8 | 9"
        return line1 + '\n' + line2 + '\n' + line3 + '\n' + line4 + '\n' + line5

        
    def __repr__(self):
        pass



    def move(self, position, player = 0):
        self.position = position
        self.player = turn
        
        while True:
            print("Please enter X and Y coordinates.")
            


    #calculates which player wins
    def calc_winner(self):
        wins = [[1,2,3],[4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [7,5,3]]
        for win in wins:
            wincount1 = 0
            wincount2 = 0
            for num in win:
                if self.board[num] == "X":
                    wincount1 += 1
                if self.board[num] == "O":
                    wincount2 += 1
            if wincount1 == 3 or wincount2 == 3:
                return "winner"
            # else:
               #  return "no winner"
        return "no winner"

    def is_full(self):
#        print('is full ran')
        calc = self.calc_winner()
        if self.player == 9 and calc == "no winner":
            
            return True

        #Determines if both conditions; board full and no winner are met (board full condition)
               
    def is_game_over():

        findwinner = Game.calc_winner()
        full = Game.is_full()
        if full == True:
            return True
        elif findwinner == "winner":
            return True
        else:
            return False


Game = Game()

def main():
    print("This is tic-tac-toe!")
    print(Game.board)
    players = []
    player1=Player(input("Please enter your name? You will be the 'X' Player:"), "X")
    player2=Player(input("Please enter your name? You will be the 'O' Player:"), "O")
    players.append(player1)
    players.append(player2)


    while not Game.is_game_over() == True:
        active_player = players[Game.turn %2]
        print(Game.turn)
        print(Game)
        position = int(input(f'{active_player} enter a number position (1-9) to place your token: '))
        print(Game.move(position, active_player))
        # Game.is_game_over()
    # print(Game)