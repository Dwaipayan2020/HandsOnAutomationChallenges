l1 = ['A', 'B', 'C', 'D']
l2 = ['Apple', 'Ball', 'Cat', 'Dog']
d1 = dict(zip(l1, l2))
d3 = d1.items()
d2 = list(d3)[::2]
print(d1)
print(d3)
print(d2)
