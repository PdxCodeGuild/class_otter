class Size:
    def __init__(self, width=1, height=1):
        self.width = width
        self.height = height

class Vector2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class GameObject:
    def __init__(self, position=Vector2(), size=Size(), color=(255, 0, 255)):
        self._position = position
        self._size = size
        self._color = color

    def update(self):
        pass