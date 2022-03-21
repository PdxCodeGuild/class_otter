import pygame


class DisplayWindow:
    def __init__(self, screen_size, background_color):
        self.screen_size = screen_size

        self._background_screen = pygame.Surface(self.screen_size)
        self.surface = pygame.display.set_mode(self.screen_size)
        self.__background_color = background_color

        self._refresh()

    def _refresh(self, background_color=None):
        if background_color is not None:
            self.__background_color = background_color

        self._background_screen.fill(self.__background_color)
        self._background_screen = self._background_screen.convert()
        self.surface.blit(self._background_screen, (0, 0))

    def update(self, title):
        # Update window title
        pygame.display.set_caption(title)
        self._refresh()

    def render(self):
        # Swap display buffers
        pygame.display.flip()