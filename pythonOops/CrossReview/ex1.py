class IExample:
    def __init__(self, num_a, num_b):
        self.var1 = num_a
        self.var2 = num_b

    def get_addition(self):
        return self.var1 + self.var2


class ChildA(IExample):
    def __init__(self, num_a, num_b, num_c):
        IExample.__init__(self, num_a, num_b)
        self.var1 = num_a
        self.var2 = num_b
        self.var3 = num_c

    # def get_addition(self):
    #     return self.var1 + self.var2 + self.var3


# i_example = IExample(50, 100)
child_a = ChildA(50, 100, 150)

print(child_a.get_addition())

