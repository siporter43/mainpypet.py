# def coin_flip():
# """trying to write a loop that asks the user heads or tails until they answer"""

    # answer =  ["heads","tails","Heads","Tails"]
    # reply = ""

    # while reply not in answer:
    #     reply = input("Heads or Tails? ")
    #     print

    
import random

# def guess_random():
# """writing a while loop that prints a random between 1-100 until the number is >50"""
#     number = 0
#     while number<50:
#         number = random.randint(1,100)
#         print(number)
    
#     while True:
#         num = random.randint(1,25)
#         print("Thy numeral ist:", num)
#         reply = input("Continue? ")
#         if reply == "n":
#             break

# def roll_check():
# """we're trying to pick rolls randomly, decide whether or not to keep them, and append them to this list. Then break. Then print list."""
#     rolls_list = []
#     roll_count = 0

#     while roll_count < 10:
#         roll_count += 1
#         roll = random.randint(1,6)
#         print("Your roll is:", roll)
#         reply = input("Continue and append roll? ")
#         if reply == "n":
#             print("Well I guess someone is lame...psh")
#             continue
#         print("That's the way I likes it!")
#         rolls_list.append(roll)
#         print (rolls_list)

import time
DELAY = 1

# i=3

# while i>0:
#     print("iteration:", i)
#     i = i - 1
#     time.sleep(DELAY)

# def lunch_check():
#     """We're here to create a lunch menu list with numbers"""
#     i=0
#     lunch_menu= ["fire flakes", "snow flakes", "corn flakes", "pastry flakes"]

#     while i < len(lunch_menu):
#         print("Food thing", i+1, "is:", lunch_menu[i])
#         i +=1
 

# def vowel_check():
    # """the goal is to have only the vowels printed with their..."""
#     vowels = ["a","e","i","o","u","y"]
#     word = input("Enter a word, you pescatarian: ")

#     i = 0
#     while i < len(word):
#         if word[i] in vowels:
#             print("Letter", i + 1, "is:", word[i])
#         i+=1

# def beer_wall():    
#     i = 3
#     while i > 0:
#         print (i, "Bottles of beer on the wall. Take one down. Pass it around", i - 1, "Bottles of beer on the wall")
#         time.sleep(DELAY)
#         i -= 1

#Practice Exercises Loops 1/11/2021

#2 We are trying to write the "For he's a jolly good fellow" song. So three iterations of that phrase
# Then add "which nobody can deny" on the last go. Godspeed

def jolly_good():
    i = 3
    while i > 0:
        print("For he's a jolly good fellow...")
        time.sleep(DELAY)
        i -= 1
    print("Which nobody can deny!")
    
def name_cheer():
    """Plan is to do the "gimme an A..gimme a ___" etc for your name" """
    name = "Sean"
    
    i = 0
    while i < len(name):
        print("Gimme a", name[i], "!")
        i += 1
    
    print(f"And what's that spell? {name} !")

def multi_table():
    """Plan is to create a 9x9 multiplication table"""    
    rows, cols = 10, 10
    r = 0 
    while r < 10:
        print(r)
        c = 0
        while c < 10:
            print(c)
            c += 1
        r += 1
        print(r * c)
   
multi_table()
        

    
