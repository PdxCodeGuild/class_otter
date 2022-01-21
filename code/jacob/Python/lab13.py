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
            return 'Invalid'
        
        else:
            self.board[a][b] = token
    
    def calc_winner(self):
        
        if self.board[0][0] == self.board[0][1] == self.board[0][2] and self.board[0][0] != ' ':
            return self.board[0][0]

        elif self.board[1][0] == self.board[1][1] == self.board[1][2] and self.board[1][0] != ' ':
            return self.board[1][0]

        elif self.board[2][0] == self.board[2][1] == self.board[2][2] and self.board[2][0] != ' ':
            return self.board[2][0]
        
        elif self.board[0][0] == self.board[1][0] == self.board[2][0] and self.board[0][0] != ' ':
            return self.board[0][0]
        
        elif self.board[0][1] == self.board[1][1] == self.board[2][1] and self.board[0][1] != ' ':
            return self.board[0][1]
        
        elif self.board[0][2] == self.board[1][2] == self.board[2][2] and self.board[0][2] != ' ':
            return self.board[0][2]
        
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

        if self.is_full() == False:
            return False
        else:
            return True
        


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

while board.is_game_over() == False:
    
    print(board)
    print(display)
    
    move1 = int(input('Enter your move: '))
    
    while move1 > 9:
        print('Please choose a valid space between 1 to 9.')
        move1 = int(input('Choose a valid space: '))

    a, b = game_board_coord[move1]
    move1 = board.move(a, b, player1.token)
    
    while move1 == 'Invalid':
        print('Invalid move, please choose an open spot!')
        move1 = int(input(f'{player1} enter your move: '))
        a, b = game_board_coord[move1]
        move1 = board.move(a, b, player1.token)
    
    if board.calc_winner() == 'X':
        print(f'{player1} wins!')
        break
    
    if board.is_full() == True:
        print('Game is over with no winner!')
        break    
    
    print(board)
    print(display)
    
    move2 = int(input('Enter your move: '))
    
    while move2 > 9:
        print('Please choose a valid space between 1 to 9.')
        move2 = int(input('Choose a valid space: '))

    a, b = game_board_coord[move2]
    move2 = board.move(a, b, player2.token)
    print(board)
    
    while move2 == 'Invalid':
        print('Invalid move, please choose an open spot!')
        move1 = int(input(f'{player2} enter your move: '))
        a, b = game_board_coord[move2]
        move1 = board.move(a, b, player2.token)
    
    if board.calc_winner() == 'O':
        print(f'{player2} wins!')
        break

