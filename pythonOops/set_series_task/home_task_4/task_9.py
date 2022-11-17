"""WAP to input a list of numbers and store in a tuple.
Now input another number and print the
index of this number in the tuple.
"""
import sys

numbers = list()
sys.stdout.write('Input Numbers:\n')
for i in range(5):
    n = int(input())
    numbers.append(n)

tpl_nums = tuple(numbers)
print('tuple is ', tpl_nums)
k = int(input('Enter a new number to be added in the tuple :\n'))
print('added ', k, ' to the tuple')
new_tpl_nums = tpl_nums + (k,)
print('new tuple : ', new_tpl_nums, end='\n')
print('Index of newly added number: ', k, ' is ',  new_tpl_nums.index(k))
