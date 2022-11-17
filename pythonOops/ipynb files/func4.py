# def Add(a, b, *arg):  # arg is just a variable name
#     print(a)
#     print(b)
#     print(arg)
#     print(a + b + arg[::-1][0])
#
#
# Add(10, 20, 30)
# print('\n-------------------\n')
# Add(10, 20, 30, 40, 50)

# def Add(a, b, **kwarg):  # kwarg is just a variable name
#     print(a)
#     print(b)
#     print(kwarg)
#     print(a + b + kwarg["y"])
#
#
# Add(10, b=20, y=30)
# print('\n-------------------\n')
# Add(10, b=20, x=20, y=30)

def Add(a, b, *arg, **kwarg):  # kwarg is just a variable name
    print(a)
    print(b)
    print(arg)
    print(kwarg)
    print(a + b + arg[0], kwarg["x"])


Add(10, 20, -1, -2, 5, x=20, y=30)
print('\n-------------------\n')
Add(20, -1, -2, 5, x=20, y=30)

# Add(5, x=20, b=30)
# Add(1, 2, 3, 20, x=20, y=30)
