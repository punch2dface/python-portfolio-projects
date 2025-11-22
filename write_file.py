# writing in file python

# writing fully replaces the file contents:
# if file path/file does not exist, python creates it

with open("log.txt", "w") as file:
    file.write("Hello World!\n")
    

# overwrites the current file with a new text
with open("log.txt", "w") as file:
    file.write("overwrite the previous text.")