import pygame
import pygame.freetype
from GameObject import *
from Utility import *
from Engine import *


class Button(GameObject):
    def __init__(self, message="", position=Vector2(), size=(0, 0), color=(255, 0, 255), click_func=None):
        super().__init__(position, size, color)
        self._message = message
        self._is_disabled = False
        self._is_hovering = False
        self._disabled_color = self._calc_color(0.1)
        self._hover_color = self._calc_color(0.5)
        self._click_func = click_func

    def _calc_color(self, factor):
        r = int(clamp(self._color[0] * factor, 0, 255))
        g = int(clamp(self._color[1] * factor, 0, 255))
        b = int(clamp(self._color[2] * factor, 0, 255))
        return (r, g, b)

    def _do_click(self):
        if not self._is_disabled:
            self._is_disabled = True
            self._click_func(Engine._game)
            


    def click(self, click_position, screen_size):
        if self._check_collision(screen_size, click_position):
            self._do_click()

    def update(self, time, display):
        if not self._is_disabled:
            if self._check_collision(display.screen_size, pygame.mouse.get_pos()):
                self._is_hovering = True
            else:
                self._is_hovering = False

    def draw(self, time, display):
        if not self._is_disabled:
            color = self._hover_color if self._is_hovering else self._color
        else:
            color = self._disabled_color
        
        pygame.draw.rect(display.surface, color, local_to_screen(display.screen_size, rect=self.get_rect()))