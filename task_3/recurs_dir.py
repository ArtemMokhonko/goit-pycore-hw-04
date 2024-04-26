from pathlib import Path
from colorama_utils import print_directory

def dir_structure(dir_path: Path, space=0):
    print_directory(dir_path.name, space, is_dir=True)
    for el in dir_path.iterdir():
        if el.is_dir():
            dir_structure(el, space + 1)
        else:
            print_directory(el.name, space+1, is_dir=False)