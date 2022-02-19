class Player:
        def __init__(self, name, token):
            self.name = name
            self.token = token
        def __repr__(self):
            return f"{self.name} using {self.token}"
chosen = input('Player 1 token X or O: ')
if chosen == 'x' or 'X':
    p1token = 'X'
    p2token = 'O'              
elif chosen == 'o' or 'O':
    p1token = 'O'
    p2token = 'X'
else:
    print('Retry Later')
player1 = Player('Player 1', p1token)
player2 = Player('Player 2', p2token)
print(player1)
print(player2)

class Game:
    def __init__(self):
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ',]]
    def __repr__(self):
        return f"{self.board[0][0]}|{self.board[0][1]}|{self.board[0][2]}\n{self.board[1][0]}|{self.board[1][1]}|{self.board[1][2]}\n{self.board[2][0]}|{self.board[2][1]}|{self.board[2][2]}"
    #print(start) how to print out this
    ttt_dic = {
        1 : [0, 0],
        2 : [0, 1],
        3 : [0, 2],
        4 : [1, 0],
        5 : [1, 1],
        6 : [1, 2],
        7 : [2, 0],
        8 : [2, 1],
        9 : [2,2]
    }
    def move(self, row, col, token):
        if self.board[row][col] == ' ':
            self.board[row][col] = token
            return True
        else:
            return False
    def calc_winner(self, token):
        x1 = self.ttt_dic[1][0]
        y1 = self.ttt_dic[1][1]
        x2 = self.ttt_dic[2][0]
        y2 = self.ttt_dic[2][1]
        x3 = self.ttt_dic[3][0]
        y3 = self.ttt_dic[3][1]
        x4 = self.ttt_dic[4][0]
        y4 = self.ttt_dic[4][1]
        x5 = self.ttt_dic[5][0]
        y5 = self.ttt_dic[5][1]
        x6 = self.ttt_dic[6][0]
        y6 = self.ttt_dic[6][1]
        x7 = self.ttt_dic[7][0]
        y7 = self.ttt_dic[7][1]
        x8 = self.ttt_dic[8][0]
        y8 = self.ttt_dic[8][1]
        x9 = self.ttt_dic[9][0]
        y9 = self.ttt_dic[9][1]
        if self.board[x1][y1] == token and self.board[x2][y2] == token and self.board[x3][y3] == token:
            print('winner across top')
            return True
        elif self.board[x4][y4] == token and self.board[x5][y5] == token and self.board[x6][y6] == token:
            print('winner across middle')
            return True
        elif self.board[x7][y7] == token and self.board[x8][y8] == token and self.board[x9][y9] == token:
            print('winner across bottom')
            return True
        elif self.board[x1][y1] == token and self.board[x4][y4] == token and self.board[x7][y7] == token:
            print('winner down left')
            return True
        elif self.board[x2][y2] == token and self.board[x5][y5] == token and self.board[x8][y8] == token:
            print('winner down middle')
            return True
        elif self.board[x3][y3] == token and self.board[x6][y6] == token and self.board[x9][y9] == token:
            print('winner down right')
            return True
        elif self.board[x1][y1] == token and self.board[x5][y5] == token and self.board[x9][y9] == token:
            print('winner diagonal top left to bottom right')
            return True
        elif self.board[x3][y3] == token and self.board[x5][y5] == token and self.board[x7][y7] == token:
            print('winner diagonal top right to bottom left ')
            return True
        else:
            return False
    def is_full(self):
        for i in range(1, 10):
            x = self.ttt_dic[i][0]
            # print(x)
            y = self.ttt_dic[i][1]
            # print(y)
            position = self.board[x][y]
            # print(position)
            if position == ' ':
                return False
        return True
    def is_game_over(self):
        for i in range(1, 10):
            x = self.ttt_dic[i][0]
            # print(x)
            y = self.ttt_dic[i][1]
            # print(y)
            position = self.board[x][y]
            # print(position)
            if position == 'X' or 'O':
                return False
        return True
start = Game()
print(start)
while True:
    print("X player move enter coorindate ie (0,0) is top left: ")
    x_move = input("Enter row coordinate: ")
    x_move = int(x_move)
    y_move = input("Enter column coordinate: ")
    y_move = int(y_move)
    if p1token == 'X':
        if start.move(x_move, y_move, p1token) == True:
            start.move(x_move, y_move, p1token)
        elif start.move(x_move, y_move, p1token) == False:
            print('Invalid Input')
    elif p1token == 'O':
        if start.move(x_move, y_move, p1token) == True:
            start.move(x_move, y_move, p1token)
        elif start.move(x_move, y_move, p1token) == False:
            print('Invalid Input')
    print(start)
    if start.is_game_over() == True:
        print('Is the Game over?\nTrue')
    if start.calc_winner(p1token) == True:
        print('Player 1 Wins!')
        break
    if start.calc_winner(p2token) == True:
        print('Player 2 Wins!')
        break
    if start.is_full() == True:
        print('Tie')
        break
    print("O player move enter coorindate ie (0,0) is top left: ")
    cx_move = input("Enter row coordinate: ")
    cx_move = int(cx_move)
    cy_move = input("Enter column coordinate: ")
    cy_move = int(cy_move)
    if p2token == 'X':
        if start.move(cx_move, cy_move, p2token) == True:
            start.move(cx_move, cy_move, p2token)
        elif start.move(cx_move, cy_move, p2token) == False:
            print('Invalid Input')
    elif p2token == 'O':
        if start.move(cx_move, cy_move, p2token) == True:
            start.move(cx_move, cy_move, p2token)
        elif start.move(cx_move, cy_move, p2token) == False:
            print('Invalid Input')
        print(start)
    if start.is_game_over() == True:
        print('Is the Game over?\nTrue')
    if start.calc_winner(p1token) == True:
        print('Player 1 Wins!')
        break
    if start.calc_winner(p2token) == True:
        print('Player 2 Wins!')
        break
    if start.is_full() == True:
        print('Tie')
        break