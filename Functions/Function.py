# Function Python

'''
Basic Function Anatomy
- def > defines a function
- greet > name of the function
- () > parameters go here (empty in this case)
- : > start block
- indentation defines the function body
'''

def greet():
    print("Hello!")

greet() # calls the greet function
    
'''
Parameters vs. Arguments
'''

# Parameters - variables inside the function definition

def greet(name): # name is a parameter
    print("Hello", name)

# Arguments - actual values you pass in

greet("Ben") # "Ben" is an argument

'''
Default Parameters
- Useful when you want a function to work even if arguments are not passed.
'''

def greet(name="friend"):
    print("Hello", name)

greet("Ben") # prints Hello Ben
greet() # prints Hello friend

'''
Keyword Arguments
- call a function by explicitly naming the parameter
- order does not matter
- improves readability
'''

def describe_pet(name, animal_type):
    print(f"{name} is a {animal_type}")

describe_pet(animal_type="dog", name="Buddy")

'''
*args - Arbitrary Positional Arguments
- Use *args when you do not know how many arguments the user will pass
- *args becomes a tuple of all extra positional arguments
- great for
    - calculators
    - aggregators
    - logging
    - flexible API design
'''

def add_numbers(*args):
    return sum(args)

print(add_numbers(1, 2, 3))
print(add_numbers(10, 20, 30, 40, 50))

'''
**kwargs - Arbitrary Keyword Arguments
- use this when you do not know which named arguments will be passed
- useful for:
    - configuration systems
    - passing settings
    - dynamic function behavior
'''

def print_info(**kwargs): # **kwargs becomes a dictionary
    for key, value in kwargs.items():
        print(key, "=", value)
        
print_info(name="Ben", age=26, city="LA")

'''
Returning Values
'''

# Basic return

def multiply(a, b):
    return a * b

# returning multiple values

def math_ops(x, y):
    return x + y, x - y, x * y

sum_, diff, product = math_ops(10, 3) # variable ordering must match with the return ordering

# returing lists or dictionaries

def student_record(name, grade):
    return {"name": name, "grade": grade}

'''
Common Mistakes to Avoid
'''

# Forgeting to return

# a + b does nothing, must return a + b
def add(a, b):
    a + b 
    
# using mutable default arguments

# avoid
def bad_func(data=[]):
    data.append(1)
    return data

# Use
def good_func(data=None):
    if data is None:
        data = []

# confusing *args and **kwargs
# - *args = positional
# - **kwargs = keywords/named
# they can be combined

def demo(a, b, *args, **kwargs):
    print(a, b, args, kwargs)
