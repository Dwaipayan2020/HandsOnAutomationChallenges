lst = list()
se = set()
tu = tuple()

"""Common methods between a list and a set
"""
print('------------ Common Methods LIST and SET ---------------\n')
print(set(dir(lst)).intersection(set(dir(se))))
"""Distinct methods inside a list
"""
print('------------ Distinct Methods in list but not in set ---------------\n')
common_set = set(dir(lst)).intersection(set(dir(se)))

print(set(dir(lst)) - common_set)
print('------------ Distinct Methods in set but not in list ---------------\n')
"""Distinct methods inside a set 
"""
print(set(dir(se)) - common_set)

print('\n------------ Common Methods in list and tuple  ---------------\n')
print(set(dir(lst)).intersection(set(dir(tu))))

print('\n------------ Distinct Methods in list but not in tuple  ---------------\n')
print(set(dir(lst)) - set(dir(lst)).intersection(set(dir(tu))))
print('\n------------ Distinct Methods in tuple but not in list ---------------\n')
print(set(dir(tu)) - set(dir(lst)).intersection(set(dir(tu))))

print('\n------------ Common Methods in list, tuple and set  ---------------\n')
print(set(dir(lst)).intersection(set(dir(tu))).intersection(set(dir(se))))
# print('------------ Methods accessible by a LIST ---------------\n')
#
# print('--------------- Methods accessible by a SET ------------\n')
# print(dir(se))
# print('\n------------ Methods accessible by a TUPLE ---------------')
# print(dir(tu))
