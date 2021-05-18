from pathlib import Path

"""
ex.15
[x]Use .touch() to make an empty file xxx.txt
[x]Make a new Path object to data/xxx.txt
[x]Check to make sure data/xxx.txt does not exist, and print an error if it does.
[x]Print a message {samp}”Moving ‘{from}’ to ‘{to}’.”
[x]Use .replace() to move the file.

ex.17
[x]Rename the file_1.txt that you created earlier to file_01.txt.
[x]Be sure to check first that the destination does not already exist.
[ ]Print the files new name.
"""

"""fncns"""

def x_maker():
    path = Path("xxx.txt")
    path.touch()
    print("I'm ready spaghetti")
    to_path = Path("data")/ "xxx.txt"
    if to_path.exists():
        print(f"Error: '{to_path}' already exists")
    else:
        path.replace(to_path)
        print(f"File moved for '{path}' to '{to_path}'")
    print("THE BUTLER DID IT!")


def new_name():
    folder = Path("data") / "tmp"
    from_path = folder / "file_3.txt"
    to_path = folder / "file_03.txt"
    if to_path.exists():
        print(f"Error it's already therror")
    else:
        from_path.replace(to_path)
        print(to_path)
    print("We don't live here no more")
    


"""runner"""

# x_maker()

new_name()
