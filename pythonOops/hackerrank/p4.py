se = set()
l = [1, 2, 3]
se.update(l)
se.add(4)
l2 = ['a', 'b', 'c', 'd', 'c', 'd', 'e', 'e']

for item in set(l2):
    print(f'{item} = {l2.count(item)}')
print(se)

print(l.count(3))
