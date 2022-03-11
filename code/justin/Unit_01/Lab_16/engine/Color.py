import engine.Utility as Utility

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
    r = int(Utility.clamp(color[0] * factor, 0, 255))
    g = int(Utility.clamp(color[1] * factor, 0, 255))
    b = int(Utility.clamp(color[2] * factor, 0, 255))
    return (r, g, b)
