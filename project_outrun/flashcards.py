# Short descr.

"""this is where we create our flashcards for class"""

# Directions

"""
Part 1: Make CSV (filetype/space to keep it)
    [x] Create a folder data/flashcards if it doesn’t already exist
    [x] Make a csv file with flashcard data
    [x] In the data/flashcards directory manually make file ending in .csv. For example paths.csv.
    [x] Each line should be one card with the format: text for front, text for back.

Part 2: Start flashcards.py (create workspace to create and call flashcards)
    [x] write a main() function
    [x] print any temporary debug message in it
    [x] call it

Part 3: Start load_csv() (create this new fncn)
    load_csv()
        [x] write a load_csv() function that takes one argument: path
        [x] check to make sure the csv file exists. If not, print an error
            message that includes the path then return
        [x] print a temporary debug message: loading file: path
    in main()
        [x] make a Path object to your csv file
        [x] call your load_csv() function, passing it your Path object as the
            argument, and assign the returned value to a variable named cards

Part 4: Read each line of the csv file
    [x] open the csv file in read mode using the open() function
    [x] use fh.readlines() to iterate through each line in the file
    [x] for temporary debugging, print each line

Part 5: Get the card data from the csv file
    [ ] make an empty dict assigned to a variable named card
    [ ] split each line on the "," using the .split() method and assign the result to a variable named row
    [ ] check that there are two items in the row using the len() function. If not print an error message and return
    [ ] assign card["front"] to the first item in the row, and card["back"] to the second
    [ ] for temporary debugging, print the card dict

"""

# imports

from pathlib import Path
import random
from sys import stderr

# global variables

# fncns

def load_csv(path):
    """this fncn will check existence and read/print every line in the file"""
    if path.exists():
        print(f"File {path} already exists, bro")
    else:
        print(f"{path} not here. Make it")
        return
    print(f"loading file: {path}")
    
    # this part is to open, read, and print the card info
    fh = open(path)
    card_info = fh.readlines()
    for line in card_info:
        print(f"{line} \n")
    fh.close()

    print(card_info)


def main():
    """this is the fncn to call the load_csv"""
    # /Users/vision/code/project_outrun/data/flashcard_project/paths.csv
    path = Path("data") / "flashcard_project" / "paths.csv"

    cards = load_csv(path)

    print("Call me Butter because I'm on a roll!")



# runner

main()

# load_csv("paths.csv")
