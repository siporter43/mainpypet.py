"""this is a continuation of last week's path work"""

from pathlib import Path

# fncns
def path_print():
    """
    [x] find file to print contents of (groceries.txt)
    [ ] make a path object relative to the current file w/ __file__ 
    [ ] have it join up
    [ ] open the file with fh
    [ ] print it
    [ ] ...?
    """
    # /Users/vision/code/project_outrun/data/groceries.txt
    basedir = Path(__file__).parent.parent  / "data" / "groceries.txt"

    if not basedir.is_file():
        print(f"Not here, buddy {basedir}")
        return

    with open(basedir) as fh:
        contents = fh.read()
    
    print(contents)

def main():
    """so the thing we are doing here is writing a fncn to check if our contacts.txt exists then printing its contents using"""    
    path = Path("data/contacts.txt")
    if not path.is_file():
        print("Sorry no such file exists. Try investing in bitcoin")
        return
    fh = open(path)
    contents = fh.read()
    fh.close()
    print (contents)

# script runner

# main()

path_print()
