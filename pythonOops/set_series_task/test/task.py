a = [x * x for x in range(4)]
b = {x * x for x in range(4)}
c = (x * x for x in range(4))
d = {x: x * x for x in range(4)}

print(a, '\n')
print(b, '\n')
print(c, '\n')
print(d, '\n')
# print(d.items(), '\n')

"""
o/p 1 : [0,1,4,9]
o/p 2 : {0,1,4,9}
o/p 3 : (0,1,4,9)
o/p  : {0:0,1:1,4:4,9:9}
"""

#
# def update_list(val, list=[]):
#     list.append(val)
#     return list
#
#
# list1 = update_list(10)
# list2 = update_list(123, [])
# list3 = update_list('a')
#
# print(list1)
# print(list2)
# print(list3)
#
#
