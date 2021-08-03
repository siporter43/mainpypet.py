"""This is our dictionaries lesson start"""

# Imports

from os import SEEK_HOLE
import random
import pprint


# Global Variables

# Fncns

numbers = {"one": 1, "two":2, "three": 3, "four": 4, "five":5, "six": 6, 
"seven":7, "eight":8,"nine": 9, "ten":10}

def add(a,b):
    """we want to add the value 2 number strings"""
    solution = numbers[a] + numbers[b] 
    return solution


points = {"A": 1, "E":1, "I":1, "L":1, "N":1, "O":1, "N": 1, "R":1, "S":1, "T":1, "U":1,
"D":2, "G":2, "B": 3, "C":3, "M":3, "P":3, "F":4, "H":4, "V":4, "W":4, "Y":4}

def score(letters):
    for letters in points:
        i = len(letters)
        total = letters[i] + total
        continue
    print(f"{total} is the score for word: {letters}")

# runner


