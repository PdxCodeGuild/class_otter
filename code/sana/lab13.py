pchosen = input('x or o?')
class Player:
    def picktoken(chosen):
        if chosen == 'x':
            moves = 'X'
            return moves 
        elif chosen == 'o':
            moves = 'O'
            return moves

player = Player()
class Game:
    def __init__(self):
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ',]]
    def display(self):
        print(f"{self.board[0][0]}|{self.board[0][1]}|{self.board[0][2]}")
        print(f"{self.board[1][0]}|{self.board[1][1]}|{self.board[2][2]}")
        print(f"{self.board[2][0]}|{self.board[2][1]}|{self.board[2][2]}")
    def move(self, row, col, token):
        if self.board[row][col] == ' ':
            self.board[row][col] = token
            return True
        else:
            return False
    def is_full(self):
        for row in self.board:
            for position in row:
                if position == ' ':
                    return False
        return True
    def is_game_over(self):
        for row in self.board:
            for position in row:
                if position == 'X' or position == 'O':
                    return True
        return False
    def calc_winner(self):
        win = None
        n = len(self.board)
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win
        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False      


start = Game()
start.display()
ptoken = player.picktoken(pchosen)
while True:
    print("X player move enter coorindate ie (0,0) is top left: ")
    x_move = input("Enter row coordinate: ")
    x_move = int(x_move)
    y_move = input("Enter column coordinate: ")
    y_move = int(y_move)
    if start.move(x_move, y_move, ptoken) == False:
        print('Retry')
        pass
    start.display()
    print("X player move enter coorindate ie (0,0) is top left: ")
    cx_move = input("Enter row coordinate: ")
    cx_move = int(cx_move)
    cy_move = input("Enter column coordinate: ")
    cy_move = int(cy_move)
    if ptoken == 'X':
        ctoken = 'O'
    elif ptoken == 'O':
        ctoken = 'X'
    if start.move(cx_move, cy_move, ctoken) == False:
        print('Retry')
        pass
    if start.calc_winner():
        print('winner')
        start.is_game_over()
        break
    if start.is_full():
        print('Tie')
        start.is_game_over()
        break
start.display() 
start.is_game_over()
