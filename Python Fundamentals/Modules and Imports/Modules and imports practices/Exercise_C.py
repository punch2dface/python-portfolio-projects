# Exercise C - Cleaner Import Styles

'''
Tasks:
Modify Exercise_B.py to use:
- IMport only one function
- import with an alias.
'''

# Import
# import helpers
from helpers import shout
import helpers as h

print(shout("hello")) # output HELLO!
print(h.add(3, 4)) # output 7
print(h.triple(5)) # output 15