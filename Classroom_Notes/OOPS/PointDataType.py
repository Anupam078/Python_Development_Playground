class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        return self.x + other.x, self.y + other.y

    def __sub__(self, other):
        return self.x - other.x, self.y - other.y
    def __mod__(self, other):
        return self.x % other.x, self.y % other.y
    def __ge__(self, other):
        return self.x >= other.x and self.y >= other.y

point1 = Point(3, 4)
point2 = Point(1, 2)
print(point1+point2)
print(point1-point2)
print(point1%point2)
print(point1>=point2)
