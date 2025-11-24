# Exercise A - Inspect a Folder

'''
Goal: Print
- number of files
- number of folders
- total size in MB
- list of all filenames
'''

from pathlib import Path

path = Path(".") # current directory

file_count = 0
folder_count = 0
total_size = 0
filename_list = []

for item in path.iterdir():
    if item.is_file():
        file_count += 1
        total_size += item.stat().st_size
        filename_list.append(item)
    elif item.is_dir():
        folder_count += 1

print(path.resolve())

print("Files:", file_count)
print("Folders:", folder_count)
print("Total size (MB):", round(total_size / (1024 * 1024), 2))

for file in filename_list:
    print(" - ", file.name)