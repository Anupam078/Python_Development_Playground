from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Triangle(Shape):
    def __init__(self, b, h, s1, s2, s3):
        self.b = b
        self.h = h
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
    def area(self):
        return 0.5 * self.b * self.h
    def perimeter(self):
        return self.s1 + self.s2 + self.s3

class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w
    def area(self):
        return self.l * self.w
    def perimeter(self):
        return 2 * (self.l + self.w)

class Square(Shape):
    def __init__(self, s):
        self.s = s
    def area(self):
        return self.s * self.s
    def perimeter(self):
        return 4 * self.s

class Pentagon(Shape):
    def __init__(self, s):
        self.s = s
    def area(self):
        return (5*self.s**2) / (4 * math.tan(math.pi / 5))
    def perimeter(self):
        return 5 * self.s
    def center_to_side(self):
        return self.s/(2*math.tan(math.pi/5))


t =Triangle(10, 6, 10, 8, 7)
r =Rectangle(8, 5)
sq =Square(4)
p =Pentagon(6)



print("Triangle Area:", t.area())
print("Triangle Perimeter:", t.perimeter())

print("Rectangle Area:", r.area())
print("Rectangle Perimeter:", r.perimeter())

print("Square Area:", sq.area())
print("Square Perimeter:", sq.perimeter())

print("Pentagon Area:", p.area())
print("Pentagon Perimeter:", p.perimeter())
print("Distance from Pentagon Center to Side:", p.center_to_side())