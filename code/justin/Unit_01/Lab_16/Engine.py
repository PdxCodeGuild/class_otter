import pygame
import pygame.freetype
from Utility import *


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


class GameClock:
    def __init__(self, frames_per_second=144):
        self._frames_per_second = frames_per_second
        self.frame_time = 0
        self.delta_time = 0
        self.tick_count = 0
        self.clock = pygame.time.Clock()

    def tick(self):
        # Count up frame time and tick the clock up to the given frames per second
        self.frame_time += self.clock.tick(self._frames_per_second)
        self.delta_time = self.clock.get_time() / 1000
        self.tick_count += 1



class Engine:
    game = None
    font = None
    font_size = 24

    def __init__(self):
        # Initialize pygame library
        pygame.init()
        Engine.font = pygame.freetype.SysFont(pygame.freetype.get_default_font(), Engine.font_size)

        self.display = None
        self.clock = None

    def initialize(self):
        # Setup display window
        self.display = DisplayWindow((640, 480), BRIGHT_GRAY)

        # Setup clock
        self.clock = GameClock()

    def load_game(self, game_to_load):
        Engine.game = game_to_load

    def run(self):
        # Main game loop
        is_running = True
        while is_running:
            # Update
            self.clock.tick()
            is_running = self.process_input() and not Engine.game._should_quit
            Engine.game.update(self.clock, self.display)
            
            # Render
            self.display.update(self.game.title_text)
            Engine.game.render(self.clock, self.display)
            self.display.render()

        pygame.quit()

    def process_input(self):
        is_running = True

        # Check for input events
        screen_size = self.display.screen_size
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    is_running = False
                    break
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.game.click(event.pos, screen_size)

        return is_running
