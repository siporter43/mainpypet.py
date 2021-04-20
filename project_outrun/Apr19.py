from pathlib import Path

"""We're going to write a fncn to list all the .txt files in our data directory"""

"""fncns"""

def main():
    path = Path("data")
    for f in path.iterdir():
        if f.suffix == ".txt":
            print(f.name)

def temp_maker():
    path = Path("data")/"tmp"
    path.mkdir(exist_ok=True)
    
def temp_breaker():
    path = Path("data")/"tmp"
    path.rmdir()

def empty_file_maker():
    path = Path("data")/"tmp"
    path.mkdir(exist_ok=True)
    i = 1
    while i <= 9:
        box= f"file_{i}.txt"
        i += 1
        # print(box)
        new_path = path/box
        new_path.touch()

"""runner"""

# main()

#temp_maker()

# temp_breaker()

empty_file_maker()
