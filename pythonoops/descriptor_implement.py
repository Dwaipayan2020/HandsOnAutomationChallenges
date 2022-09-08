class MyDescriptor:

    def __int__(self):
        self.__age = 0

    def __get__(self, instance, owner):
        return self.__age

    def __set__(self, instance, value):

        if value > 30:
            print("30 plus")
        else:
            print("either > 40 or <30")

        self.__age = value

    def __delete__(self, instance):
        del self.__age


class Student:
    age = MyDescriptor()

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


c = Student("Rohit", 40)

c2 = Student("Rahul", 20)

print(str(c.get_name()) + " " + str(c.get_age()))
print(str(c2.get_name()) + " " + str(c2.get_age()))
