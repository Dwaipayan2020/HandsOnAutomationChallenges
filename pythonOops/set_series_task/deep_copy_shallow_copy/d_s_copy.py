
"""Shallow Copy"""
import copy

print('Performing Shallow Copy')
L1 = [1, 3, 5, 7, [1, 2, 3, 4]]
L2 = L1.copy()
L2[4][0] = 0

print(L2, id(L2))
print(L1, id(L1))


"""Deep Copy"""
print('\n\nPerforming Deep Copy')
L3 = [1, 3, 5, 7, [1, 2, 3, 4]]
L4 = copy.deepcopy(L3)
L4[4][0] = 0

print(L4, id(L4))
print(L3, id(L3))