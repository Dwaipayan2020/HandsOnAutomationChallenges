"""Print Elements at Odd indexes
from a list (Using for loop)
l = [10,11,20, 21,30, 31, 40, 41]
"""

lst = [10, 11, 20, 21, 30, 31, 40, 41]

for el in lst:
    el_index = lst.index(el)
    if el_index % 2 != 0:
        print('\n', el, el_index)
