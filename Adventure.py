"""This is our cool new project in which we'll create a text based adventure game :)
            https://alissa-huskey.github.io/python-class/exercises/adventure.html"""


# [x]     2.4 Fill in the GO
# [x] Part 3: Prettify
# [x]     3.1 Text Wrapping
# [x]     3.2 Colors
# [x]     3.3: Headers and write fncns
# [x] Part 4: Examine Items 
#     [x] 4.1 Add New Items
#     [x] 4.2 Add do_examine()
#     [x] 4.3 Finish Examine Command
# [] Part 5: Look Around
#     [x] 5.1: Add Command
    #       A: Define a do_look() function
    #           [x] Define a do_look() function.
    #           [x] In it, use the debug() function to print something like "Trying to look around.".
    #       B: in main(), in the while loop
    #           [x] Add an elif that checks if command is "l" or "look".
    #           [x] if so, call do_look()
#    [x] 5.2: Print place name and desc.
#           A: In do_look(): look up and print the current place
#    [] 5.3: Print the place items
            # A: At the end of do_look
#                 [ ] Using the .get() method, get the value from place associated with the items dictionary. Use a default value of [] and assign it to the variable items.

                # [ ] If items is truthy:

                # [ ] Make an empty list assigned to the variable names

                # [ ] Iterate over the items list using the variable name key for each item. For each item:

                # [ ] Get the value from ITEMS associated with the key key and assign it to the variable item

                # [ ] Append the value associated with the "name" key from the items dictionary to the names list


# Imports

from os import error

from pprint import pprint

from pathlib import Path

from sys import stderr

from console import fg, bg, fx

import textwrap


# Global Variables

WIDTH = 60

MARGIN = 4

DEBUG = True

ITEMS = {
    "elixir": {
        "key": "elixir",
        "name": "Booze of healing",
        "description": "Some medicine mixed with everclear for taste",
        "price": -10,
    },
    "club": {
        "key": "club",
        "name": "Club",
        "description": "A big piece of something you can hit anyone with",
        "price": -20,
    },
    "flute": {
        "key": "flute",
        "name": "Flute of Viscious Whimsy",
        "description": "An Instrument for Melody and Murder",
        "price": -15
    },
    "poison": {
        "key": "poison",
        "name": "Actual Poison",
        "description": "It's poison. Don't buy this",
        "price": -10
    },
    "book": {
        "key": "book",
        "name": "Books of Mild Secrets",
        "description": "It's a pleather-bound book of pages from sages",
        "price": ""
    },
    "desk": {
        "key": "desk",
        "name": "The Resolute Desk",
        "description": "A heavy wooden desk with a clever book open on its surface",
        "price": ""
    }
}

PLAYER = {
    "place": "home"
}

#  MAP of PLACES:
#  
#               well  ---   market
#                |            |
#               home -- town square
#                           |
#                           cove
# 


PLACES = {
    "home": {
        "key": "home",
        "name": "Your Housey-House",
        "description": "A wondrous chateau filled with cool stuff",
        "east": "town square",
        "north": "well",
        "items": ["book", "desk"],
    },
    "town square": {
        "key": "town square",
        "name": "Rad Center",
        "description": "A wretched hive of scum and villainy... and commerce",
        "west": "home",
        "north": "market",
        "south": "cove",
    },
    "market": {
        "key": "market",
        "name": "Magique Market",
        "description": "It's the place to buy the things",
        "west": "well",
        "south": "town square",
        "items": ["elixir", "club", "flute", "poison"]
    },
    "well":{
        "key": "well",
        "name": "The Well Well",
        "description": "A Well Well full of Magic and Intrigue",
        "south": "home",
        "east": "market"
    },
    "cove":{
        "key": "cove",
        "name": "Ducky Cover",
        "description": "A cove full of ducks of all shapes and sizes...and tempers",
        "north": "town square"
    }
}
# FNCNs

def debug(message):
    if DEBUG == True:
        print(fg.green(bg.black(f"DEBUG:{message}")))

def error(message):
    print(bg.red(f"ERROR: {message}"))

def wrap(text):
    margin = MARGIN * " "
    paragraph = textwrap.fill(text, WIDTH, initial_indent= margin, subsequent_indent= margin)
    print(paragraph)

def write(text):
    print(MARGIN * " ", text, sep="")

def header(title):
    print()
    real_title = fg.lightblack(fx.bold(title))
    write(real_title)
    print()

def do_examine(args):
    place_name = PLAYER["place"]
    place = PLACES[place_name]
    debug(f"Trying to examine: {args}")
    if not args:
        error("What do you want to examine?")
        return
    name = args[0].lower()
    items = place.get("items", [])
    if name not in items:
        error(f"Sorry, idk what this is: {name}")
        return
    if name not in ITEMS:
        error(f"Welp! The info about {name} isn't here, my dear.")
        return
    item = ITEMS[name]
    header(item["name"])
    wrap(item["description"])

def do_look():
    place_name = PLAYER["place"]
    place = PLACES[place_name]
    header(place["name"])
    wrap(place_name["description"])
    debug("Trying to look around...")


def do_shop():
    header("Items for Sale:")
    for item in ITEMS.values():
        if not item["price"]:
            continue
        write(f'Name:{item["name"]} \n Desc.: {item["description"]} \n Cost: {item["price"]}')

def do_go(args):
    debug(f"Trying to go: {args}")
    compass = ["north", "south", "east", "west"]
    old_name = PLAYER["place"]
    old_place = PLACES[old_name]
    if not args:
        error(fg.cyan(f"Which way does your heart guide you?"))
        return
    direction = args[0].lower()
    if direction not in compass:
        error(f"Sorry, you're wrong. I have no idea how to go {direction} from here.")
        return
    new_name = old_place.get(direction)
    if not new_name:
        error(fx.frame("Sorry, you can't get there from here"))
        return
    new_place = PLACES.get(new_name)
    if not new_place:
        error(f"OOOPS, The info about {fg.lightpurple({new_name})} seems missing")
        return
    PLAYER["place"] = new_name
    wrap(fx.bold(new_place["name"])) 
    wrap(fx.encircle(new_place["description"]))



def main():
    print("Welcome to the Adventure of a Slight-time!")
    while True:
        debug(f'You are at:{PLAYER["place"]}')
        reply = input(fg.yellow(">")).strip(" ")
        cancel = ["Quit", "quit", "q"]
        shop = ["shop", "Shop", "s"]
        go = ["g", "go", "Go"]
        examine = ["x", "exam", "examine", "Examine"]
        look = ["l", "Look", "look"]
        args = reply.split()
        if not args:
            continue
        command = args.pop(0)
        debug(f"Command is {command}")
        debug(f"Args is {args}")
        if command in cancel:
            do_quit()
        elif command in shop:
            do_shop()
        elif command in go:
            do_go(args)
        elif command in examine:
            do_examine(args)
        elif command in look:
            do_look()
        else:
            error("No Such Command")
            continue
    else:
        do_quit()
    


def check_main():
    if __name__ == "__main__": 
        main()


def do_quit():
    write(bg.lightmagenta("Goodbye, nerd"))
    quit()

def new_file():
    path = Path("Strings_Nov29.py")
    print(f"Now creating {path} for our new lesson")
    path.touch()

# Runner

main()

# do_examine(["cat"])

# check_main()

# do_shop()

# new_file()

