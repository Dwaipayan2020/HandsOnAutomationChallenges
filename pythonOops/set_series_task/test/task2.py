
class A():
    def __init__(self, name):
        print('name: ', name)
        # super().__init__()
        print("A")


class B():
    def __init__(self, age):
        print('age: ', age)
        # super().__init__()
        print("B")


class C(B, A):
    def __init__(self):
        # super().__init__()
        B.__init__(self, 29)
        A.__init__(self, "Dwaipayan")
        print("C")


c = C()

"""
No of ways to call super class constructors in python.
"""
