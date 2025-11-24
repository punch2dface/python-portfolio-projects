# Exercise A - Using standard library modules

'''
Tasks:
- use the following modules and print:
    - a random integer between 1 and 100 (random)
    - the square root of 144 (math)
    - the current working directory (os)
'''
# imports
import random
import math
import os

# get a random integer between 1 - 100
random_integer = random.randint(1, 100)
print (random_integer)

# get the square root of 144
sqr_root = math.sqrt(144)
print(sqr_root)

# get the current directory
curr_directory = os.getcwd()
print(curr_directory)