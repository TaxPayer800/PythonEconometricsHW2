
import math


class Circle():
    def __init__(self):
        self.radius = 0

    def area(self):
        return (math.pi * self.radius**2)

class Square():
    def __init__(self):
        self.side = 0
        
    def area(self):
        return (self.side**2)


class Rectangle():
    def __init__(self):
        self.base = 0
        self.height = 0

    def area(self):
        return (self.base * self.height)

    def diagonal(self):
        return math.sqrt(self.base**2 + self.height**2)
        



c1 = Circle()
c1.radius = 9

s1 = Square()
s1.side = 10

r1 = Rectangle()
r1.base = 7.5
r1.height = 12



max_value = max(s1.area(), r1.area(), c1.area())
print('Area max =', max_value)


