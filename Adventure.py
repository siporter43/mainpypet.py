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
        []In between your if and else, add an elif clause that checks if reply is equal to shop.
        []If so, call do_shop()
"""

"""Imports"""
from pprint import pprint


"""Global Variables"""

DEBUG = True

ITEMS = {
    "elixir": {
        "key": "elixir",
        "name": "booze of healing",
        "description": "some medicine mixed with everclear for taste",
        "price": -10,
    },
    "club": {
        "key": "club",
        "name": "Club",
        "description": "a big piece of something you can hit anyone with",
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
        "name": "poison",
        "description": "It's poison. Don't buy this",
        "price": -10
    },

}
"""FNCNs"""

def debug(message):
    if DEBUG == True:
        print(f"DEBUG:{message}")

def do_shop():
    print("Items for Sale:")
    for item in ITEMS.values():
        print(f'Name:{item["name"]} \n Desc.: {item["description"]} \n Cost: {item["price"]}')



def main():
    print("Welcome!")
    while True:
        reply = input(">")
        cancel = ["Quit", "quit", "q"]
        if reply in cancel:
            do_quit()
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



"""Runner"""

# main()

# check_main()

do_shop()
