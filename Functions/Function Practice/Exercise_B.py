# Exercise B - using args

'''
write a function called calculate_average:

requirements:
- accept any amount of numbers using *args
- return the average of all numbers passed
- if no numbers are passed, return 0
'''

def calculate_average(*args):
    if not args:    # if args is empty (no arguments passed)
        return 0
    else:
        return sum(args) / len(args)
    
print(calculate_average(10,20,30))
print(calculate_average())