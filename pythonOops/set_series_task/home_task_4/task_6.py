""" WAP to input a string and
print the ASCII value of each character
in the string.
"""

str = str(input('Input a String:\n'))

for ch in str:
    print(ch, ord(ch), end='\n')
