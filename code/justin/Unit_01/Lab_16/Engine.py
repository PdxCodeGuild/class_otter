import pygame


class DisplayWindow:
    def __init__(self, screen_size, background_color):
        self.screen_size = screen_size
        self.surface = pygame.display.set_mode(screen_size)
        self.background_color = background_color
        self.screen = pygame.Surface(self.screen_size)
        self._refresh()

    def _refresh(self):
        self.screen.fill(self.background_color)
        self.screen = self.screen.convert()
        self.surface.blit(self.screen, (0, 0))

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
    def __init__(self):
        self._game = None
        self._display = None
        self._clock = None

    def initialize(self):
        # Initialize pygame library
        pygame.init()

        # Setup display window
        self._display = DisplayWindow((640, 480), (255, 128, 0))

        # Setup clock
        self._clock = GameClock()

    def load_game(self, game_to_load):
        self._game = game_to_load

    def run(self):
        # Main game loop
        is_running = True
        while is_running:
            # Update
            self._clock.tick()
            is_running = self.process_input()
            self._game.update(self._clock, self._display)
            
            # Render
            self._display.update(self._game.title_text)
            self._game.render(self._clock, self._display)
            self._display.render()
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    print(event.pos)

        return is_running
