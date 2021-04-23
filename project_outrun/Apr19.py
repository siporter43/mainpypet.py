from pathlib import Path

"""We're going to write a fncn to list all the .txt files in our data directory"""

"""fncns"""

def main():
    path = Path("data")
    for f in path.iterdir():
        if f.suffix == ".txt":
            print(f.name)

def otra_dir():
    path = Path("tests")
    for f in path.iterdir():
        print(f.name)

    
def temp_maker():
    path = Path("data")/"tmp"
    path.mkdir(exist_ok=True)

def new_maker():
     path = Path.cwd()
     path = path.parent / "project_trello" / "kim_gordon"
     path.mkdir(exist_ok=True)
     print(path)   

# def far_breaker():


def far_file():
    path = Path.cwd()
    band_path = path.parent / "project_trello" / "kim_gordon" 
    file_path = band_path / "kissability"
    file_path.touch()
    print(file_path.absolute())

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

# empty_file_maker()

# otra_dir()

# new_maker()

far_file()
