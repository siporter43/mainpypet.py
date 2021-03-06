"""The goal of the following exercise is to create an ice cream flavors list and a numbered menu"""
# so i'm creating a list of all the flavors. not a variable
ice_cream_flavors = ["banana", "chocolate", "lemon", "pistachio", "raspberry", "strawberry", "vanilla"]

# I'm making i a variable that will help us increment/keep track of placement in the list
i = 0
# then i'm creating a while loop that occurs for the length of flavors 
def flavor_menu():
    while i < len(ice_cream_flavors):
        print("FlavorTown City District", i + 1, "is:", ice_cream_flavors[i])
        i += 1


"""print every possible dual combo without redundancies and doubles"""

# find a way to pair...maybe something like i and i+1 

flavor_combo = ["banana chocolate", "banana lemon", "banana pistachio", "banana raspberry", "banana strawberry", "banana vanilla",

"chocolate lemon", "chocolate pistachio", "chocolate raspberry", "chocolate strawberry", "strawberry vanilla",

"lemon chocolate", "lemon pistachio", "lemon raspberry", "lemon strawberry", "lemon vanilla",

"pistachio raspberry", "pistachio strawberry", "pistachio vanilla",

"raspberry strawberry", "raspberry vanilla",

"strawberry vanilla"]
def flavor_party():
    i = 0
    while i < len(flavor_combo):
        # print("Combo", i, ice_cream_flavors[i], ice_cream_flavors[i+1])
        i += 1

# with this i'm trying to apply the multiplication this problem
def flavor_combo():
    r = 0
    while r < len(ice_cream_flavors):
        c = r + 1
        while c < len(ice_cream_flavors):
            print(ice_cream_flavors[r] + ice_cream_flavors[c])
            c += 1
        r += 1

flavor_combo()
