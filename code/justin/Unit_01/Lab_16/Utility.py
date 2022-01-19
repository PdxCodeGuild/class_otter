import math
from pygame import Vector2
from pygame import Rect


# Color constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (64, 64, 64)
MAGENTA = (255, 0, 255)
BRIGHT_GRAY = (96, 96, 96)
BRIGHT_GREEN = (32, 255, 64)
BRIGHT_RED = (255, 64, 32)
BRIGHT_ORANGE = (255, 128, 0)
BRIGHT_BLUE = (0, 128, 255)

def mult_color(color, factor):
    r = int(clamp(color[0] * factor, 0, 255))
    g = int(clamp(color[1] * factor, 0, 255))
    b = int(clamp(color[2] * factor, 0, 255))
    return (r, g, b)

def local_to_screen(screen_size, position=Vector2(), size=Vector2(), rect=None):
    x_offset = (screen_size[0] / 2)
    y_offset = (screen_size[1] / 2)

    if rect is None:
        x_offset -= (size[0] / 2)
        y_offset -= (size[1] / 2)
        new_rect = Rect(position.x + x_offset, position.y + y_offset, size[0], size[1])
    else:
        x_offset -= (rect.width / 2)
        y_offset -= (rect.height / 2)
        new_rect = Rect(rect.centerx + x_offset, rect.centery + y_offset, rect.width, rect.height)
    
    return new_rect

def clamp(value, range_min, range_max):
    return max(range_min, min(value, range_max))