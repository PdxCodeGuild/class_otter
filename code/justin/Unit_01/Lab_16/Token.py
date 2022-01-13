from GameObject import *


class Token_X(GameObject):
    def __init__(self, position=Vector2(), size=Size(), color=(255, 0, 255)):
        super().__init__(position, size, color)

    def update(self, time):
        pass

    def draw(self, surface):
        pos = self._position
        half_size = self._size.width / 2, self._size.height / 2
        pygame.draw.line(surface, self._color, (pos.x - half_size[0], pos.y - half_size[1]), (pos.x + half_size[0], pos.y + half_size[1]), 8)
        pygame.draw.line(surface, self._color, (pos.x + half_size[0], pos.y - half_size[1]), (pos.x - half_size[0], pos.y + half_size[0]), 8)


class Token_Y(GameObject):
    def __init__(self, position=Vector2(), size=Size(), color=(255, 0, 255)):
        super().__init__(position, size, color)

    def update(self, time):
        pass

    def draw(self, surface):
        pygame.draw.circle(surface, self._color, (self._position.x, self._position.y), self._size.width / 2, 6)