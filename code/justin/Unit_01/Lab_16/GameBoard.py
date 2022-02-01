import pygame
import engine.Color as Color
from pygame.math import Vector2
from engine.core.GameObject import GameObject
from engine.core.Engine import Engine


class GameBoard():
    def __init__(self):
        self.__positions_remaining = 9
        self.__tile_rects = []
        self.__draw_tile = [False, False, False, False, False, False, False, False, False]

        self.board = []
        for _ in range(3):
            self.board.append([' ' for _ in range(3)])

        rect_size = (80, 80)
        half_size = [int(x / 2) for x in rect_size]        
        position = Vector2(0, 0)
        for x in range(-rect_size[0], rect_size[0] + 1, rect_size[0]):
            position.x = x
            for y in range(-rect_size[1], rect_size[1] + 1, rect_size[1]):
                position.y = y
                self.__tile_rects.append(pygame.Rect((position.x - half_size[0], position.y - half_size[1]), rect_size))
    
    def _is_position_available(self, x, y):
        return self.board[x][y] == ' '

    def _check_diagonals(self, board_layout):
        center_position = board_layout[1][1]
        if center_position == ' ':
            return None

        if board_layout[0][0] == center_position and board_layout[2][2] == center_position:
            return center_position
        elif board_layout[2][0] == center_position and board_layout[0][2] == center_position:
            return center_position
        
        return None

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
    
    def _is_full(self):
        return self.__positions_remaining <= 0


    def get_rect_center_at(self, screen_position):
        for i in range(len(self.__tile_rects)):
            rect = GameObject.local_to_screen(rect=self.__tile_rects[i])
            if rect.collidepoint(screen_position):
                return rect.center
        return None

    def move(self, screen_position, player):
        x = y = -1
        for i in range(len(self.__tile_rects)):
            rect = GameObject.local_to_screen(rect=self.__tile_rects[i])
            if rect.collidepoint(screen_position):
                x = i // 3
                y = i % 3
        
        if x == -1:
            return False

        if self._is_position_available(x, y):
            self.board[x][y] = player.token
            self.__positions_remaining -= 1
            return True
        
        return False

    def calc_winner(self):
        current_board = self.board
        winner = self._check_diagonals(current_board)
        if winner is not None:
            return winner

        for i in range(3):
            winner = self._check_row(current_board, i)
            if winner is not None:
                return winner

        transposed_board = self._transpose(current_board)
        for i in range(3):
            winner = self._check_row(transposed_board, i)
            if winner is not None:
                return winner

        return None

    def is_game_over(self):
        return self._is_full() or self.calc_winner() != None


    def click(self, click_position):
        pass

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        for i in range(len(self.__tile_rects)):
            rect = GameObject.local_to_screen(rect=self.__tile_rects[i])
            if rect.collidepoint(mouse_pos):
                self.__draw_tile[i] = True
            else:
                self.__draw_tile[i] = False

    def draw(self):
        surface = Engine.display.surface
        
        pygame.draw.line(surface, Color.BLACK, (280, 122), (280, 358), 3)
        pygame.draw.line(surface, Color.BLACK, (360, 122), (360, 358), 3)

        pygame.draw.line(surface, Color.BLACK, (202, 200), (438, 200), 3)
        pygame.draw.line(surface, Color.BLACK, (202, 280), (438, 280), 3)

        for i in range(len(self.__tile_rects)):
            if self.__draw_tile[i]:
                pygame.draw.rect(surface, Color.BRIGHT_RED, GameObject.local_to_screen(rect=self.__tile_rects[i]), 2)
