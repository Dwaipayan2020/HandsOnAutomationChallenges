"""WAP to join a list and a tuple:
L = [1,3,5,7]
T = (8,6,4,2)
"""

t = (8, 6, 4, 2)
L = [1, 3, 5, 7]
lst = list(t)
res = list(lst + L)
print(res)
