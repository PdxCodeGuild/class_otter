"""
Lab 13: Tic-Tac-Toe
"""

class Player:
    
    def __init__(self, player, token):
        self.player = player
        self.token = token
    
    def __repr__(self):
        return self.player

class Game:
    
    def  __init__(self):
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        
    def __repr__(self):
        game_board = ''
        for x in self.board:
            game_board += '|'.join(x)
            game_board += '\n'     
        return game_board

    def move(self, a, b, token):
        if self.board[a][b] != ' ':
            return 'Invalid. Choose again'
        else:
            self.board[a][b] = token
    
    def calc_winner(self):
        if self.board[0][0] == self.board[0][1] == self.board[0][2] and self.board[0][0] != ' ':
            return self.board[0][0]

        elif self.board[1][0] == self.board[1][1] == self.board[1][2] and self.board[1][0] != ' ':
            return self.board[1][0]

        elif self.board[2][0] == self.board[2][1] == self.board[2][2] and self.board[2][0] != ' ':
            return self.board[2][0]

        elif self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != ' ':
            return self.board[0][0]
        
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != ' ':
            return self.board[0][2]

        else:
            return None
        
    def is_full(self):

        for x in self.board:
            for i in x:
                if i == ' ':
                    return False
        return True

    def is_game_over(self):
        return self.calc_winner() or self.is_full()


game_board_coord = {1:(0,0), 2:(0,1), 3:(0,2),
                  4:(1,0), 5:(1,1), 6:(1,2),
                  7:(2,0), 8:(2,1), 9:(2,2)}

display_board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
display = ''    
for x in display_board:
    display += '|'.join(x)
    display += '\n'

board = Game()
player1 = Player(input('Player one: '), 'X')
player2 = Player(input('Player two: '), 'O')

while not board.is_game_over():
    print(display)
    move1 = int(input('Enter your move: '))

    a, b = game_board_coord[move1]
    move1 = board.move(a, b, player1.token)
    
    if board.calc_winner() == 'X':
        print(f'{player1} wins!')
        break

    print(board)
    print(display)
    
    move2 = int(input('Enter your move: '))

    a, b = game_board_coord[move2]
    move2 = board.move(a, b, player2.token)
    print(board)

    if board.calc_winner() == 'O':
        print(f'{player2} wins!')
        break

