import pygame
import engine.Color as Color
from engine.core.GameObject import GameObject
from engine.core.Engine import Engine
from pygame import Vector2
from pygame import Rect


class Panel(GameObject):
    text_padding = (10, 10)

    def __init__(self, message="", position=Vector2(), size=Vector2(), color=Color.MAGENTA):
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

    def click(self, click_position):
        pass
    
    def update(self):
        pass

    def draw(self):
        surface = Engine.display.surface
        button_rect = GameObject.local_to_screen(rect=self.get_rect())

        pygame.draw.rect(surface, self.color, button_rect)

        text_rect = GameObject.local_to_screen(rect=self.__text_rect)
        text_shadow_rect = Rect(text_rect)
        text_shadow_rect.centerx += 1
        text_shadow_rect.centery += 1
        Engine.font.render_to(surface, text_shadow_rect, self.__message, Color.BLACK)
        Engine.font.render_to(surface, text_rect, self.__message, Color.WHITE)
        
