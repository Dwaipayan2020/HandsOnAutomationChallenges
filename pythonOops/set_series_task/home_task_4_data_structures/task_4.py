s = "Python is Object Oriented"

print(s[1:1])
print(s[:-1])
print(s[4:10])

# s2 = ‘a#b#c#d#’
# print(s2)

# s3 = ''
# print(s3[1])
s4 = "a#b#c#d#"
print('s4 after split', s4.split())
print(s4.split("#"))
l5 = s4.split("#")
s5 = "$".join(l5)
print(s5)

s6 = "abcba"
print(s6.count('a'), end="  , ")
print(s6.count('A'), end="  , ")
print(s6.count('a', 2, 4), end="  , ")
