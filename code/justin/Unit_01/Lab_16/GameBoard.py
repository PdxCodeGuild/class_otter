import pygame


class GameBoard:
    def __init__(self):
        self.board = []
        for _ in range(3):
            self.board.append([' ' for _ in range(3)])

        self._positions_remaining = 9
    
    def _is_position_available(self, x, y):
        return self.board[x][y] == ' '

    def _check_diagonal(self, board_layout):
        first_position = board_layout[0][0]
        if first_position == ' ':
            return None

        for x in range(2):
            x += 1
            if board_layout[x][x] != first_position:
                return None
        
        return first_position

    def _check_row(self, board_layout, row):
        first_position = board_layout[0][row]
        if first_position == ' ':
            return None

        for x in range(2):
            x += 1
            if board_layout[x][row] != first_position:
                return None
        
        return first_position

    def _transpose(self, board_layout):
        transposed_board_layout = []
        for _ in range(3):
            transposed_board_layout.append([' ' for _ in range(3)])

        for y in range(3):
            for x in range(3):
                transposed_board_layout[x][y] = board_layout[y][x]

        return transposed_board_layout


    def move(self, x, y, player):
        if self._is_position_available(x, y):
            self.board[x][y] = player.token
            self._positions_remaining -= 1
            return True
        return False

    def calc_winner(self):
        current_board = self.board
        winner = self._check_diagonal(current_board)
        if winner != None:
            return winner

        for i in range(3):
            winner = self._check_row(current_board, i)
            if winner != None:
                return winner

        transposed_board = self._transpose(current_board)
        winner = self._check_diagonal(transposed_board)
        if winner != None:
            return winner

        for i in range(3):
            winner = self._check_row(transposed_board, i)
            if winner != None:
                return winner

        return None

    def is_full(self):
        return self._positions_remaining <= 0

    def is_game_over(self):
        return self.is_full() or self.calc_winner() != None

    def update(self, time):
        pass

    def draw(self, surface):
        black = (0, 0, 0)
        pygame.draw.line(surface, black, (280, 120), (280, 360), 3)
        pygame.draw.line(surface, black, (360, 120), (360, 360), 3)

        pygame.draw.line(surface, black, (200, 200), (440, 200), 3)
        pygame.draw.line(surface, black, (200, 280), (440, 280), 3)