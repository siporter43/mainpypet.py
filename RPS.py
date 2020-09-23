"""This is a game of Rock, Paper, Scissors where the User is provided with a choice of those 3. Then the computer randomly chooses another and they compare to determine winner"""


#imports#########################################################

import random

import textwrap



#Global Variables############################

WIDTH = 58

CHOICE = ['rock', 'paper', 'scissors']

DELAY = 1

WRAP = 30

#Code Hax######################################################

def describe(message):
    for line in textwrap.wrap(message, WRAP):
        print("   ", line)

def intro():
    """Display the intro description to the player"""
    describe("""Welcome to a Game of Skill and Luck and Rocks 
    and Papers and Scissors. Pick one. Accept your fate. KTHXBYE .\n""")
    print()
    
def valid_choice(response):
    """Return True if response is in list of valid CHOICE"""
    return response in CHOICE 

def choose():
    """Prompt player to pick "rock" or "paper" or "scissors" then return response"""
    choice = ""
    while not valid_choice(choice):
        print("You need to choose rock, paper, or scissors")
        choice = input("(rock, paper, scissors): ").lower()
        # print("> Hint: You said", WHAT?)
        if not valid_choice(choice):
            print('Type "rock" or "paper" or "scissors". \n')
    print()
    return choice

def play():
    #this is to determine if the player beats the round against the computer...hmmm
    #needs to have RPS and simultaneously the same with the computer then have the choices
    #compared and determine winner from that
    
    #while winner is None:
    computer_choice = random.choice(CHOICE)
    return computer_choice


player_choice = choose()

print ("The Robots choose " + play() + " And You chose " + player_choice)

