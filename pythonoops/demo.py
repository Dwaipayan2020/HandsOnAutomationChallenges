class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


c = Student("Rohit", 30)
print(str(c.get_name()))
print(str(c.get_age()))