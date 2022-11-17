class MyClass:
    @classmethod
    def hello(cls, name):
        print(cls)
        print('Hello from', cls.__name__, ', ', name)

    def hello_instance_method(self, name):
        """Instance methods are the most common type of
           methods which is invoked by an instance object
           (and not a class object).
           it takes the instance (self) as its first
           argument.
        """
        print(self)
        print('Hello from', self.__class__.__name__, ', ', name)

    @staticmethod
    def hello_static_method():
        """A static method doesn't know its class
           and is attached to the class for convenience.
           It does not depend on the state of the object
           and could be a separate function of a module.
           A static method can be invoked via  a class object
           or instance object.
        """
        print('Hello, World!')


MyClass.hello('Ronit')

m_class = MyClass()
m_class.hello_instance_method('Dwaipayan')
MyClass.hello_static_method()
# Below line, it works but does not make sense.
# MyClass.hello_instance_method(m_class, 'Ronit')
# any instance method must be called using
# class instance or object.
