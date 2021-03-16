
# Functions
def groceries():
    fh = open("data/groceries.txt")
    contents = fh.read()
    fh.close()
    print("Groceries")
    print("=========")
    fh = open("data/groceries.txt")
    for line in fh.readlines():
        print(line, end="")
    fh.close()

# print("=========")

def mug_brownie():
    fh = open("mug-brownie.md")
    for line in fh.readlines():
        print(line, end="")
    fh.close()

def todo():
    fh = open("data/todo.txt")
    for line in fh.readlines():
        print("*", line, end ="")
    fh.close()

def make_groceries():
    groceries = [
        "blueberries", 
        "granola", 
        "dog food", 
        "My enemies"]
    
    fh = open("data/groceries.txt", "w")
    for item in groceries:
        fh.write(f"- {item} \n")
    fh.close()

def add_groceries():
    fh = open("data/groceries.txt", "a")
    fh.write("boogers\n")
    fh.close()

def auto_mug_brownie():
    with open("mug-brownie.md") as fp:
        contents = fp.read()
    print(contents)

"""Runner"""

# make_groceries()

# add_groceries()
auto_mug_brownie()


