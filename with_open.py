# Using with open() (the recommended way)

# modern and safe way - Python will automatically close the file for you.
# do not need file.close() - pyhton handles it for you.

with open("example.txt", "r") as file:
    content = file.read()
    print(content)