"""WAP to input 2 strings and swap the strings
"""

s1 = str(input("Please Enter First String : \n"))
s2 = str(input("Please Enter Second String : \n"))
print('\nBefore Swap, First String: ', s1, ', Second String:', s2)
# Swapping two strings
s1, s2 = s2, s1
print('\nAfter Swap, First String: ', s1, ', Second String:', s2)

