class player:     
    def __init__(self, name='', token= ''):
        self.name = name
        self.token = token
        return f'Player("{self.name}","{self.token}")'
    def __repr__(self):
            return f'Player("{self.name}","{self.token}")'
        
        
        
class Game:
    def __init__(self, turn=0):
        
        self.turn = turn
        self.board = {0: " ", 1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " "}

    def __repr__(self):
       
        b = self.board
        line1 = b[0] + " | " + b[1] + " | " + b[2] + "     1 | 2 | 3"
        line2 = '-+-+-'
        line3 = b[3] + " | " + b[4] + " | " + b[5] + "     4 | 5 | 6"
        line4 = '-+-+-'
        line5 = b[6] + " | " + b[7] + " | " + b[8] + "     7 | 8 | 9"
        return line1 + '\n' + line2 + '\n' + line3 + '\n' + line4 + '\n' + line5

    
    def move(self, x, y, player):
        b = self.board
        b[x y position] = player.token
      
        self.turn += 1
        return command
    
    #calculates which player wins
    def calc_winner(self):
        print('is calc ran')

        b = self.board
      
        
        wins = [[1,2,3],[4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [7,5,3]]
        for win in wins:
            wincount1 = 0
            wincount2 = 0
            for num in win:
                if b[num] == "X":
                    wincount1 += 1
                if b[num] == "O":
                    wincount2 += 1
            if wincount1 == 3 or wincount2 == 3:
                return "winner"
            # else:
               #  return "no winner"
        return "no winner"

    def is_full(self):
#        print('is full ran')
        calc = self.calc_winner()
        if self.turn == 9 and calc == "no winner":
            
            return True

        #Determines if condition board full and  no winner'''
       
    def is_game_over(self):

        findwinner = self.calc_winner()
        full = self.is_full()
        if full == True:
            return True
        elif findwinner == "winner":
            return True
        
        else:
            return False

        # if findwinner != "no winner" and full == True:
        #     return True
        # else:
        #     return False

        # if full == True:
        #     return True
        # else:
        #      return False
        #returns true if board full condition or a player wins


    def display_board(board):
            print("\n")
            print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
            print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
            print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
            print("\n")

game = Game()


    # Show the initial game board


def main():
    print("This is tic-tac-toe!")
    players = []
    player1=player(input("Please enter your name? You will be the 'X' Player:"), "X")
    player2=player(input("Please enter your name? You will be the 'O' Player:"), "O")
    players.append(player1)
    players.append(player2)
    print(players)

    # print(game)
    while not game.is_game_over() == True:
        active_player = players[game.turn %2]
        print(game.turn)
        print(game)
        command = int(input(f'{active_player.name} enter a number position (1-9) to place your token: '))
        print(game.move(command, active_player))
        game.is_game_over()
    print(game)
    
# if __name__ == '__main__':
#     main()