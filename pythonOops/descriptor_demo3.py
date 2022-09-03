'''
Use Of property Decorator
'''


class Circle:
    PI = 3.141

    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    @property
    def get_circumference(self):
        return 2 * self.PI * self.get_radius()


c = Circle(10)
c.radius = 20
print(c.get_circumference)
