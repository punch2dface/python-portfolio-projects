# File Paths & OS Operations (Beginner -> Intermediate)

# Python give you two main tools for working with files and folders:
# - 1. os module - older but still widely used
# - 2. pathlib module - modern, cleaner, easier
# (will use both so I understand real-world code)'''

# Part A - Understand File Paths

# There are 2 types of paths:
# - 1. Absolute path
#     - C:\Users\Ben\Downloads
#     - /home/user/documents
# - 2. Relative path
#     - ./hello.txt       # file in the same folder
#     - ../other_folder   # one folder up

# pathlib.Path
# - Path behaves like a smart object instead of a string.

from pathlib import Path
import os

p = Path("hello.txt")
print(p.exists())  # checks if hello.txt is in current folder
print(p.resolve()) # full absolute path

# Part B - OS operations you must know

# 1. Check if a file/folder exists

from pathlib import Path

p = Path("hello.txt")
print(p.exists())

# 2. Create a folder

Path("NewFolder").mkdir(exist_ok=True)

# 3. List all files in a folder

folder = Path(".")
for item in folder.iterdir():
    print(item)
    
# 4. Delete

Path("old.txt").unlink()    # delete file
Path("OldFolder").rmdir()   # delete empty folder

# 5. Move/Copy (using shutil)

import shutil

shutil.copy("a.txt", "backup/a.txt")
shutil.move("a.txt", "Archive/a.txt")