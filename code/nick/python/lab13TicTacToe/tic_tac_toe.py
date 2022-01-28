class Player:
    def __init__(self, player_name, token):
        self.player_name = player_name
        self.token = token

class Game:
    def __init__(self):
        self.game_board = [
                ['_','_','_'],
                ['_','_','_'],
                ['_','_','_'],
                ]
    def __repr__(self):
        for row in self.game_board:
            for spot in row:
                    print(spot, end='')
                    
        
    def move(self, x, y, player):
        self.game_board[x][y] = player
  


board = Game()
print(board.move(2,2,'x'),board.__repr__())