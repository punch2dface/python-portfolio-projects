# Handling Exceptions Python

# Exception - an error that stops your pragram unless you handle it

# Example: 
# - 10/0 : ZeroDivisionError
# - int("Hello") : ValueError
# - open("Nope.txt") : FileNotFoundError

# Basic Structure
# try:
#    # risky code (might crash)
# except:
#    # what to do if an error happens

try:
    x = 10/0
except:
    print("Something went wrong!")
    
# Output: Something went wrong! - due to ZeroDivisionError
# Catching Specific Exceptions

try:
    num = int(input("Enter a number: "))
except:
    print("You didn't enter a valid number.")
    
# The else and finally blocks
# else - runs if NO error happens.

try:
    num = int("5")
except:
    print("invalid")
else:
    print("conversion worked!")

# finally - runs wheterh an error happened or not.

try: 
    file = open("hello.txt")
except FileNotFoundError:
    print("file missing")
finally:
    print("Done trying!")
    
    
# Real Example: Safer File Reading
# Without exceptions:
# file = open("Hello.txt", "r")
# - this crashes if the file doesn't exist.

# With Exceptions

try:
    with open("hello.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found!")
    