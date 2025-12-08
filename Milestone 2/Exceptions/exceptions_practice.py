# Exception Practic Python

# Exercise A

# ask the user for two numbers
# divide them
# if the user enters something that isn't a number -> print a useful message
# if the user tries to divide by zero -> print a useful message


try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print(f"{num1} / {num2} = {result}")
except ValueError:
    print("You have entered an invalid number!")
except ZeroDivisionError:
    print("Unable to divide!")


# Excerise B - File Reader with Errors

# ask the user for a filename
# tries to open it
# if file doesn't exist -> print "That file does not exist."
# if file opens successfully -> print the first line


try:
    with open(input("Enter a file name: "), "r") as file:
        print(file.readline())
except FileNotFoundError:
    print("That file does not exist.")


# Exercise C - Improved Word Counter

# modify code to safely:
# - catch missing file errors
# - catch unreadable file errors
# - use finally to print "Done!" no matter what.

'''
# original code
filename = input("Enter a file name: ")
file = open(filename, "r")
print(file.read())
'''

try:
    filename = input("Enter a file name: ")
    file = open(filename, "r")
    print(file.read())
except FileNotFoundError:
    print("File not found!")
except (PermissionError, IsADirectoryError, UnicodeDecodeError):
    print("File is unreadable!")
finally:
    print("Done!")
