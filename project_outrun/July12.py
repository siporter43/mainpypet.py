"""this is our Loop lesson"""

"""Imports"""


"""Global Variables"""


"""Fncns"""

# # def movie_it():
# """this is where we text out iterating with a for loop"""
#     movies = [
#     "The Matrix",
#     "Ex Machina",
#     "Honey, I Shrunk the Kids",
#     "Breakin'",
#     "The Croods"
#     ]
#     for item in movies:
#         print(f"I like {item}...probably")

# # def name_itera():
#     """this is a fncn that uses the iter fncn to iterate over the list"""
#     letters = ["s", "e", "a", "n"]
#     letter_iterator = iter(letters)
#     for item in letters:
#         print(next(letter_iterator))


game_roles = ["bard", "fighter", "rogue", "wizard", "hacker", "loving grandma"]

def it_game_for():
    for role in game_roles:
        print(f"This choice:{role} is your only hope")

def it_game_while():
    game_iterator = iter(game_roles)
   
    while True:
        try:
            role = next(game_iterator)
        except StopIteration:
            break
        print(f"Role could be: {role}")


tool_role = {
    "guitar":"bard", 
    "fist":"fighter", 
    "lockpick":"rogue", 
    "wand":"wizard", 
    "computer":"hacker", 
    "fresh baked cookies":"loving grandma"
    }

def tool_role_while():
    tool_role_iter = iter(tool_role.items())
    while True:
        try:
            tool, role = next(tool_role_iter)
        except StopIteration:
            print("It done")
            break
        print(f"A {role}'s favorite tool is the trusty {tool}")

def tool_role_for():
    for tool, role in tool_role.items():
        print(f"The {tool} of the {role} is a most dangerous object")


"""Runner"""

# movie_it()

# name_itera()

# it_game_for()

# it_game_while()

tool_role_while()

tool_role_for()
