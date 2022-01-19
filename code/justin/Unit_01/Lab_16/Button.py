import pygame
from GameObject import *
from Panel import *
from Utility import *
from Engine import *


class Button(Panel):
    def __init__(self, message="", position=Vector2(), size=Vector2(), color=MAGENTA, click_func=None):
        super().__init__(message, position, size, color)
        self.__is_disabled = False
        self.__is_hovering = False
        self.__disabled_color = mult_color(self.color, 0.4)
        self.__hover_color = mult_color(self.color, 0.6)
        self.__click_func = click_func

    def _do_click(self):
        if not self.__is_disabled:
            self.__is_disabled = True
            self.__click_func(Engine.game)
    

    def enable(self):
        self.__is_disabled = False

    def click(self, click_position, screen_size):
        if self._check_collision(screen_size, click_position):
            self._do_click()

    def update(self, time, display):
        self.__is_hovering = False if self.__is_disabled else self._check_collision(display.screen_size, pygame.mouse.get_pos())

    def draw(self, time, display):
        color = self.__disabled_color if self.__is_disabled else self.__hover_color if self.__is_hovering else self.color
        
        hover_offset = 0
        if self.__is_hovering:
            hover_offset += 1

        button_rect = local_to_screen(display.screen_size, rect=self.get_rect())

        shadow_color = mult_color(self.color, 0.3)
        drop_shadow_bottom_rect = Rect(button_rect.left + 2 - hover_offset, button_rect.bottom, button_rect.width - 1 + hover_offset, 3)
        pygame.draw.rect(display.surface, shadow_color, drop_shadow_bottom_rect)
        drop_shadow_side_rect = Rect(button_rect.right, button_rect.top + 2 + hover_offset, 3 - hover_offset, button_rect.height + 1 - hover_offset)
        pygame.draw.rect(display.surface, shadow_color, drop_shadow_side_rect)

        button_rect.top += hover_offset
        pygame.draw.rect(display.surface, color, button_rect)

        text, text_rect = self._get_text()
        text_rect = local_to_screen(display.screen_size, rect=text_rect)
        text_shadow_rect = Rect(text_rect)
        text_shadow_rect.centerx += 1
        text_shadow_rect.centery += 1
        Engine.font.render_to(display.surface, text_shadow_rect, text, BLACK)
        Engine.font.render_to(display.surface, text_rect, text, WHITE)
        
