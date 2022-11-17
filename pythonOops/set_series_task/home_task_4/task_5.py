"""WAP to input a string and print individual characters
in the string using for loop.
"""
str = str(input('Input a String:\n'))

for ch in str:
    print(ch, ord(ch), end='\n')
    # print(ch, end='\n')

