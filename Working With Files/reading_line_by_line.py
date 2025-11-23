# reading line by line python

# option A - .readlines():

with open("example.txt", "r") as files:
    lines = files.readlines()
    for line in lines:
        print(line)

# option B - Loop directly (preferred)

with open("example.txt", "r") as files:
    for line in files:
        print(line)