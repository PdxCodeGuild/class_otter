import engine.Color as Color
from pygame import Vector2
from pygame import Rect
from engine.core.Engine import Engine


class GameObject:
    def __init__(self, position=Vector2(), size=Vector2(), color=Color.MAGENTA):
        self.position = position
        self.size = size
        self.color = color

    def _check_collision(self, point):
        rect = GameObject.local_to_screen(rect=self.get_rect())
        return rect.collidepoint(point)


    def get_rect(self):
        width, height = self.size
        return Rect(self.position.x - (width / 2), self.position.y - (height / 2), width, height)

    def click(self, click_position):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def draw(self):
        raise NotImplementedError

    @classmethod
    def local_to_screen(position=Vector2(), size=Vector2(), rect=None):
        x_offset = (Engine.display.screen_size[0] / 2)
        y_offset = (Engine.display.screen_size[1] / 2)

        if rect is None:
            x_offset -= (size[0] / 2)
            y_offset -= (size[1] / 2)
            new_rect = Rect(position.x + x_offset, position.y + y_offset, size[0], size[1])
        else:
            x_offset -= (rect.width / 2)
            y_offset -= (rect.height / 2)
            new_rect = Rect(rect.centerx + x_offset, rect.centery + y_offset, rect.width, rect.height)
        
        return new_rect
