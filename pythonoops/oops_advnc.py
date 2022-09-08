class Circle:
    PI = 3.141

    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius


myCircle = Circle(10)
myCircle2 = Circle(20)
#
# print(myCircle.radius)
print(myCircle.__dict__["radius"])

print(f'__str__ is -> {myCircle.__str__()}')
print(f'__class__ is -> {myCircle.__class__}')

print(f'__dir__ is -> {myCircle.__dir__()}')

# print(f'__setattr__ for area -> {myCircle.__setattr__("area", 100)}')
# print(f'getting value for attribute area -> {myCircle.__getattribute__("area")}')
# print(f' Displaying class dictionary -> {myCircle.__dict__}')
# print(f'Displaying directory -> {myCircle.__dir__()}')
#
# print(f'displaying __doc__ -> {myCircle.__doc__}')
print(f'displaying __module__ ->  {myCircle.__module__}')
print(f'displaying __hash__ of mycircle  ->  {myCircle.__hash__()}')
print(f'displaying __hash__ of mycircle2  ->  {myCircle2.__hash__()}')
print(f'displaying __sizeof__ of mycircle -> {myCircle.__sizeof__()}')
print(f'displaying __sizeof__ of mycircle2 -> {myCircle2.__sizeof__()}')

# print(f'displaying __slots__  -> {myCircle.__slots__}')
# print(f'__annotations__ is -> {myCircle.__annotations__}')
# print(f'__new__ is -> {myCircle.__new__()}')
