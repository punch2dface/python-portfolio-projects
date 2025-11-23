# Exercise A - Default Arguments

'''
write a function called greet_user:

requirements:
- it should take a parameter name
- it should have a default value of "friend" if no name is provided
- it should print: "Hello, <name>!"
'''

def greet_user(name="friend"):
    print(f"Hello, {name}!")

greet_user("Ben")
greet_user()
