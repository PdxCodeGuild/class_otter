import pygame
from GameObject import *
from pygame.math import Vector2


class Token_X(GameObject):
    def __init__(self, position=Vector2(), size=Vector2(), color=MAGENTA):
        super().__init__(position, size, color)

    def update(self, time, display):
        pass

    def draw(self, time, display):
        surface = display.surface
        pos = self.position
        half_size = self.size.x / 2, self.size.y / 2
        pygame.draw.line(surface, self.color, (pos.x - half_size[0], pos.y - half_size[1]), (pos.x + half_size[0], pos.y + half_size[1]), 8)
        pygame.draw.line(surface, self.color, (pos.x + half_size[0], pos.y - half_size[1]), (pos.x - half_size[0], pos.y + half_size[0]), 8)


class Token_O(GameObject):
    def __init__(self, position=Vector2(), size=Vector2(), color=MAGENTA):
        super().__init__(position, size, color)

    def update(self, time, display):
        pass

    def draw(self, time, display):
        surface = display.surface
        pygame.draw.circle(surface, self.color, (self.position.x, self.position.y), self.size.x / 2, 6)