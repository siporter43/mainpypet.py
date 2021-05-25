"""this is a lesson that reviews fncns"""
from random import randint
import random 

"""fncns"""
def hr():
    """we're doing a line"""
    print("-" * 100)



def header(title, y ):
    """"we're writing a title and lining it with a given character"""
    underline = y * len(title)
    print(underline)
    print(f"{title}\n{underline}")

def number():
    """this fncn will return a random number bw 1 and 100"""
    print(f"hello {randint(1,100)}")

def numero():
    """we're doing a random generator with return as the action"""
    return print(randint(1,50))

"""runner"""


if __name__ == "__main__":
    # hr()
    # header("Bar Mitzvah", "=")
    # header("Bar Mitzvah", "-")


    # header("I am a shiny toybox", "o")

    # number()
    # numero()
