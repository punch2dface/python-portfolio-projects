from pathlib import Path
import os

word_count = 0
line_count = 0
file_size = 0
last_date_modified = ""

    

# open hello.txt file with only read permissions
with open("hello.txt", "r") as file:
    # read everything inside the text file
    text = file.read()
    
    file_size = os.stat("hello.txt").st_size
    
    word_count = len(text.split())
    line_count = len(text.splitlines())

print("Line count:", line_count)
print("Word count:", word_count)
print("Character count:", len(text))

'''    # split the text into list of words
    for word in text.split():
        word_count += 1'''
    
    



'''    # split the text into lines
    for line in text.splitlines():
        line_count += 1'''
    
'''print(file_size / 1000)
print(word_count)
print(line_count)
print(len(text))'''

