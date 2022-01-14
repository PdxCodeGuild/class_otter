from pygame import Vector2
from pygame import Rect

def local_to_screen(screen_size, position=Vector2(), size=Vector2(), rect=None):
    x_offset = (screen_size[0] / 2)
    y_offset = (screen_size[1] / 2)

    if rect == None:
        x_offset -= (size[0] / 2)
        y_offset -= (size[1] / 2)
        position.x += x_offset
        position.y += y_offset
        return position
    else:
        x_offset -= (rect.width / 2)
        y_offset -= (rect.height / 2)
        rect.centerx = position.x + x_offset
        rect.centery = position.y + y_offset
        return rect

# def local_to_screen(screen_size, position=Vector2(), size=Vector2(), rect=None):
#     x_offset = (screen_size[0] / 2)
#     y_offset = (screen_size[1] / 2)

#     if rect == None:
#         x_offset -= (size[0] / 2)
#         y_offset -= (size[1] / 2)
#     else:
#         x_offset -= (rect.width / 2)
#         y_offset -= (rect.height / 2)

#     position.x += x_offset
#     position.y += y_offset
#     return position