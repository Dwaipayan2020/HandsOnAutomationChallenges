"""Use range based for loop to store all upper case alphabets
and their corresponding ASCII values in the dictionary d.
The result should be d = {‘A’: 65, ‘B’:66,…..}
"""

x = ord('A')
y = ord('Z')
d = dict()
for i in range(x, y + 1):
    alp = chr(i)
    d[alp] = i
print(d)
