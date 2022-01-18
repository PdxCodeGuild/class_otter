from Utility import *
from pygame.math import Vector2


class GameObject:
    def __init__(self, position=Vector2(), size=(0, 0), color=(255, 0, 255)):
        self._position = position
        self._size = size
        self._color = color

    def get_rect(self):
        width = self._size[0]
        height = self._size[1]
        rect = Rect(self._position.x - (width / 2), self._position.y - (height / 2), width, height)
        return rect

    def click(self, click_position, screen_size):
        pass

    def _do_click(self):
        pass

    def _check_collision(self, screen_size, point):
        rect = local_to_screen(screen_size, rect=self.get_rect())
        return rect.collidepoint(point)

    def update(self, time, display):
        pass

    def draw(self, time, display):
        pass