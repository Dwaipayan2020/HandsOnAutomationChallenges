"""Use reduce function and an appropriate lambda
to find the maximum number in a list.
"""

import sys
from functools import reduce

num_list = [1, 2, 3, 4, 5]
funct = lambda n, m: n if n > m else m
max_val = reduce(funct, num_list)
sys.stdout.write('-----------Maximum Value---------------\n')
print(max_val)
