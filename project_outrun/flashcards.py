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
Part 7: Remove extra whitespace
Part 8: Skip the Header row

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
        named_card["front"] = row[0].strip()
        named_card["back"] = row[1].strip()
        if len(row) != 2:
            print("errir, too many items")
            return
        if named_card["front"] == "front" and named_card["back"] == "back":
            print("please save")
            continue
        cards.append(named_card)
        print(f"{line} \n")
    fh.close()
    return cards

def play(cards):
    print("2 cool for skewl")

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



# runner


main()


# load_csv("paths.csv")
