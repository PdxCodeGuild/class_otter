import pygame
import pygame.freetype
import engine.Color as Color
from engine.core.DisplayWindow import DisplayWindow
from engine.core.GameClock import GameClock


class Engine:
    game = None
    font = None
    font_size = 24
    display = None
    clock = None

    def __init__(self):
        # Initialize pygame library
        pygame.init()
        Engine.font = pygame.freetype.SysFont(pygame.freetype.get_default_font(), Engine.font_size)

    def initialize(self):
        # Setup display window
        Engine.display = DisplayWindow((640, 480), Color.BRIGHT_GRAY)

        # Setup clock
        Engine.clock = GameClock()

    def load_game(self, game_to_load):
        Engine.game = game_to_load

    def run(self):
        # Main game loop
        is_running = True
        while is_running:
            # Update
            Engine.clock.tick()
            is_running = self.process_input() and not Engine.game._should_quit
            Engine.game.update()
            
            # Render
            Engine.display.update(self.game.title_text)
            Engine.game.render()
            Engine.display.render()

        pygame.quit()

    def process_input(self):
        is_running = True

        # Check for input events
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
                    self.game.click(event.pos)

        return is_running
