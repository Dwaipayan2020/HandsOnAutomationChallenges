"""Create a list of 5 random numbers and then print the list,
sum of all numbers and average.
Use a for loop.
"""

# importing the random module
import random

random_numbers_set = set()
for i in range(10):
    random_numbers_set.add(random.randint(0, 9))
    if len(random_numbers_set) == 5:
        break
random_num_lst = list(random_numbers_set)
print('List is : ', random_num_lst)
print('\nSum of all numbers : ', sum(random_num_lst))
print('Average of all numbers : ', sum(random_num_lst)/len(random_num_lst))
