# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python3
PyPet Battle Game:
* Two fighters are randomly chosen from a list of PETS, each starting with a
health of 100
* Print out details about the chosen fighters
* Each fighter takes a turn attacking the other until one fighter wins.
    - Each attack will have a description and do randomly selected amount of
    damage between 10-30
    - Each attack will print out the description of the attack, the damage it
    did, and the health of each fighter at the end of the turn
    - Whoever reaches 0 first loses and the other player wins.
* At the end of the game, announce the winner
"""

# The convention is to name modules (Python files) using
# lower_case_with_underscore
#
# The code for a project should be in a directory named using lowernounderscore
#   for example:
#
#   myproject/
#       my_module.py
#       my_script.py

# ### Imports ################################################################
from pets import PICS, PETS

import random

import time


# ## Global Variables ########################################################

DELAY = 1

WIDTH = 50 

MAX_HEALTH = 100

POWER = (10, 30)

#a list of attacks for some fightin flavor

FIGHTIN_WORDS = (
    "punches through",
    "lunges onto",
    "hits the slam-a-jam on",
    "does that thing where you rip off an arm to",
    "emotionally cripples",
    "hits em with some hot verses",
    "removes the feet of",
    "mutters passive agressively at",
    "reveals the truth of the universe to",
    "swan dives into",
    "viciously cuddles",
)


# The convention is to name global variables using ALL_CAPS_WITH_UNDERSCORE
#
# GLOBAL_VARIABLE = 2


# ## Functions #################################################y
##############
#pet functions: just some fncns that refer to pet stuff

def show(pet):
    """Takes a pet and shows its health and pic"""
    name_display = f"{pet['name']} {pet['pic']}"
    health_display = f"{pet['health']} of {MAX_HEALTH}"
    rcol_width = WIDTH - len(name_display) - 1
    print(name_display, health_display.rjust(rcol_width))


def setup(pets):
    """Takes list of pets and sets initial attributes"""
    for pet in pets:
        pet['health'] = MAX_HEALTH
        pet['pic'] = PICS[pet['species']]

# ###Game event fncns###

def attack(foe):
    """Inflict a random amount of damage, then return that value & attack used"""
    act = random.choice(FIGHTIN_WORDS)
    damage = random.randint(POWER[0], POWER[1])
    foe['health'] -= damage
    return damage, act

# ### top-level game functions ###
#

def lotto():
    """Return two randomly chosen PETs"""
    random.shuffle(PETS)
    #shuffle randomly re-orders the PETS list
    return[PETS[0], PETS[1]]

#this is just the intro, providing names and stuff
def intro(fighters):
    """    Takes a list of two PETs (fighters) and prints their details"""
    print("\n Tonight for you filthy animals is the glorious battle of...\n")
    time.sleep(DELAY)
    header = f"***{fighters[0]['name']} -VS- {fighters[1]['name']}***"
    print(header.center(WIDTH), "\n\n")
    input("WHERE'S THE BEEF?")
    print("." * WIDTH, "\n")

def fight(fighters):
    """Repeat rounds of the fight until one wins then
       Take a list of two PETs and return the winning PET"""
    winner = None
    current = 0
    while winner is None:
        attacker = fighters[current]
        rival = fighters[not current]
        input(f"\n{attacker['name']} fight>")
        # the attack
        damage, act = attack(rival)
        #pause for dramatic effect and print attack deets
        time.sleep(DELAY)
        print(f"\n {attacker['name']} {act} {rival['name']}...\n")
        #pause them show damage
        time.sleep(DELAY)
        print(f"-{damage} {rival['name']}".center(WIDTH), "\n")
        time.sleep(DELAY)
        #check for a loser
        if rival['health'] <=0:
            #doesn't allow hp to drop below 0
            rival['health'] = 0
            #set winner, this is last round
            winner = attacker
        print()
        for combatant in fighters:
            show(combatant)
        print("-" * WIDTH, "\n")
        current = not current 
    return winner
"""so yeah the while loop is basically the end of a round of battle"""

def endgame(winner):
    """Takes a PET (winner) and announce that they won the fight"""
    print()
    print(f"{winner['name']} is the TRUE MANDALORE!".center(WIDTH), "\n")
    print(winner['pic'].center(WIDTH), "\n")
    print("-" * WIDTH, "\n")

# The convention is to name functions, arguments, and local varibales using
# lower_case_with_underscore
#

#  def some_func():
#      """Short description of the function, including info about any arguments
#         and/or return values"""
#      ...


# The main() function should be at the last function defined
#

def main():
    """Main part for the Pypet Fight Game"""
    print("Gracias to the Blood&Thunderdome.")
    fighters = lotto()
    setup(fighters)
    intro(fighters)
    winner = fight(fighters)
    endgame(winner)
    

# ## Runner ##################################################################

# This calls the main() function if the script is being run directly
#   but not if it is being imported as a module

# This should always be at the very end of the script
#

if __name__ == "__main__":
    main()
