# opening file python script

# built-in open() function
# 1st arguement, file name in current directory or file path
# 2nd argument, mode: "r" read, "w" write, "a" append (adds to bottom)
file = open("example.txt", "r")
content = file.read()
print(content)

# must call file.close() ro the file stays open and locked.
file.close()