"""This is CLI (command line interface) lesson set"""

# https://alissa-huskey.github.io/python-class/lessons/cli.html#glossary-CLI

"""Imports"""

import sys
import time

"""Global Variables"""



"""Fncns"""

def countdown():
    print("sys.argv:", sys.argv)
    if len(sys.argv) >= 2:
        count = int(sys.argv[1])
    else:
        count = 3

    print(f"counting down from {count}")    
    while count > 0:
        print(f"{count}...")
        time.sleep(1)
        count = count - 1

    if len(sys.argv) == 3:
        print(f"{sys.argv[2]}")
    else:
        print("we'll, ok. Guess we're done")






"""Runner"""

countdown()
