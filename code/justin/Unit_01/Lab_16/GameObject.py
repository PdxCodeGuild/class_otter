from Utility import *
from pygame.math import Vector2


class GameObject:
    def __init__(self, position=Vector2(), size=Vector2(), color=MAGENTA):
        self.position = position
        self.size = size
        self.color = color

    def get_rect(self):
        width, height = self.size
        return Rect(self.position.x - (width / 2), self.position.y - (height / 2), width, height)

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
