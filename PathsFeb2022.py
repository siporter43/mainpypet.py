from importlib.resources import contents
from pathlib import Path

def main():
    path = Path("contacts.txt")
    if not path.exists():
        print(f"{path} doesn't live here, man")
        return

def fncn_run():
    path = Path("pets.py")
    fh = open(path)
    contents = fh.read()
    fh.close()
    print(contents)


# main()

fncn_run()
