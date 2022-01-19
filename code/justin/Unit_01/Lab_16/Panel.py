import pygame
from GameObject import *
from Utility import *
from Engine import *


class Panel(GameObject):
    text_padding = (10, 10)

    def __init__(self, message="", position=Vector2(), size=Vector2(), color=MAGENTA):
        super().__init__(position, size, color)
        self.__message = None
        self.__text_rect = None
        self.edit_text(message)

    def _get_text(self):
        return self.__message, Rect(self.__text_rect)


    def edit_text(self, new_message):
        self.__message = new_message
        self.__text_rect = Engine.font.get_rect(self.__message, size=Engine.font_size)
        self.__text_rect.center = self.position

        width = self.__text_rect.width + Panel.text_padding[0]
        height = self.__text_rect.height + Panel.text_padding[1]
        if self.size.x < width:
            self.size.x = width
        if self.size.y < height:
            self.size.y = height

    def update(self, time, display):
        pass

    def draw(self, time, display):
        pass
        button_rect = local_to_screen(display.screen_size, rect=self.get_rect())

        # shadow_color = mult_color(self.color, 0.3)
        # drop_shadow_bottom_rect = Rect(button_rect.left + 2, button_rect.bottom, button_rect.width - 1, 3)
        # pygame.draw.rect(display.surface, shadow_color, drop_shadow_bottom_rect)
        # drop_shadow_side_rect = Rect(button_rect.right, button_rect.top + 2, 3, button_rect.height + 1)
        # pygame.draw.rect(display.surface, shadow_color, drop_shadow_side_rect)

        pygame.draw.rect(display.surface, self.color, button_rect)

        text_rect = local_to_screen(display.screen_size, rect=self.__text_rect)
        text_shadow_rect = Rect(text_rect)
        text_shadow_rect.centerx += 1
        text_shadow_rect.centery += 1
        Engine.font.render_to(display.surface, text_shadow_rect, self.__message, BLACK)
        Engine.font.render_to(display.surface, text_rect, self.__message, WHITE)
        
