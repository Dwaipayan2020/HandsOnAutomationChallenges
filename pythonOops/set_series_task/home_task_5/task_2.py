"""WAP to generate 4 random numbers in the range 0-26
and print their average
"""

# importing the random module
import random

random_numbers_set = set()
for i in range(10):
    random_numbers_set.add(random.randint(0, 26))
    if len(random_numbers_set) == 4:
        break
print('Generated random numbers: ', random_numbers_set)
print('Average of all numbers : ', sum(random_numbers_set) / len(random_numbers_set))
