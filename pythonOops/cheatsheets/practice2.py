"""Unlike strings, lists are mutable sequences in python.
   String Slicing examples
"""

my_list = [1, 2, '3', True]
print(len(my_list))  # 4
print(my_list.index('3'))  # 2
print(my_list.count(2))  # 1 --> count how many times 2 appears
print(my_list[3])  # True
print(my_list[1:])  # [2, '3', True]
print(my_list[:1])  # [1]
print(my_list[-1])  # True
print(my_list[::1])  # [1, 2, '3', True]
print(my_list[::-1])  # [True, '3', 2, 1]
print(my_list[0:3:2])  # [1, '3']
# : is called slicing and has the format [ start : end : step ]
