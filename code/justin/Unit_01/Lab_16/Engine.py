import pygame


class DisplayWindow:
    def __init__(self, screen_size, background_color):
        self.screen_size = screen_size
        self.display = pygame.display.set_mode(screen_size)
        
        background = pygame.Surface(self.screen_size)
        background.fill(background_color)
        self.display.blit(background.convert(), (0, 0))

    def update(self, title):
        # Update window title
        pygame.display.set_caption(title)

        # Swap display buffers
        pygame.display.flip()


class GameClock:
    def __init__(self, fps=60):
        self._frames_per_second = fps
        self.frame_time = 0
        self.clock = pygame.time.Clock()

    def tick(self):
        # Count up frame time and tick the clock no more than 60fps
        self.frame_time += self.clock.tick(self._frames_per_second)


class Engine:
    def __init__(self):
        self._game = None
        self._display = None
        self._clock = None

    def initialize(self):
        # Initialize pygame library
        pygame.init()

        # Setup display window
        self._display = DisplayWindow((640, 480), (255, 127, 64))

        # Setup clock
        self._clock = GameClock()

    def load_game(self, game_to_load):
        self._game = game_to_load

    def run(self):
        # Main game loop
        is_running = True
        while is_running:
            self._clock.tick()
            is_running = self.process_input()
            self._game.update()
            self._game.render()
            self.render()
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
    
    def render(self):
        self._display.update(self._game.title_text)
        
        for game_object in self._game._game_objects:
            pygame.draw.rect(self._display.display, game_object._color, pygame.Rect(game_object._position.x, game_object._position.x, game_object._size.width, game_object._size.height))