# Short descr.

"""this is where we create our flashcards for class"""

# Directions

"""
https://alissa-huskey.github.io/python-class/exercises/flashcards.html#part-9-start-the-play-function
Part 1: Make CSV (filetype/space to keep it)
Part 2: Start flashcards.py (create workspace to create and call flashcards)
Part 3: Start load_csv() (create this new fncn)
Part 4: Read each line of the csv file
Part 5: Get the card data from the csv file
Part 6: Return the card data to main()¶
    Have load_csv() put all of the card dictionaries into one big cards list and return that to main().
        in load_csv(), before the readlines() loop
            [x] make an empty list assigned to a variable named cards

        in load_csv(), at the end of the readlines() loop
            [x] use the .append() method on the cards list with the argument card

        in load_csv(), after the loop
            [x] return cards

        in main()
            [x] if the cards list is falsy, return
            [x] otherwise, print the cards list for temporary debugging
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
    cards = []
    fh = open(path)
    card_info = fh.readlines()
    for line in card_info:
        named_card = {}
        row = line.split(",")
        named_card["front"] = row[0]
        named_card["back"] = row[1]
        if len(row) != 2:
            print("errir, too many items")
            return
        cards.append(named_card)
        print(f"{line} \n")
    fh.close()
    return cards


def main():
    """this is the fncn to call the load_csv"""
    # /Users/vision/code/project_outrun/data/flashcard_project/paths.csv
    path = Path("data") / "flashcard_project" / "paths.csv"

    cards = load_csv(path)

    if cards == False:
        return
    else:
        print(cards)    
    print("Call me Butter because I'm on a roll!")

# below is just an attempt to create a file

def swing_thing():
    path = Path("June28.py")
    print(f"Touching file {path}")
    path.touch()

# runner


# main()

swing_thing()
# load_csv("paths.csv")
