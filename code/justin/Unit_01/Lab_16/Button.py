import pygame
from GameObject import *
from Utility import *
from Engine import *


class Button(GameObject):
    def __init__(self, message="", position=Vector2(), size=(0, 0), color=MAGENTA, click_func=None):
        super().__init__(position, size, color)
        self.__message = message
        self.__is_disabled = False
        self.__is_hovering = False
        self.__disabled_color = self.mult_color(0.1)
        self.__hover_color = self.mult_color(0.5)
        self.__click_func = click_func
        self.__text_rect = Engine.font.get_rect(self.__message, size=Engine.font_size)


    def _do_click(self):
        if not self.__is_disabled:
            self.__is_disabled = True
            self.__click_func(Engine.game)
    

    def enable(self):
        self.__is_disabled = False

    def mult_color(self, factor):
        r = int(clamp(self.color[0] * factor, 0, 255))
        g = int(clamp(self.color[1] * factor, 0, 255))
        b = int(clamp(self.color[2] * factor, 0, 255))
        return (r, g, b)

    def click(self, click_position, screen_size):
        if self._check_collision(screen_size, click_position):
            self._do_click()

    def update(self, time, display):
        self.__is_hovering = False if self.__is_disabled else self._check_collision(display.screen_size, pygame.mouse.get_pos())

    def draw(self, time, display):
        color = self.__disabled_color if self.__is_disabled else self.__hover_color if self.__is_hovering else self.color
        
        screen_rect = local_to_screen(display.screen_size, rect=self.get_rect())
        pygame.draw.rect(display.surface, color, screen_rect)

        self.__text_rect.center = screen_rect.center
        Engine.font.render_to(display.surface, self.__text_rect, self.__message, BLACK)
