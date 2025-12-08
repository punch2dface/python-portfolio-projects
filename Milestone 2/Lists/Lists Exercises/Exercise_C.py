# Exercise C - List Filtering

'''
Given a list: 
- numbers = [3, 10, 15, 22, 1, 7, 30, 12]
output only numbers greater than 10, using a list comprehension.
- expected result: [15, 22, 20, 12]
'''

numbers = [3, 10, 15, 22, 1, 7, 30, 12]

result = [x for x in numbers if x > 10]

print(result)