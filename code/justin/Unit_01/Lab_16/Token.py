import pygame
from GameObject import *
from pygame.math import Vector2


class Token_X(GameObject):
    def __init__(self, position=Vector2(), size=(0, 0), color=(255, 0, 255)):
        super().__init__(position, size, color)

    def update(self, time, display):
        pass

    def draw(self, time, display):
        surface = display.surface
        pos = self._position
        half_size = self._size[0] / 2, self._size[1] / 2
        pygame.draw.line(surface, self._color, (pos.x - half_size[0], pos.y - half_size[1]), (pos.x + half_size[0], pos.y + half_size[1]), 8)
        pygame.draw.line(surface, self._color, (pos.x + half_size[0], pos.y - half_size[1]), (pos.x - half_size[0], pos.y + half_size[0]), 8)


class Token_O(GameObject):
    def __init__(self, position=Vector2(), size=(0, 0), color=(255, 0, 255)):
        super().__init__(position, size, color)

    def update(self, time, display):
        pass

    def draw(self, time, display):
        surface = display.surface
        pygame.draw.circle(surface, self._color, (self._position.x, self._position.y), self._size[0] / 2, 6)