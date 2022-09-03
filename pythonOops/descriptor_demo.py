class Circle:
    PI = 3.141

    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius


myCircle = Circle(10)

print(f'radius is {myCircle.radius}')

myCircle.radius = 30

print(f'radius is {myCircle.radius}')


# print(f'\nObject "{myCircle}" is an instance of class name : {type(myCircle)}\n')
# print(f'class name Circle can be written as type(class_object) == type(myCircle) == Circle .'
#       f' Hence verified as {Circle == type(myCircle)}\n')

# print(f'PI is {myCircle.PI} and asserts the expression as {myCircle.PI == type(myCircle).__dict__["PI"]}')
