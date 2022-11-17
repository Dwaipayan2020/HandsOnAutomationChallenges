lst = list()
se = set()
tu = tuple()
# print('------------ Methods accessible by a LIST ---------------\n')
# print(dir(lst))
# print('--------------- Methods accessible by a SET ------------\n')
# print(dir(se))
# print('\n------------ Methods accessible by a TUPLE ---------------')
# print(dir(tu))
lst2 = [4, 5, 6, 6]
lst3 = [6, 7, 8, 9]
tu2 = (9, 5, 6)
se2 = {10}
lst4 = [0, 5, 9]

print(list({1, 2, 3}))
print(set(lst2).intersection(set(lst3)))
"""Tuple can not be directly converted in a set
It must be converted to a list first."""

print(set(list(tu2)))
print(tuple(se2))
print(tuple(lst4))