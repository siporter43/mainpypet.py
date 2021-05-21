from pathlib import Path

"""fncns"""

def main():
    """we're trying to list the contents of data directory"""
    path = Path("data") / "tmp"
    for f in path.iterdir():
        print(f.name)

def file_touch():
    path = Path("alissa.py")
    path.touch(exist_ok=True)
    print("calf stretch")

def new_data():
    path = Path("data")
    path.mkdir(exist_ok=True)
    new_file = path / "blah.txt"
    new_file.touch()
    print("blah blah blah")    

def del_tmp():
    path = Path("data/tmp/file_3.txt")
    print(path.absolute())
    if not path.exists():
        print("Ain't nothing here, boyo")
        return

    answer = input("Do you wanna delete this forever Yes or No?...")
    if answer == "Yes":
        path.unlink(missing_ok=True)
    else:
        print("Look at this Captain Planet over here!")
    # print("He's dead, Jim")

def del_bingo():
    path = Path("data/tmp/bingo.txt")
    print(path.absolute())
    path.rmdir()
    print("Kill it with fire")

def create_flashcard():
    path = Path("flashcards.csv")
    path.mkdir(exist_ok=True)
    print("You got your flashcard directory, broseph")

def samp_flash():
    path = Path("flashcards.csv")
    new_file = path / "sample_1"
    new_file.touch(exist_ok=True)
    print("Success")

def flash_instr():
    path = Path("flashcards.csv")
    start_file = path / "intro.py"
    start_file.touch(exist_ok=True)
    print("Let's get it started")
    fh = open("flash_instr.py", "w")



"""script runner"""

# main()

# file_touch()

# new_data()

# del_tmp()

# del_bingo()

# create_flashcard()

samp_flash()
