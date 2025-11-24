# Exercise B - Create your own module

'''
Tasks:
- create a file called helpers.py
    - inside it, create 3 functions:
        - shout, add, and triple
- in the main file, import the helper file and use all three functions. 
'''

# Import
import helpers

print(helpers.shout("hello")) # output HELLO!
print(helpers.add(3, 4)) # output 7
print(helpers.triple(5)) # output 15