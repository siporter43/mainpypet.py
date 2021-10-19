"""This is our cool new project in which we'll create a text based adventure game :)
            https://alissa-huskey.github.io/python-class/exercises/adventure.html"""

"""
# Part 1.2
    # [x] Define a main() function, and have it print "Welcome!"
    # [x] In main() make a while loop with the condition True.
    # [x] In the loop, call the input() function, with the prompt "> ". 
    # Assign the returned value to the variable reply.
    # [x] Outside of main(): Use an if statement to check if __name__ == "__main__".
    # [x] In the if statement, call main()

Part 1.3
    A. Make do_quit()
        # [x] Make a do_quit() function.
        # [x] In it, print "Goodbye."
        # [x] Then call quit()

    B. In main(), in the while loop:
        [x] After getting reply, check if reply is equal to q or quit.
        [x] If so, call do_quit()
        [x] Otherwise, print a messsage like: "No such command." then continue
Part 1.5
    A. Define a do_shop() function
        [x]Define a do_shop() function.
        [x]Have it print "Items for sale."
        [x]Iterate over the ITEMS dictionary. Print the name and description of each.
    B. in main()
        [x]In between your if and else, add an elif clause that checks if reply is equal to shop.
        [x]If so, call do_shop()

Part 2.1
    A. Define do_go
        [x]Define a do_go() function that takes one argument: args.
        [x]In do_go() print Trying to go: args
    B. In main(), in the while loop
        [x]Strip the value returned from input() using the .strip() method.
            This means if a user enters " quit" or "quit " the program still knows to call do_quit().
        [x]Call .split() on reply and assign it to the variable args.
        [x]Now the args variable will contain a list where each word is an item in the list.
        [x]Use an if statement to check if args is falsy. If it is, continue.
        [x]This means that if a user doesn’t enter anything, the program will ignore it and start the loop over.
        [x]Remove the first item from args using the .pop() method and assign it to the variable command.
        [x]Now command will contain the first word the user entered, and args will contain a list of the remaining commands. 
            If there were no additional words, then args will be an empty list.
        [x]In each clause of the if statement where we check the value of reply, change it to command.
        [x]Add an elif clause that checks if command is equal to "g" or "go". If it is, call do_go() and pass args.

Part 2.2 Create PLAYER and PLACES
    A. At the top of your file
        [x]Create a PLAYER dictionary with the key "place" and the value "home".
    B. Create a PLACES dictionary where the key is a unique identifier for each place. 
        [x]The value is a dictionary that with information about each place:
            "key" – the same thing as the key
            "name" – a short description
            "description" – a longer description
            "east", "west", "north", "south" – the key to the place in that
        [x]Add two places, "home" and "town-square".
"""

"""Imports"""
from pprint import pprint

from pathlib import Path

"""Global Variables"""

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

}

PLAYER = {
    "place": "home"
}

PLACE = {
    "home": {
        "key": "home",
        "name": "Your Housey-House",
        "description": "A wondrous chateau filled with cool stuff",
        "east": "town-square",
    },
    "town-square": {
        "key": "town-square",
        "name": "Rad Center",
        "description": "A wretched hive of scum and villainy... and commerce",
        "west": "home",
    }
}
"""FNCNs"""

def debug(message):
    if DEBUG == True:
        print(f"DEBUG:{message}")

def do_shop():
    print("Items for Sale:")
    for item in ITEMS.values():
        print(f'Name:{item["name"]} \n Desc.: {item["description"]} \n Cost: {item["price"]}')

def do_go(args):
    print(f"Trying to go: {args}")


def main():
    print("Welcome to the Adventure of a Slight-time!")
    while True:
        reply = input(">").strip(" ")
        cancel = ["Quit", "quit", "q"]
        shop = ["shop", "Shop", "s"]
        go = ["g", "go", "Go"]
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
        else:
            print("No Such Command")
            continue
    else:
        do_quit()
    


def check_main():
    if __name__ == "__main__": 
        main()


def do_quit():
    print("Goodbye, nerd")
    quit()

def new_file():
    path = Path("Strings_Oct18.py")
    print(f"Now creating {path} for our new lesson")
    path.touch()

"""Runner"""

# main()

# check_main()

# do_shop()
new_file()
