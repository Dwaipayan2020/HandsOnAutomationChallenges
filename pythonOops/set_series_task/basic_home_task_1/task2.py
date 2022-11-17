"""Question: WAP to input 2 numbers and print their sum and difference

"""

import sys
num1 = int(input("Enter first number\n"))
num2 = int(input("Enter second number\n"))
sys.stdout.write(f'Sum of the inputs \n  {num1+num2}\n')
sys.stdout.write(f'Difference between the inputs \n  {abs(num1-num2)}\n')