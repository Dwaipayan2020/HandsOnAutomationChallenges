from weakref import WeakKeyDictionary


class MyDescriptor:

    def __int__(self):
        self.__age = WeakKeyDictionary()

    def __get__(self, instance, owner):
        return self.__age.get(instance)

    def __set__(self, instance, value):

        if value > 30:
            print("30 plus")
        else:
            print("either > 40 or <30")
        self.__age[instance] = value

    def __delete__(self, instance):
        del self.__age[instance]


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
print(str(c.get_name()) + str(c.get_age()))
