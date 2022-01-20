import pygame
import engine.Color as Color
from engine.core.GameObject import GameObject
from pygame.math import Vector2
from engine.core.Engine import Engine


class Token_X(GameObject):
    def __init__(self, position=Vector2(), size=Vector2(), color=Color.MAGENTA):
        super().__init__(position, size, color)
        self.half_size = self.size.x / 2, self.size.y / 2

    def update(self):
        pass

    def draw(self):
        surface = Engine.display.surface
        pos = self.position
        pygame.draw.line(surface, self.color, (pos.x - self.half_size[0], pos.y - self.half_size[1]), (pos.x + self.half_size[0], pos.y + self.half_size[1]), 8)
        pygame.draw.line(surface, self.color, (pos.x + self.half_size[0], pos.y - self.half_size[1]), (pos.x - self.half_size[0], pos.y + self.half_size[0]), 8)


class Token_O(GameObject):
    def __init__(self, position=Vector2(), size=Vector2(), color=Color.MAGENTA):
        super().__init__(position, size, color)
        self.radius = self.size.x / 2

    def update(self):
        pass

    def draw(self):
        surface = Engine.display.surface
        pygame.draw.circle(surface, self.color, (self.position.x, self.position.y), self.radius, 6)