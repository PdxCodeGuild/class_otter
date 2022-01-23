# Resources:
# https://github.com/PdxCodeGuild/class_otter/blob/main/1%20Python/docs/14%20Classes.md

import math

class Point:
    # This is a static variable. Belongs to class. Accessible to all objects in class.
    pi = 3.1415

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def distance(self, p): # method, or 'member function'
        dx = self.x - p.x
        dy = self.y - p.y
        return math.sqrt(dx*dx + dy*dy)
    
    def scale(self, v):
        self.x *= v
        self.y *= v
    
p3 = Point()
p1 = Point(5,2)
p2 = Point(8,4)
dist = p1.distance(p2) # or p2.distance(p1), either works
print(f"round(dist, 2): {round(dist, 2)}")

print(f"round(Point.pi, 2): {round(Point.pi, 2)}")