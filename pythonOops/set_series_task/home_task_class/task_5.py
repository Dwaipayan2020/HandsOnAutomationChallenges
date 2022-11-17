"""5. Create a class Circle, that stores
the radius and contains 2 methods:
get_area, get_perimeter, which give the area and perimeter
respectively of the
circle."""
from math import pi


class Circle:
    perimeter = 0
    area = 0

    def __init__(self, radius):
        self.r = radius
        pass

    def get_area(self):
        self.area = pi * pow(self.r, 2)
        return self.area

    def get_perimeter(self):
        self.perimeter = 2 * pi * self.r
        return self.perimeter


rad = 5
c = Circle(rad)
print('Circle radius: ', rad)
print(f'Perimeter of the circle: {c.get_perimeter()}', end='\n')
print(f'Area of the circle: {c.get_area()}', end='\n')
