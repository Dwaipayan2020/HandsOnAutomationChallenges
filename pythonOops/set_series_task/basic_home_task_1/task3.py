""" Questions: WAP to input a string s and a number n. Print the string n times on the screen,
   each should appear in a separate line (do not use any kind of loops, use the multiplication operator)

"""

import sys
s = str(input("Input a String\n"))
n = int(input('Enter the multiplier\n'))
s_str = s + '\n'
result = (s_str * n)
sys.stdout.write(f'{result}')
