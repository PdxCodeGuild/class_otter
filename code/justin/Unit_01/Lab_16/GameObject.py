from Utility import *
from pygame.math import Vector2


class GameObject:
    def __init__(self, position=Vector2(), size=(0, 0), color=(255, 0, 255)):
        self._position = position
        self._size = size
        self._color = color

    def update(self, time, display):
        pass

    def draw(self, time, display):
        pass