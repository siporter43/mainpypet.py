"""this is an exercise-based lesson"""

from pathlib import Path

"""fncns"""

def welcome(name):
    """for this fncn we are going to say welcome to class"""
    print(f"Welcome to coding class {name}!")


def letter_count(word):
    """this fncn will tell us how many characters in a word"""
    print(f"There are {len(word)} characters in {word}")


vowels = ("a", "A", "e", "E", "i", "I", "o", "O", "u", "U", "y", "Y")

def is_vowel(letter):
    """for this fncn we will determine whether a letter is a vowel and provide a true or false"""
    if letter not in vowels:
        # print(f"{letter} is not a vowel")
        return False
    else:
        # print(f"{letter} is a beautiful vowel")
        return True

def is_it(letter):
    """for this fncn we're gonna have the is_vowel fncn print its results"""
    print(f" Is {letter} a vowel?", is_vowel(letter))


def tip(total, tip_percent):
    pay_tip = total * (0.01 * tip_percent)
    return pay_tip
    # total_bill = pay_tip + total
    # print(f"On a ${total} tap and tipping {tip_percent}%, it would make sense to tip ${pay_tip}. Making your total ${total_bill}")

def how_much(total, tip_percent):
    print(f"For a bill of ${total} with a {tip_percent}% tip $", tip(total, tip_percent))

"""runner"""

# welcome("bingo")

# letter_count("android")

# is_it("poe")
# is_it("2323")
# is_it("u")
# is_it("E")

# tip(100, 20)
# should return 20
# tip(200, 5)
# tip(5,50)
how_much(10, 10)
how_much(25, 25)
how_much(1, 200)
