"""Here we're doing some works on our file i/o, paths, and file system ops"""
"""This exercise is to generate files for a list of people that you can use to keep track of notes, 
birthday info, gift ideas etc.

At the end of the exercise you should have a folder containing a file for each person that 
contains something related to that person.

1.[x] Make a list of people's names that you'd like to keep track of information about.
2. [x]Create a new directory called something like people if it does not exist.
3. [ ]Iterate over the list of people.
    -[x] Create a blank file called {name}.txt in the people directory if it doesn't exist.
    - [ ]Write something to the file about that person
    
4. Write something different for each person in the list
    [ ] Change the list to a dict where the key is the name of the person
        and the value is a gift idea.
    [ ] Change your for loop to get the name and gift of each item
        in the dict using the .items() method
    [ ] Write a second line to the file with their gift idea
"""

from pathlib import Path

"""variables"""

commie_list = ["Kitty Pryde", "Scott Summers", "Jean Grey", "Orroro Monroe", "Kurt Wagner", "etc"]


"""fncns"""

def main():
    path = Path("data") / "Xman_Xmas"
    path.mkdir(exist_ok=True)
    print("Make way for the Homo Superior!")

def del_firstd():
    path = Path("Xman_Xmas")
    path.rmdir()
    print("Dawn has fell")

def x_file():
    path = Path("data")/ "Xman_Xmas"
    
    for name in commie_list:
        wording = name.replace(" ", "_")
        new_path = path/ f"{wording}.txt"
        # print(f"creating file for {name}" , new_path)
        new_path.touch()    
    
    print("Phoenix Rose")

def x_write():
    """Here we want to add some sort of text to each of the newly created files"""
    print("=" * 50)
    path = Path("data") / "Xman_Xmas"
    for file_path in path.iterdir():
        print(f"writing to {file_path}")
        fh = open(f"{file_path}", "w")
        fh.write("Create More Mutants")
        fh.close()
    print("harm no man")
    print("=" * 50)

"""script runner"""

# main()

# del_firstd()

# x_file()

x_write()
