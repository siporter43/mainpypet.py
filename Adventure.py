"""This is our cool new project in which we'll create a text based adventure game :) https://alissa-huskey.github.io/python-class/exercises/adventure.html"""

# Imports

from bdb import Breakpoint
from email import message
from os import error, name

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
        "price": -15,
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

def debug(message: str):
    """Print a debug message when in debug mode."""
    if DEBUG == True:
        print(fg.green(bg.black(f"DEBUG:{message}")))

def error(message: str):
    """Print a formatted error message."""
    print(bg.red(f"ERROR: {message}"))

def abort(message: str):
    """Print a formatted error message then exit the game."""
    error(message)
    exit(1)

def wrap(text):
    """"Prints standard format for text"""
    margin = MARGIN * " "
    paragraph = textwrap.fill(text, WIDTH, initial_indent= margin, subsequent_indent= margin)
    print(f"{paragraph} \n")

def write(text):
    """Prints text standard with margins"""
    print(MARGIN * " ", text, sep="")

def header(title):
    print()
    real_title = fg.lightblack(fx.bold(title))
    write(real_title)
    print()

def get_item(key: str) -> dict:
    """Return the item dictionary from ITEMS associated with key.

       If key is missing, abort.
       
       Args
       ----
       * key: the key to the item in the ITEMS dictionary
    """
    item = ITEMS.get(key)
    if not item:
        abort(f"Welp-O! Looks like info about item {name} is missing")
    return item

def player_has(key: str) -> bool:
    """ Checks whether an item exists in current player inventory.
    
    Args
    ----
    * key: the key is in PLAYER: inventory dict
    """
    if PLAYER["inventory"].get(key, 0) > 0:
        return True
    else:
        return False

def current_place_has(key: str) -> bool:
    """Checks whether an item is in current place. 

    Args
    ----
    * key: the key is in PLACES dict
    """
    place = get_place()
    if key not in place.get("items", []):
        return False
    else:
        return True


def place_remove(key: str):
    """This will remove an item from a PLACE's item list.
    
    Args
    ----
    * key: the key is the name of the item (hopefully in the list)
    """
    # We're getting current place
    place = get_place()
    
    # If key is in place then we remove it
    if "items" not in place:
        # place["items"] = []
        return

    if key in place['items']:
        place["items"].remove(key)



def is_for_sale(key: str) -> bool:
    """Check whether an item in a dictionary has a price key.

    If no key, return False.

    Args
    ----
    * key: key is in ITEMS dict
    """
    item = ITEMS.get(key)
    sale_price = item.get("price")
    if sale_price:
        return True
    else:
        return False

def inventory_change(key, quantity):
    """Run to change quantity of item in inventory
    
    If no key, message error asking for item name

    If no quatity, return error 

    Args
    ----
    key: any string
    quantity: numbers excluding 0, incl negatives
    """
    # PLAYER["inventory"].setdefault(key, 0) # NOTE: same as below
    if key not in PLAYER["inventory"]:
        PLAYER["inventory"][key] = 0

    PLAYER["inventory"][key] = (PLAYER["inventory"][key] + quantity)

    # need to set it up such that anytime a quantity hits 0 that it .pop the item
    if PLAYER["inventory"][key] <= 0:
       PLAYER["inventory"].pop(key)

def place_add(key: str):
    """This moves an item into the 'items' of current place
    
    Args
    ----
    * key: any string
    """
    # We're getting the current Player place ->a dict
    place = get_place()
    
    # We're now creating an 'items' list for that dict if one doesn't exist
    place.setdefault("items", [])
    
    # We're checking if key is in 'items' list, if it is then return,
    #  if not then add list to place
    if key not in place["items"]:
        place["items"].append(key)

def do_examine(args: list) -> "None":
    """Run for the examine command and lets user get further info on item in location/
    inventory 
    
    Args
    ----
    * args: list of strings
    """
    debug(f"Trying to examine: {args}")
    if not args:
        error("What do you want to examine?")
        return
    name = args[0].lower()
    if not current_place_has(name) and not player_has(name):
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

def do_take(args: list):
    """Runs relative to take cmd to take an item from a 
    location if it is there/can be taken and place in PLAYER inventory 

    If no arg, then print error

    If item info missing, abort

    If cannot take, tell user No

    Args
    ----
    * args: list of strings 
    """
    place = get_place()
    if not args:
        error("Which way do you want to go with all this?")
        return
    name = args[0].lower()
    item = ITEMS.get(name)
    debug(f"Trying to take: {name}")
    if not current_place_has(name):
        error(f"I don't see {name} here, you fool of a Took!")
        return
    if not item:
        abort(f"Welp! The info about {name} is missing or something...")
    if not item.get("can_take", []):
        wrap(f"You try to pick up {item['name']}, but you are a puny mortal with no muscles")
        return
    # rn we're gonna change some stuff to 
    # PLAYER["inventory"][name] = PLAYER["inventory"][name] + 1
    inventory_change(name, 1)
    # place["items"].remove(name)
    place_remove(name)
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
    # breakpoint()
    debug(f"Trying to drop {args}")
    if not args:
        error("What you wanna drop?")
        return
    name = args[0].lower()
    if not player_has(name):
        error(f"You don't have any {name}.")
        return
    # rn we're gonna replace below with inventory_change fncn
    # PLAYER["inventory"][name] -= 1
    # if not PLAYER["inventory"][name]:
    #    PLAYER["inventory"].pop(name)
    inventory_change(name, -1)
    # place = get_place()
    # place.setdefault(name, [])
    # place["items"].append(name)
    place_add(name)
    wrap(f"You gently toss {name} on the ground.")
    

def do_shop():
    header("Items for Sale:")
    for item in ITEMS.values():
        if not item["price"]:
            continue
        write(f'Name:{item["name"]} \n Desc.: {item["description"]} \n Cost: {item["price"]}')

def get_place(key: str=None) -> dict:
    """"It returns the dictionary info for a place from PLACES dict using the key
        key defaults to wherever current Player location"""
    if not key:
        key = PLAYER["place"]
    place = PLACES.get(key)
    if place == None:
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

# NOTE: make this a seperate script sometime
def new_file():
    path = Path("may2.py")
    print(f"Now creating {path} for our new lesson")
    path.touch()


# Runner
if __name__ == "__main__":
    main()

