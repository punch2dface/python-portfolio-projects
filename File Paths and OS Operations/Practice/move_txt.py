# Excerise C - Move all .txt Files to a Folder

'''
Create a folder named TextFiles
Move all .txt files in the current directory into it.
'''

from pathlib import Path
import shutil

path = Path(".")
dest = Path("TextFiles")
dest.mkdir(exist_ok=True)

for item in path.iterdir():
    if item.suffix == ".txt":
        shutil.move(str(item), dest / item.name)