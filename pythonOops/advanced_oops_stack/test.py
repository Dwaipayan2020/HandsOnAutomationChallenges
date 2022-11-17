class Test:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        pass

    def __add__(self, other):
        return self.x + other.x, self.y + other.y

    def __mul__(self, other):
        return self.x * other.x, self.y * other.y


t_obj = Test(3, 4)

t_obj2 = Test(5, 6)

print(str(t_obj + t_obj2))

print(str(t_obj * t_obj2))
