# Exercise C - Student Grades Lookup

'''
Create a dictionary:

grades = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}

Ask the user for a name.
If the name exists > print the grade.
If not > print "Student not found."

Use:

if name in grades:

'''

grades = {
    "Alice": 85, 
    "Bob": 92,
    "Charlie": 78
}

name = str(input("Enter a name: ").title())

if name in grades:
    print(grades[name])
else:
    print("Student not found.")