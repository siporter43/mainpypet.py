#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Dragon Realm - A game of chance and skill where the player decides between 2 caves, 
    holding either treasure or DOOM.
"""

# Imports #####################################################

import time

import textwrap

import random

# Global Variables ############################################

WIDTH = 58

CAVES = ['right', 'left']

DELAY = 1.25

WRAP = 45

# Functions ###################################################

def describe(message):
    for line in textwrap.wrap(message, WRAP):
        print("   ", line)

def intro():
    """Display the intro description to the player"""
    describe("""You are in a dangerous land of magic and dungeons and...DRAGONS. Before you
you glance two caves. In one cave, the friendly dragon Herenity the Friendly would offer
his treasure to you weary traveler. In the other you shall feel the violent might of
Boof the Mean and he'll kill you for your hubris.\n""")
    print()
    
def valid_cave(response):
    """Return True if response is in list of valid CAVES"""
    return response in CAVES 

def choose():
    """Prompt player to pick "right" or "left" then return response"""
    cave = ""
    while not valid_cave(cave):
        print("Do you enter the cave on the left or right, or do you run")
        cave = input("(right,left): ").lower()
        # print("> Hint: You said", cave)

        if not valid_cave(cave):
            print('Type "right or "left". \n')
    print()
    return cave

def enter(cave):
    """Print the description of the cave, and print what the dragon does based on cave
       Args: cave is "left" or "right"
    """   
    messages = [
        "You move towards the darkness...",
        "Welp there's a spooky cave...",
        "The atmosphere takes hold of your heart..."
    ]
    
    for message in messages:
        describe(message)
        time.sleep(DELAY)

    nature = is_friendly(cave)
    # print("> Hint: The dragon you choose is:", nature, "friendly")
    dragon(nature)

def is_friendly(dragon):
    """Return is true iff dragon is in randomly chosen friendly"""
    friendly = random.randint(0, 1)
    # print("> Hint: The dragon value is:", dragon)
    # print("> Hint: The friendly dragon is:", friendly, CAVES[friendly])

    return dragon == CAVES[friendly]

def dragon(is_friendly):
    """Print the dragon option for friendly or unfriendly"""
    actions = {
        #friendliness:action
        True: "You GET PAID...in decorative towels?",
        False: "BOOF GOBBLES YOU ALIVE!",
    }

    print()
    describe(actions[is_friendly])
    print()


# Script Runner ###############################################

def main():
    """Welcome to the Dragon Realm Trial of Vengeance"""
    print("Welcome to the Dragon Realm")
    again = 'yes'
    while again.lower() in ["y", "yes", "sure"]:
        print("-------------------------------------\n")
        intro()
        cave = choose()
        enter(cave)
        again = input("Play again? ")

if __name__ == '__main__':
    main()
