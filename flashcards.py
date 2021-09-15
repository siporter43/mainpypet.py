"""Flashcards

    Setup
    -----
    1. [x]Create a folder data/flashcards if it doesn't exist
    2. [ ]Make flashcard csv files
        [x] In the data/flashcards directory manually make file called ending in .csv
        [ ] Each line should be one card with the format: "text for front, text for back".
       Here is my "paths.csv" example:

       front, back
       import the Path class, from pathlib import Path
       check if Path object path exists, path.exists()
       check if Path object path is a file, path.is_file()
       check if Path object path is a directory, path.is_dir()

    Exercise
    --------
    1. Start your flashcards.py file
       [ ] write a main() function, and in it print something, then call it
    2. Write a load_csv() function
       [ ] open the csv file you made using the `open()` function
       [ ] use `fp.readlines()` to iterate through each line in the file
"""
"""imports"""

from pathlib import Path

DATA_DIR = Path("data/flashcard_project")

"""fncns"""

def del_samp():
    # this fncn is to del a file from a directory that was useless. not for the project
    path = Path("flashcards.csv/sample_1")
    if not path.exists():
        print("it's not there bro")
        return
    path.unlink()
    print("Get gone")

def del_olddir():
    # this is to del a directory that was unnecessary. not for project
    path = Path("flashcards.csv")
    path.rmdir()
    print("Useless thing gone now")

def flashcard_proj():
    # now we're making the directory for our project
    path = Path("data") / "flashcard_project"
    path.mkdir(exist_ok=True)
    print("Make it so")

def change_flashname():
    # /Users/vision/code/project_outrun/flaschards.py
    from_path = Path.cwd() / "flaschards.py"
    to_path = Path.cwd() / "flashcards.py"
    if not from_path.exists():
        print("Clean it up")
        print(from_path)
        return
    from_path.replace(to_path)
    print("nice one")

def flash_files():
    # here we're creating our flashcard csv files and trying to put "setup" example on step 2
    path = DATA_DIR / "paths.csv"
    response = input(f"{path} \n do you want to create this file? ").upper()
    if response != "YES":
        print("Not my name")
        return
    print("It's happening")
    path.touch()

"""runner"""

# del_olddir()

# del_samp()

# flashcard_proj()

# change_flashname()

# flashcard_proj()

# flash_files()
