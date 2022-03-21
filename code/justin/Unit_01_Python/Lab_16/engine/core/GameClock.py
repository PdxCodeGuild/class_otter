import pygame


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
