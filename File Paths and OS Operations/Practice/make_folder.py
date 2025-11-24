# Exercise B - Create a folder if Missing

'''
Ask the user for a folder name
- if it doesn't exists -> create it
- if it exists -> print "Already exists."
'''

from pathlib import Path

folder = str(input("Folder name: "))
p = Path(folder)

if p.exists():
    print("Already exists")
else:
    try:
        p.mkdir(parents=True, exist_ok=True)
        print("Created:", p)
    except Exception as e:
        print("Error Creating Folder: ", e)
    