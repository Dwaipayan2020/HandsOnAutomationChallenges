"""Input: AAABBCDD

output: A3B2C1D2"""
from functools import reduce
from collections import Counter

s1 = "AAABBCDD"
counter = Counter(list(s1))
lst = list()
s = None
for k, v in counter.items():
    s = f'{k}{v}'
    lst.append(s)
# print(lst)
len_lst = len(lst)

# reduced = reduce(lambda x, y: f'{lst[x]}{lst[y]}' if y == (x + 1) else None, lst)

print(''.join(lst))
