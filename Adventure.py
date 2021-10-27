"""This is our cool new project in which we'll create a text based adventure game :)
            https://alissa-huskey.github.io/python-class/exercises/adventure.html"""


# # Part 1.2
#     # [x] Define a main() function, and have it print "Welcome!"
#     # [x] In main() make a while loop with the condition True.
#     # [x] In the loop, call the input() function, with the prompt "> ". 
#     # Assign the returned value to the variable reply.
#     # [x] Outside of main(): Use an if statement to check if __name__ == "__main__".
#     # [x] In the if statement, call main()

# Part 1.3
#     A. Make do_quit()
#         # [x] Make a do_quit() function.
#         # [x] In it, print "Goodbye."
#         # [x] Then call quit()

#     B. In main(), in the while loop:
#         [x] After getting reply, check if reply is equal to q or quit.
#         [x] If so, call do_quit()
#         [x] Otherwise, print a messsage like: "No such command." then continue
# Part 1.5
#     A. Define a do_shop() function
#         [x]Define a do_shop() function.
#         [x]Have it print "Items for sale."
#         [x]Iterate over the ITEMS dictionary. Print the name and description of each.
#     B. in main()
#         [x]In between your if and else, add an elif clause that checks if reply is equal to shop.
#         [x]If so, call do_shop()

# Part 2.1
#     A. Define do_go
#         [x]Define a do_go() function that takes one argument: args.
#         [x]In do_go() print Trying to go: args
#     B. In main(), in the while loop
#         [x]Strip the value returned from input() using the .strip() method.
#             This means if a user enters " quit" or "quit " the program still knows to call do_quit().
#         [x]Call .split() on reply and assign it to the variable args.
#         [x]Now the args variable will contain a list where each word is an item in the list.
#         [x]Use an if statement to check if args is falsy. If it is, continue.
#         [x]This means that if a user doesn’t enter anything, the program will ignore it and start the loop over.
#         [x]Remove the first item from args using the .pop() method and assign it to the variable command.
#         [x]Now command will contain the first word the user entered, and args will contain a list of the remaining commands. 
#             If there were no additional words, then args will be an empty list.
#         [x]In each clause of the if statement where we check the value of reply, change it to command.
#         [x]Add an elif clause that checks if command is equal to "g" or "go". If it is, call do_go() and pass args.

# Part 2.2 Create PLAYER and PLACES
#     A. At the top of your file
#         [x]Create a PLAYER dictionary with the key "place" and the value "home".
#     B. Create a PLACES dictionary where the key is a unique identifier for each place. 
#         [x]The value is a dictionary that with information about each place:
#             "key" – the same thing as the key
#             "name" – a short description
#             "description" – a longer description
#             "east", "west", "north", "south" – the key to the place in that
#         [x]Add two places, "home" and "town-square".

# Part 2.3 Write user message fncns
    # A. At the top of the file
        # [x] Import stderr from the sys module
        # [x] Add a global variable DEBUG and set it to True
    # B. Define debug() function
        # [x] Write a function named: debug with one parameter: message
        # [x] In the function, check if DEBUG is True (or truthy)
        # [x] If so, then print message
    # [x] Bonus: Print something before it like "DEBUG: ", or "# ", 
    #           so you can more easily tell that it is a debug message
    # C. define error() function
        # [x] Write a function named: error with one parameter: message
        # [?] Print message with something before it like "Error: ". 
            # Send the keyword argument file with the value stderr to print it to stderr. 
            # See CLI Lesson for more information.
    # D. in do_go()
        # [x] Call debug() instead of print() for the message Trying to go: args
    # E. in main(), in the while loop
        # [x] At the beginning of the while loop call debug() with the message 
            # You are at: PLACE. Replace PLACE with the value in the PLAYER dictionary 
            # associated with the "place" key
            # This will print a debug message with your current location 
            # every time the loop runs.
        # [x] After assigning command, use debug() to print command and args.
        # [x] Call error() instead of print() for the message No such command.
    # F. Test debug messages
        #  [x] Test with DEBUG set to True as well as with DEBUG set to False
# 2.4 Fill in the GO
    # A. in do_go(): ensure that the user typed a valid direction
        # In this section we’ll be making sure there is at least one item in the args list 
        #   and that it is a valid direction.
        # [x] Check to see if args is falsy, if so:
            # [x] Use the error() function to print a message saying: "Which way do you want to go?"
            # [x] return
    # [x] assign the first item of the args list to the variable direction and make it lowercase
    # [x] Check if direction is one of "north", "south", "east", "west". If not:
    # [x] Use the error() function to print a message saying: "Sorry, I don't know how to go: direction.")
    #   [x] return
    # B. (still) in do_go(): look up where the user is at
        # In this section we’ll be using the PLAYER["place"] to get the current place 
        #   from the PLACES dictionary, as shown here.
        # [x] get the value from PLAYER associated with the "place" key and assign it to old_name
        # [x] get the value from PLACES associated with old_name and assign it to old_place
    # C. (still) in do_go(): look up what is in that direction from here
        # In this section we’ll use the direction (ie. "east") the player wants to go 
        #   to look up the name of the next place (if any) in the current place dictionary as seen here.
        # [x] use the .get() method on old_place to get the value associated with the direction key and 
        #       assign it to new_name
        # [x] Check if new_name is falsy. If so:
            # [] Use the error() function to print a message saying: "Sorry, you can't go direction from here.")
            # [ ] return
    # D. (still) in do_go(): figure out where we’re going
        # Next we’ll look up the new place name from the current place dictionary 
            # using the direction (ie. "east") to as a key. 
            # If it’s missing, that means the player can’t go that direction from where they are.
        # [ ] use the .get() method on PLACES to get the value associated 
        #   with the new_name key and assign it to new_place
        # [ ] Check if new_place is falsy. If so:
            # [ ] Use the error() function to print a message saying: "Woops! 
            #   The information about {new_name} seems to be missing."
        # This will only happen if you made a mistake somewhere in your code. But just in case we do, 
        # we want to have a clear error message so we can tell what went wrong.
        # [ ] return
    # E. (still) in do_go(): update the players place and describe it
        # Finally, we can now update the PLAYER dictionary to point to the new place name and print the place information.
        # [ ] In the PLAYER dictionary change value associated with the "player" key to new_name
        # [ ] Print the values associated with the "name" and "description" keys of the new_place dictionary

# Imports

from os import error

from pprint import pprint

from pathlib import Path

from sys import stderr

from console import fg, bg, fx


# Global Variables

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

PLACES = {
    "home": {
        "key": "home",
        "name": "Your Housey-House",
        "description": "A wondrous chateau filled with cool stuff",
        "east": "town-square",
        "north": "well"
    },
    "town-square": {
        "key": "town-square",
        "name": "Rad Center",
        "description": "A wretched hive of scum and villainy... and commerce",
        "west": "home",
        "south": "cove"
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
        "north": "town-square"
    }
}
# FNCNs

def debug(message):
    if DEBUG == True:
        print(fx.dim(f"DEBUG:{message}"))

def error(message):
    print(bg.red(f"ERROR: {message}"))

def do_shop():
    print("Items for Sale:")
    for item in ITEMS.values():
        print(f'Name:{item["name"]} \n Desc.: {item["description"]} \n Cost: {item["price"]}')

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


def main():
    print("Welcome to the Adventure of a Slight-time!")
    while True:
        debug(f'You are at:{PLAYER["place"]}')
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
            error("No Such Command")
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

# Runner

main()

# check_main()

# do_shop()
