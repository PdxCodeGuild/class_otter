class player:     
    def __init__(self, name='', token= ''):
        self.name = name
        self.token = token
        return f'Player("{self.name}","{self.token}")'

    def __str__(self):
            return f'Player("{self.name}","{self.token}")'


        #ask for player_name and select 1 or 2 to play as 'X' or 'O'


class game:     
    def __init__(self, board):
        self.board = board

    def __repr__():
        print(board)

    def move(self, x, y, player)





    #ask for player_name and select 1 or 2 to play as 'X' or 'O'

game = game()

def main():
    players = []
    player1=player(input("Please enter your name? You will be the 'X' Player:"), "X")
    player2=player(input("Please enter your name? You will be the 'O' Player:"), "O")
    players.append(player1)
    players.append(player2)
