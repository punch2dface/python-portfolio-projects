# append file python

# write new entry without overwriting the pre-existing text. 
with open("log.txt", "a") as file:
    file.write("New Entry!\n")