# Functions in Python

def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# Mini-Check: Make a function that returns if a number is even or odd

def oddOrEven(num):
    if num % 2 == 0:
        return f"{num} is even"
    else:
        return f"{num} is odd"

print(oddOrEven(10))
print(oddOrEven(7))
print(oddOrEven(0))
print(oddOrEven(-3))