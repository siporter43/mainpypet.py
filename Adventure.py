"""This is our cool new project in which we'll create a text based adventure game :)
            https://alissa-huskey.github.io/python-class/exercises/adventure.html"""

"""Either write place_has() use TDD or use player_has()"""
# [x]     2.4 Fill in the GO
# [x] Part 3: Prettify
# [x]     3.1 Text Wrapping
# [x]     3.2 Colors
# [x]     3.3: Headers and write fncns
# [x] Part 4: Examine Items 
#     [x] 4.1 Add New Items
#     [x] 4.2 Add do_examine()
#     [x] 4.3 Finish Examine Command
# [x] Part 5: Look Around
#    [x] 5.1: Add Command
#    [x] 5.2: Print place name and desc.
#    [x] 5.3: Print the place items
#    [x] 5.4: Print the nearby places
# [x] Part 6: Take Things
#       [x] 6.1: Add Command
#       [x] 6.2: Validate Item
#       [x] 6.3: Take it
#       [x] 6.4: Examine Inventory
# [x] Part 7: Show Inventory
    # [x] 7.1: Add command
    # [x] 7.2: Print Inventory
# [x]Part 8: Drop things
    #[x] 8.1: Add Command
    #[x] 8.2: Validate
    #[x] 8.3: Drop it
# [] Part 9: Refactoring
    # [x] 9.1: Add abort()
    # [x] 9.2: Add get_place()
    # []  9.3: Add get_item()
        # [x] A. Define get_item()
            # [x] define a get_item() function that takes one argument key
            # [x] use the .get() method on the ITEMS dictionary to get the value assocated from the key key and assign it to the variable item
            # [x] If item is falsy,
            # [x] Use the abort() function to print an error message like:
            # "Woops! The information about the item name seems to be missing."
            # [x] return item

#  [] Part 11: Test Things
        #[x] 11.1 Setup
        # [] 11.2 Test is_for_sale
        # [] 11.3 Test Error
        #   [] A. Write test_error()
        #        [?] Add error to your import line, something like: from adventure import is_for_sale, error.
#                [x] Add a test_error() function with the parameter capsys.
                # [x] Call error() with any message you like
                # [x] Assign the results of capsys.readouterr().out to the variable output
                # [x] Write an assert statement that output equals what you expect to be printed, 
                #     with a failure message like:
                # [ ] Run your tests, either at the command line or in VS Code.
                #     "The formatted error message should be printed."

# Imports

from ast import Assert, Pass
from email.policy import default
from inspect import ArgSpec

from os import error, name

from pprint import pprint

from pathlib import Path

from sys import stderr

from tkinter.messagebox import ABORT

from console import fg, bg, fx

import textwrap

from pytest import Item
from requests import get


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
        "price": -10,
    },
    "book": {
        "key": "book",
        "name": "The Book of Mild Secrets",
        "description": "It's a pleather-bound book of pages from sages",
        "price": "",
        "can_take": True
    },
    "desk": {
        "key": "desk",
        "name": "The Resolute Desk",
        "description": "A heavy wooden desk with a clever book open on its surface",
        "price": "",
        "can_take": False
    },
    "dogs": {
        "key": "dogs",
        "name": "little pupperonis",
        "description": "The cutest little things",
        "price": "",
        "can_take": False
    },
    "snack":{
        "key": "snack",
        "name": "secret electro-ice cream",
        "description": "The ice cream that makes you good at coding instead of giving brain freezes",
        "price": "",
        "can_take": True
    },
    "bones":{
        "key": "bones",
        "name": "The Bones of her enemies",
        "description": "This is what happens when you don't commit...you get pushed INTO HELL!",
        "price": "",
        "can_take": False
    }
}

PLAYER = {
    "place": "home",
    "inventory": {}
}

#  MAP of PLACES:
#  
#               well  ---   market
#                |            |
#               home -- town square
#                           |
#                           cove -- Alissa
# 


PLACES = {
    "home": {
        "key": "home",
        "name": "Your Housey-House",
        "description": "A wondrous chateau filled with cool stuff",
        "east": "town square",
        "north": "well",
        "items": ["desk", "book"],
    },
    "town square": {
        "key": "town square",
        "name": "Rad Center",
        "description": "A wretched hive of scum and villainy... and commerce",
        "west": "home",
        "north": "market",
        "south": "cove",
        "items": []
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
        "east": "market",
        "items": []
    },
    "cove":{
        "key": "cove",
        "name": "Ducky Cover",
        "description": "A cove full of ducks of all shapes and sizes...and tempers",
        "north": "town square",
        "east": "Alissa",
        "items": []
    },
    "Alissa":{
        "key": "Alissa",
        "name": "The Robo-Home of the Beep Boop Queen",
        "description": "The cybernetic lair of the Alissa person, may have food.",
        "west": "cove",
        "items": ["snack", "dogs", "bones"]
    }
}
# FNCNs

