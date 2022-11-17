"""Question: Write lambdas to:
a. Square a number x2
b. Inverse a number 1/x
c. Negate a number
"""

import sys
num_list = [1, 2, 3, 4, 5]
sqr_lam = lambda x: x ** 2
inverse_lam = lambda x: 1 / x
negate_lam = lambda x: (-x)
[print(sqr_lam(x)) for x in num_list]
sys.stdout.write('--------------------------\n')
[print(inverse_lam(x)) for x in num_list]
sys.stdout.write('--------------------------\n')
[print(negate_lam(x)) for x in num_list]


