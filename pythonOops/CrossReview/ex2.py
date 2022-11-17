def get_args(*args, **kwargs):
    d = kwargs
    res = 0
    if d is None:
        res = sum(list(args))
    else:
        r1 = sum(list(args))
        r2 = sum([i[1] for i in d.items()])
        res = r1 + r2
    return res


#
# print(get_args(1, 2, x=5, y=10))
print(get_args(1, 2, {'x': 5, 'y': 10}))
# print(get_args(1, 2))
