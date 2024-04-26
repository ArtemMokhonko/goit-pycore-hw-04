import sys
from pathlib import Path
from recurs_dir import dir_structure

def main():
    try:
        dir_path = Path(sys.argv[1])
        if dir_path.is_dir():
            dir_structure(dir_path)
        else:
            print("It's not a dir")
    
    except FileNotFoundError:
        print("no file")

    except Exception as error:
        print(error)


if __name__=="__main__":
    main()
