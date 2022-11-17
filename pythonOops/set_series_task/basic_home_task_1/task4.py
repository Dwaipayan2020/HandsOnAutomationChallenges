""" WAP to input a number and print its square root ()
"""

import math as m
import sys

num = int(input("Enter a number\n"))
result = m.sqrt(num)
sys.stdout.write(f'{result}')
