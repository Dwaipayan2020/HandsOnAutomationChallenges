def __Add(a, b):
    print(a + b)


def Sub(a, b):
    print(a - b)


def Prod(a, b):
    print(a * b)


def Mod(a, b):
    print(a % b)


def PerformDiv(a, b):
    print(a / b)


print(__name__)
if __name__ == "__main__":
    print("I am being executed from __main__ file")
    PerformDiv(10, 2)
    __Add(10, 2)
else:
    print("I am being called from other file")
