"""WAP to generate and print a random capital alphabet.
"""

# importing the random module
import random
import string

# Two different ways to get a random capital alphabet
RAND_S1 = chr(random.randint(ord('A'), ord('Z')))
RAND_S2 = random.choice(string.ascii_letters).upper()
print('Generated random numbers: ', RAND_S1, RAND_S2)
