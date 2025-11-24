# Mini-Project: "Stats Helper"

'''
Create a script taht does the following:
A) Create a list of numbers
- hardcoded or user-input, exmaple:
    - numbers = [5, 10, 15, 20, 25]
B) Write the following function:
    - 1. get_min(numbers) > returns the smallest value
    - 2. get_max(numbers) > returns the largest value
    - 3. get_average(numbers) > returns mean
    - 4. get_range(numbers) > returns max-min
    - 5. summarize(numbers) > returns a dictionary
C) Print the Summary
'''

num_list = [5, 10, 15, 20, 25]

def get_min(numbers):
    if not numbers:
        return None
    return min(numbers)

def get_max(numbers):
    if not numbers:
        return None
    return max(numbers)

def get_average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

def get_range(numbers):
    if not numbers:
        return None
    return get_max(numbers) - get_min(numbers)

def summarize(numbers):
    return {"min": get_min(numbers), "max": get_max(numbers), "average": get_average(numbers), "range": get_range(numbers)}

print(summarize(num_list))