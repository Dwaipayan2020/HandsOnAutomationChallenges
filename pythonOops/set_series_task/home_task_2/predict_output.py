from functools import reduce
from math import sqrt

f = lambda x, y: x if x > y else y
l = [10, 30, 50, 30, 10]
num = reduce(f, l)
print(num)
# Output 50

func_root = lambda x: sqrt(x)
func_inverse = lambda  x: 1/x
num_list = [1, 4, 16, 64]
# print(list(map(func_root, num_list)))

[print(func_root(x))for x in num_list]
[print(func_inverse(x))for x in list(map(func_root, num_list))]
