"""This is our beginning of file system operations lesson"""

"""Goal:
[ ] iterate over the contents of the working directory
    [x]skip over files/directories with names that start with . or _
    [x]print the name of directories followed by a /
    [.]print the name of anything else
"""

from pathlib import Path

def main():
    cwd = Path.cwd()
    for f in cwd.iterdir():
        if f.name[0] in ("_","."):
            continue
        if f.is_dir():
            print(f"{f.name}/")
        else:
            print(f.name)
    # path = Path("bling/blong/data.txt")
    # print(f'the filename is "{path}" is: {path.name}"')


main()
