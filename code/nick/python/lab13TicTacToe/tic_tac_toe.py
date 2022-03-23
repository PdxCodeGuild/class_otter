
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
        if self.board[x][y] != ' ':
            return 'invalid move'
        else:
            self.board[x][y] = token
    
    def calc_winner(self):
        if (self.board[0][0]==self.board[0][1]==self.board[0][2]) and self.board[0][0] != ' ':
            return self.board[0][0] #top row
        if (self.board[1][0]==self.board[1][1]==self.board[1][2]) and self.board[1][2] != ' ':
            return self.board[1][0] #middle row
        if (self.board[2][0]==self.board[2][1]==self.board[2][2]) and self.board[2][0] != ' ':
            return self.board[2][0] #bottom row
        if (self.board[0][0]==self.board[1][0]==self.board[2][0]) and self.board[0][0] != ' ':
            return self.board[0][0] #left col
        if (self.board[0][1]==self.board[1][1]==self.board[2][1]) and self.board[0][1] != ' ':
            return self.board[0][1] #middle col
        if (self.board[0][2]==self.board[1][2]==self.board[2][2]) and self.board[0][2] != ' ':
            return self.board[0][2] #right col
        if (self.board[0][0]==self.board[1][1]==self.board[2][2]) and self.board[0][0] != ' ':
            return self.board[0][0] #diagnol 1
        if (self.board[0][2]==self.board[1][1]==self.board[2][0]) and self.board[0][2] != ' ':
            return self.board[0][2] #diagnol 2


    def is_full(self):
        for row in self.board:
            if any(item==' ' for item in row):
                return False
        return True

    
    def is_game_over(self):
            return self.calc_winner() or self.is_full()
  
# player_1 = Player(input('player 1 name: '), 'X')
# player_2 = Player(input('Player 2 name: '), 'O')
# print(player_1.name,player_1.token)
# print(player_2.name,player_2.token)
# print(repr(game.move(0,0, player_1.token)))
# print(repr(game))
'''
'0,0'|'0,1'|'0,2'
-----|-----|-----
'1,0'|'1,1'|'1,2'
-----|-----|-----
'2,0'|'2,1'|'2,2'

'''

while True:
    spots = {
        1:(0,0), 2:(0,1), 3:(0,2), 
        4:(1,0), 5:(1,1), 6:(1,2), 
        7:(2,0), 8:(2,1), 9:(2,2)}
    board = Game()
    first_player = Player(input('player one: '),'X')
    second_player = Player(input('player two: '),'O')
    print(first_player.name, first_player.token)
    print(second_player.name, second_player.token)
    rounds  = 1

    while not board.is_game_over():
        current_player = first_player if rounds % 2 else second_player
        
        while True:
            move = input(f'{current_player.name}: enter your move: ').strip()
            move = int(move)
            x,y = spots[move]
            move = board.move(x,y,current_player.token)
            print(repr(board))
            rounds +=1
            break
    if board.is_full():
        print('full board new game. ')
    elif board.is_game_over():
        print(board.calc_winner(),f'{current_player.name} won')