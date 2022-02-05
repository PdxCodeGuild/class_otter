
class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token

class Game:
    def __init__(self):
        self.board = [
            [' ',' ',' '],
            [' ',' ',' '],
            [' ',' ',' ']
        ]

    def __repr__(self):  
        b = ''
        for row in self.board:
            b += '|'.join(row)
            b += '\n'
        return b
        
    def move(self, x, y, token):
        if self.board[y][x] != ' ':
            return 'invalid move'
        else:
            self.board[x][y] = token
    
    def calc_winner(self):
        if self.board[0][0]==self.board[0][1]==self.board==[0][2]:
            return self.board[0][0]


    
    # def is_full():
    
    # def is_game_over():
  


# player_1 = Player(input('player 1 name: '), 'X')
# player_2 = Player(input('Player 2 name: '), 'O')
# print(player_1.name,player_1.token)
# print(player_2.name,player_2.token)
# print(repr(game.move(0,0, player_1.token)))
# print(repr(game))

while True:
    board = Game()
    first = Player(input('player one: '),'X')
    second = Player(input('player two: '),'O')
    print(first.name, first.token)
    print(second.name, second.token)
    print('Coordinates are 0, 1, and 2.\n0,0 being the top left of the board. ')
    while True:
        x = input('enter coordinates x: ').strip()
        y = input('enter coordinate y: ').strip()
        x=int(x)
        y=int(y)
        board.move(x,y,first.token)
        print(repr(board))