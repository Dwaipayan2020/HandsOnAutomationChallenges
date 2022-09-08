class Widget:
    copyright = "Witrett.inc"


class Circle(Widget):
    PI = 3.141

    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius


myCircle = Circle(10)
myWidget = Widget()
print(f'method resolution order of object myCircle is {type(myCircle).mro()}')
print(f'method resolution order of object myWidget is {type(myWidget).mro()}')
print(f'copyright is reserved by {myCircle.copyright}\n')
print(f'copyright is reserved by {Circle.copyright}\n')
print(f'copyright is reserved by {Widget.copyright}\n')
print(f'copyright is reserved by {myWidget.copyright}\n')
