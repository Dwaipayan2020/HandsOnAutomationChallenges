"""WAP to input 10 numbers repeatedly (using range based for loop)
and store them in a list."""
import sys
input_taker = list()
sys.stdout.write('Enter 10 numbers:\n')
for i in range(10):
    n = int(input())
    input_taker.append(n)

print(input_taker)
