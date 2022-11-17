from functools import reduce
from math import *

"""Map
"""
lst = [1, 4, 8, 16, 25, 36, 49]
# tu = tuple(lst)
print('lst :', lst, end='\n\n')
m_lam = lambda x: pow(x, 2)

m = map(m_lam, lst)
lst_m = list(m)
# tu_m = tuple(lst_m)
print('After mapping (map) : ', lst_m)

"""Filter
"""
f_lam = lambda x: x % 4 == 0

f_obj = filter(f_lam, lst_m)

lst_f = list(f_obj)
print('\n After filtering (filter): ', lst_f)
"""Reduce
"""
r_lam = lambda x, y: x + y

# tu_f = tuple(lst_f)
r = reduce(r_lam, lst_f)

print('\n After reducing (reduce): ', r)
