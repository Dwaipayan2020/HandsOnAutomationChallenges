"""WAP to input a number and print its factorial.
Factorial is denoted by n!,
where n is the number whose factorial is to be found.
        Ex: if n = 4 output should be 24
        4! = 1x2x3x4 = 24
"""
import sys
sys.stdout.write('Input a number to find its factorial:\n')
n = int(input())
factorial = 1
for i in range(n):
    factorial = factorial * (i+1)
print(f'Factorial of {n} is :\n', factorial)
