
# Resources:
# https://github.com/PdxCodeGuild/class_otter/blob/bruce/1%20Python/docs/14%20Classes.md

import math

# Create the class:
##########################################################
class Point:
    # Initializer is used to 'create' an instance 'object' of class 'Point'.
    def __init__(self, x, y):
        # Specify some member variables. These will be 'member variables'
        # or 'attributes' of 'p1' etc.
        self.x = x
        self.y = y
    
    # 'self' is current instance of the class:
    # If "p1 = Point(5, 2)" is used to create the object, p1 IS self.
    # 'p1' does not need to be passed into 'distance()' since it is
    # known as self. Only the other instance obect is needed to be
    # passed to function.
    def distance(self, p): # method, or 'member function'
        dx = self.x - p.x
        dy = self.y - p.y
        return math.sqrt(dx*dx + dy*dy)
##########################################################


# Use the class:
###################
# Call the initializer to create the objects.
p1 = Point(5, 2)
p2 = Point(8, 4)

# We can access 'p1.x' since 'x' is not 'private'. We will change it to
# private later.
print(f"p1.x: {p1.x}") # p1.x: 5
print(f"p1.y: {p1.y}") # p1.y: 2

print(f"type(p1): {type(p1)}")
# type(p1): <class '__main__.Point'>
print(f"round(p1.distance(p2),2): {round(p1.distance(p2),2)}")
# round(p1.distance(p2),2): 3.61
###################





# Second object version
##########################################################

##########################################################
