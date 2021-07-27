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
Part 9: Start the play() fncn
Part 10: Go through each card in random order
Part 11: Test the User
Part 12: Scorekeeping
Part 13: Prettifying flashcards
    throughout your file
        [x] get rid of any debug print() statements
    at the top of the file
        [x] make a global variable WIDTH and set it to around 75
    in play
        [x] print a line to the beginning and end of each card
        [x] add some extra newlines around various elements
        [x] center any string by calling the .center() method 
        on it and pass the argument WIDTH. For example, the card["front"] line.
        [/] right align any string by calling the .rjust() method on it 
            and passing the argument WIDTH. For example, the card x of y line.
        [ ] print "score of total" after the end of each card
"""

# imports

from pathlib import Path
import random
from sys import stderr
import textwrap

# global variables

WIDTH = 75


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
            # print("please save")
            continue
        cards.append(named_card)
        # print(f"{line} \n")
    fh.close()
    return cards

def play(cards):
    """what is being done here is randomly drawing cards until the deck runs out"""
    score = 0
    total = len(cards)
    num = 1
    border = "=" * WIDTH
    
    while len(cards) > 0:
        # print(f"\n You so far have {score} out of a possible {total} \n")
        card = random.choice(cards)
        print("\n", border)
        print(card["front"].center(WIDTH), "\n")
        answer= input("\n What is the fncn to find this? \n")
        if answer == card["back"]:
            print("\n CORRECTAMUNDO \n")
            score += 1
        else:
            print("\n INCORRECTO \n")
            print("\n The answer is actually", card["back"], "\n")  

        cards.remove(card)
        print(f"Your score is {score} out of {num}")
        keep_going = input("\n Do you want to continue?\n")
        if keep_going.lower() != "yes":
            print("\n It's ok to be a quitter...sometimes...\n")
            return
        num += 1
        print(border, "\n")
    print(f"You have scored {score} out of {total} today. Good luck in the future")

def main():
    """this is the fncn to call the load_csv and play fncn"""
    # /Users/vision/code/project_outrun/data/flashcard_project/paths.csv
    path = Path("data") / "flashcard_project" / "paths.csv"

    cards = load_csv(path)
    if cards == False:
        return
        # else:
        #     print(cards)
    play(cards)

    
def new_file():
    path = Path("July26.py")
    print(f"We're creating the file {path} right now!")
    path.touch()


# runner


# main()

new_file()


# load_csv("paths.csv")
