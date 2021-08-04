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
Part 14: Wrap long questions
Part 15: Add topics menu
    at the top of your file
        [ ]Make a list assigned to the global variable TOPICS
    menu()
        [x]write a menu() function
        [x]assign TOPICS to a list of Path objects in your flashcards directory 
        using the .iterdir() method
        [x]print an error message if no files are found in your flashcards directory
        [x]print the filename minus the .csv extension for each Path object 
        in the TOPICS list, next to a number
        [x]print a special option "all" with a menu selection of 0
        [x]make a list assigned to the variable selection
        [x]get input from the user asking them to choose one or more topics 
        and assign it to a variable choices
        [x]use the .split() method to split choices into multiple items on whitespace
        [x]iterate over each response and assign to choice:
            [x]if the response is "0", return TOPICS
            [x]convert choice to an int and subtract 1
            [x]get the item from TOPICS at the choice index and append it to selection list
        [x]return the selection list
    in main()
        [ ]at the beginning of the function, make an empty cards list
        [ ]call menu() and assign the returned value to the variable paths
        [ ]remove the line where you previously defined the path to your .csv file
        [ ]iterate over paths and assign each element to the variable path:
            [ ]call load_csv() with the path argument
            [ ]append the returned value to cards using the .extend() method
"""

# imports

from pathlib import Path
import random
from sys import stderr
import textwrap

# global variables

WIDTH = 75
MAXWIDTH = 60

TOPICS = list

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


def menu():
    """the plan is to add a menu to pick a particular set to use"""
    path = Path("data")/"flashcard_project"
    TOPICS = list(path.iterdir())
    """I want to make an if statement to give an error if there are no files in directory"""
    if not TOPICS:
        print("No files in this directory, bro-ski")
    """now need to do enumerate Stem filenames"""
    for i, item in enumerate(TOPICS):
        print(i+1, item.stem)
    """Now create a special opt for 'all' with menu=0"""
    print(0,"All")
    selection = []
    """get input from user to choose one or more topics assign to var choices"""
    choices = input("What topic would you like to work with today? ")
    for choice in choices.split():
        if choice == "0":
            return TOPICS
        choice = int(choice) -1 
        selection.append(TOPICS[choice])
    return selection


 





def play(cards):
    """what is being done here is randomly drawing cards until the deck runs out"""
    score = 0
    total = len(cards)
    num = 1
    border = "=" * WIDTH
    
    while len(cards) > 0:
        # print(f"\n You so far have {score} out of a possible {total} \n")
        card = random.choice(cards)
        lines = textwrap.wrap(card["front"])
        print("\n", border)
        for front_line in lines:
            print(f"\n {front_line} \n")
        # print(f"\n{lines} \n")
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
    path = Path("Aug2.py")
    print(f"We're creating the file {path} right now!")
    path.touch()


# runner
print(menu())

# main()

# new_file()


# load_csv("paths.csv")
