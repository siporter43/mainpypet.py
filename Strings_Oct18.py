"""This is our new lesson on Strings"""

# IMPORTS


# GLOBAL VARIABLES

# FNCNS

from typing import Text


def rhyme():
    rhyme= """Roses are red, \nViolets are purple, \nDoing a bunch of loops
    Puts me in a circle"""
    print(rhyme)

def lymric():
    verse= """Rockabye baby in the treetop, 
    When the wind blows
    the cradle will rock.
    When the bough breaks,
    The cradle will fall.
    And down will come baby
    Cradle and all"""
    print(verse)

def number_lines():
    numbers = "one \n two \n three"
    print(numbers)


def double_double():
    print("\"What up\"")

def single():
    print('\'the sky\'')


def b_slash():
    print("\\Or else\\")

def r_writ():
    print(r"Hotel\Bilding\Dag")

def string_cat():
    ursa = "Bear people"
    print("Watch out for " + ursa + ".")
    
def quote():
    quote = "Don't put all your fish in one basket"
    text = quote.split()
    print(text)

def flavoring():
    flavors = "banana split;hot fudge;cherry;malted;black and white"
    ice_cream = flavors.split(";")
    print(ice_cream)

def day_word():
    word = "demagogue"
    daily = list(word)
    print(daily)

def day_week():
    day = ["m", "o", "n", "d", "a", "y"]
    week = "".join(day)
    print(week)

def dino_party():
    dinosaurs = ["T-Rex", "Stegasaurus", "Betty White"]
    party = "\n".join(dinosaurs)
    print(party)

def to_12hr(time):
    """
        Take the 24 hour string time and return a 12 hour version.
        
        >>> to_12hr("08:00")
        "8:00 AM"
        >>> to_12hr("23:15")
        "11:15 PM"
    """
    # [x] split the time string on ":"
    # [x] convert both parts to an int
    # [x] test if the hour is > 12
    #     [x] if so, subtract 12
    #     [x] make it PM
    # [x] otherwise
    #     [x] make it AM
    # [ ] make an list named nice_time and add the time string (like "11:15") and the period (like "PM")
    # [ ] join them together with a space
    # [ ] return the new formatted string containing the hour, minute and period
    clock = time.split(":")
    clock[0] = int(clock[0])
    if clock[0] > 12:
        clock[0] = clock[0] - 12 
        clock.append("PM")
    else:
        clock.append("AM")
    # nice_time = [str(clock[0]) + ":" + clock[1]]
    nice_time = [f"{clock[0]}:{clock[1]}", clock[2]]
    text = " ".join(nice_time)
    # print(clock)
    return text    



# SCRIPT RUNNER

# rhyme()

# print(help(rhyme))

# lymric()
# number_lines()
# double_double()
# single()
# b_slash()
# r_writ()
# string_cat()

# quote()

# flavoring()

# day_word()

# day_week()

# dino_party()

time = to_12hr("23:45")
print("the time is (not actually)", time)

time = to_12hr("5:30")
print("and now the time is (not actually)", time)
