import pygame
import engine.Color as Color
from engine.core.GameObject import GameObject
from engine.interface.Panel import Panel
from engine.core.Engine import Engine
from pygame import Vector2
from pygame import Rect


class Button(Panel):
    def __init__(self, message="", position=Vector2(), size=Vector2(), color=Color.MAGENTA, click_func=None):
        super().__init__(message, position, size, color)
        self.__is_disabled = False
        self.__is_hovering = False
        self.__disabled_color = Color.mult_color(self.color, 0.4)
        self.__hover_color = Color.mult_color(self.color, 0.6)
        self.__click_func = click_func

    def _do_click(self):
        if not self.__is_disabled:
            self.__is_disabled = True
            self.__click_func(Engine.game)
    

    def enable(self):
        self.__is_disabled = False

    def click(self, click_position):
        if self._check_collision(click_position):
            self._do_click()

    def update(self):
        self.__is_hovering = False if self.__is_disabled else self._check_collision(pygame.mouse.get_pos())

    def draw(self):
        surface = Engine.display.surface

        color = self.__disabled_color if self.__is_disabled else self.__hover_color if self.__is_hovering else self.color
        
        hover_offset = 0
        if self.__is_hovering:
            hover_offset += 1

        button_rect = GameObject.local_to_screen(rect=self.get_rect())

        shadow_color = Color.mult_color(self.color, 0.3)
        drop_shadow_bottom_rect = Rect(button_rect.left + 2 - hover_offset, button_rect.bottom, button_rect.width - 1 + hover_offset, 3)
        pygame.draw.rect(surface, shadow_color, drop_shadow_bottom_rect)
        drop_shadow_side_rect = Rect(button_rect.right, button_rect.top + 2 + hover_offset, 3 - hover_offset, button_rect.height + 1 - hover_offset)
        pygame.draw.rect(surface, shadow_color, drop_shadow_side_rect)

        button_rect.top += hover_offset
        pygame.draw.rect(surface, color, button_rect)

        text, text_rect = self._get_text()
        text_rect = GameObject.local_to_screen(rect=text_rect)
        text_shadow_rect = Rect(text_rect)
        text_shadow_rect.centerx += 1
        text_shadow_rect.centery += 1
        Engine.font.render_to(surface, text_shadow_rect, text, Color.BLACK)
        Engine.font.render_to(surface, text_rect, text, Color.WHITE)
        
