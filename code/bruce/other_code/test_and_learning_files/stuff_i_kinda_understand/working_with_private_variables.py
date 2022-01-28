import math

class Rotator:
    
    def __init__(self, alpha):
        self.set_alpha(alpha)
        # self.setAlpha(alpha)
    
    def set_alpha(self, alpha): #encapsulation
        self.__alpha = alpha
        self.cos_alpha = math.cos(alpha)
        self.sin_alpha = math.sin(alpha)
    
    def rotate(self, px, py):
        rx = px*self.cos_alpha + py*self.sin_alpha
        ry = -px*self.sin_alpha + py*self.cos_alpha
        return rx, ry

r1 = Rotator(2)
r1x, r1y = r1.rotate(3,4)
print(r1x, r1y)
for r in r1.rotate(3,4):
    print(round(r, 2))