def debug(message):
    if DEBUG == True:
        print(fg.green(bg.black(f"DEBUG:{message}")))

def error(message):
    print(bg.red(f"ERROR: {message}"))

def abort(message):
    error(message)
    exit(1)

def wrap(text):
    margin = MARGIN * " "
    paragraph = textwrap.fill(text, WIDTH, initial_indent= margin, subsequent_indent= margin)
    print(f"{paragraph} \n")

def write(text):
    print(MARGIN * " ", text, sep="")

def header(title):
    print()
    real_title = fg.lightblack(fx.bold(title))
    write(real_title)
    print()

def get_item(key):
    item = ITEMS.get(key)
    if not item:
        abort(f"Welp-O! Looks like info about item {name} is missing")
    return item

def player_has(key):
    if PLAYER["inventory"].get(key, 0) > 0:
        return True
    else:
        return False



def do_examine(args):
    place = get_place()
    debug(f"Trying to examine: {args}")
    if not args:
        error("What do you want to examine?")
        return
    name = args[0].lower()
    items = place.get("items", [])
    if name not in items and name not in PLAYER["inventory"]:
        error(f"Sorry, idk what this is: {name}")
        return
    if name not in ITEMS:
        abort(f"Welp! The info about {name} isn't here, my dear.")
    item = ITEMS[name]
    header(item["name"])
    wrap(item["description"])

def do_look():
    place = get_place()
    header(place["name"])
    wrap(place["description"])
    debug("Trying to look around...")
    items = place.get("items", [])
    names = []
    if items:
        for key in items:
            item = ITEMS.get(key)
            names.append(item["name"])
        last = names.pop()
        text = ", ".join(names)
        if text:
            text += " and "
        text += last
        print()
        write(f"You see {text}.\n")
    debug(names)        
    for direction in ["north", "south", "east", "west"]:
        name = place.get(direction)
        if not name:
            continue
        destination = get_place(name)
        write(f"\n To the {direction} is: {destination['name']}. \n")

def do_take(args):
    place = get_place()
    if not args:
        error("Which way do you want to go with all this?")
        return
    name = args[0].lower()
    item = ITEMS.get(name)
    debug(f"Trying to take: {name}")
    if name not in place.get("items", []):
        error(f"I don't see {name} here, you fool of a Took!")
        return
    if not item:
        abort(f"Welp! The info about {name} is missing or something...")
    if not item.get("can_take", []):
        wrap(f"You try to pick up {item['name']}, but you are a puny mortal with no muscles")
        return
    PLAYER["inventory"].setdefault(name, 0)
    PLAYER["inventory"][name] = PLAYER["inventory"][name] + 1
    place["items"].remove(name)
    wrap(f"You pick up the {item['name']} and put it in your backy-pack")


def do_inventory():
    debug(f"Trying to show inventory")
    header("Inventory")
    stuff = PLAYER["inventory"]
    if not stuff:
        write("Empty")
        return
    for thing, qty in stuff.items():
        print(f"You find {qty} {thing} \n")
    
def do_drop(args):
    debug(f"Trying to drop {args}")
    if not args:
        error("What you wanna drop?")
        return
    name = args[0].lower()
    if name not in PLAYER["inventory"] or PLAYER["inventory"][name] < 1:
        error(f"You don't have any {name}.")
        return
    PLAYER["inventory"][name] -= 1
    if not PLAYER["inventory"][name]:
       PLAYER["inventory"].pop(name)
    place = get_place()
    place.setdefault(name, [])
    place["items"].append(name)
    wrap(f"You gently toss {name} on the ground.")
    

def do_shop():
    header("Items for Sale:")
    for item in ITEMS.values():
        if not item["price"]:
            continue
        write(f'Name:{item["name"]} \n Desc.: {item["description"]} \n Cost: {item["price"]}')

def get_place(key=None):
    if not key:
        key = PLAYER["place"]
    place = PLACES[key]
    if not place:
        abort(f"Well ya got me stumped. Info about {name} ain't here, bucko.")    
    return place

# get_place()            # key = None
# get_place("somewhere") # key = "somewhere"

def do_go(args):
    debug(f"Trying to go: {args}")
    compass = ["north", "south", "east", "west"]
    old_place = get_place()
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
    new_place = get_place(new_name)
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
        take = ["t", "take", "grab"]
        args = reply.split()
        inventory = ["i", "inventory", "I", "inven"]
        drop = ["D", "d", "Drop", "drop"]
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
        elif command in take:
            do_take(args)
        elif command in inventory:
            do_inventory()
        elif command in drop:
            do_drop(args)
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
    path = Path("may2.py")
    print(f"Now creating {path} for our new lesson")
    path.touch()


# Runner

# main()

# do_examine(["cat"])

# check_main()

# do_shop()

new_file()

