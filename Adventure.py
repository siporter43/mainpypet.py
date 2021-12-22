"""This is our cool new project in which we'll create a text based adventure game :)
            https://alissa-huskey.github.io/python-class/exercises/adventure.html"""


# [x]     2.4 Fill in the GO
# [x] Part 3: Prettify
# [x]     3.1 Text Wrapping
# [x]     3.2 Colors
# [x]     3.3: Headers and write fncns
# [ ] Part 4: Examine Items 
#     [x] 4.1 Add New Items 
#             [x] A. In ITEMS:
#                 [x] Add two items to the ITEMS dictionary with keys: "desk" and "book". Like previous items, 
#                     each element one should be a dictionary with a "name" and "description"; unlike the others, these will have no "price".
#             [x] B. In do_shop(), in the for loop:
#                    [x] Before printing each item, check if the item has a "price" key. continue if not.
#     [x] 4.2 Add do_examine()
#             [x] A. Make do_examine():
#                 [x] Add a function do_examine() with one parameter: args.
#                 [x] Use the debug() function to print the value of args, something like:
#                     Trying to examine: args
#             [x] B. In main(), in the while loop:
#                [x] Add an elif clause that checks if command is "x", "exam", or "examine".
#           If it is, call do_examine() and pass args.
#      [ ] 4.3 Finish Examine Command
#              [x] A. In do_examine() ensure args is not empty
#                 [x] Check to see if args is falsy, if so:
#                 [x] Use the error() function to print a message saying: "What do you want to examine?"
#                 [x] return
#              [x] B. Still in do_examine(): get the current place
#                     [x] get the value from PLAYER associated with the "place"
#                         key and assign it to place_name
#                     [x] get the value from PLACES associated with place_name
#                         and assign it to place
#              [x] C. Still in do_examine(): check the name
#                     [x] assign the first element from the args list to the
#                         variable name and make it lowercase
#                     [x] check if name is in the items list by:
#                     [x] use an if statement with the condition:
#                         [x] check if name is not in the list returned by .get()
#                         [x] use the .get() method on place to get the "items"
#                             list and pass
#                         [x] if the above condition is met:
#                             [x] print an error message like: "Sorry, I don't
#                                 know what this is: name."
#                             [x] return
#                     [ ] Check if name is a key in the ITEMS dictionary, if not:
#                         [ ] Print an error message like:
#                                 "Woops! The information about name seems to be missing."
#                             This will only happen if you made a mistake somewhere in your code. But just in case we do, 
#                             we want to have a clear error message so we can tell what went wrong.
#              [ ] D. Still in do_examine(): get and print the item info
#                     [ ] Get the value from the ITEMS dictionary associated with the 
#                         name key and assign it to the variable item
#                     [ ] Using the header() funciton print the item name
#                     [ ] Using the wrap() function print the item description



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
#               well
#                |
#               home  -- town square
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
        "south": "cove",
    },
    "well":{
        "key": "well",
        "name": "The Well Well",
        "description": "A Well Well full of Magic and Intrigue",
        "south": "home"
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
    debug("Hello Alissa-Monster. AHHHHHHHHHH")

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

