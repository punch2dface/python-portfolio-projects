# Milestone 2 practice Python

# Exercise A - Create a file named hello.txt containing: "My first file from python!"

with open("hello.txt", "w") as files:
    files.write("My first file from Python!\n")
    
# Exercise B - Append Another line: This is an appended line.

with open("hello.txt", "a") as files:
    files.write("This is an appended line.\n")
    
# Exercise C - count how many lines are in hello.txt

line_count = 0
with open("hello.txt", "r") as files:
    for lines in files:
        line_count += 1

print(f"Number of lines: {line_count}")

# Exercise D - read a file and print only lines longer than 10 characters

with open("hello.txt", "r") as files:
    for lines in files:
        if len(lines) > 10:
            print(lines.strip())