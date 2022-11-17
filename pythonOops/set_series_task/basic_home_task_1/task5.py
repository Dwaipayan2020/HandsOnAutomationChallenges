"""WAP to input 4 numbers from user and print their average
"""

import sys

input_integers = list()
for i in range(4):
    num = int(input(f'Enter number at index {i} \n'))
    input_integers.append(num)
result = sum(input_integers) / len(input_integers)
sys.stdout.write(f'Average of four inputs -> {result}\n')
