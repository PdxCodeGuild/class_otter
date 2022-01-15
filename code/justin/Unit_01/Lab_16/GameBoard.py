import pygame
from pygame import Rect
from pygame.math import Vector2
from Utility import *


class GameBoard:
    def __init__(self):
        self.board = []
        for _ in range(3):
            self.board.append([' ' for _ in range(3)])

        self._positions_remaining = 9
        self._tile_rects = []
        rect_size = (80, 80)
        half_size = [int(x / 2) for x in rect_size]
        
        position = Vector2(0, 0)
        for x in range(-rect_size[0] - half_size[0], rect_size[0] - half_size[0] + 1, rect_size[0]):
            position.x = x
            for y in range(-rect_size[1] - half_size[1], rect_size[1] - half_size[1] + 1, rect_size[1]):
                position.y = y
                self._tile_rects.append(pygame.Rect((position.x - half_size[0], position.y - half_size[1]), rect_size))
        
        self._draw_tile = [False, False, False, False, False, False, False, False, False]
    
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


    def update(self, time, display):
        mouse_pos = pygame.mouse.get_pos()
        for i in range(len(self._tile_rects)):
            rect = local_to_screen(display.screen_size, rect=self._tile_rects[i])
            if rect.collidepoint(mouse_pos):
                self._draw_tile[i] = True
            else:
                self._draw_tile[i] = False

        

    def draw(self, time, display):
        surface = display.surface
        black = (0, 0, 0)
        
        pygame.draw.line(surface, black, (280, 122), (280, 358), 3)
        pygame.draw.line(surface, black, (360, 122), (360, 358), 3)

        pygame.draw.line(surface, black, (202, 200), (438, 200), 3)
        pygame.draw.line(surface, black, (202, 280), (438, 280), 3)

        red = (255, 0, 0)
        screen_size = display.screen_size
        for i in range(len(self._tile_rects)):
            if self._draw_tile[i]:
                pygame.draw.rect(surface, red, local_to_screen(screen_size, rect=self._tile_rects[i]), 2)