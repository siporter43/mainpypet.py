# a = "hello"
# print(a.upper())

from pprint import pprint
from pathlib import Path

path = Path("alissa.py")
# pprint(list(dir(path)))
dir(path)

print("stem:", path.stem, "name:", path.name)

print("is_file:", path.is_file(), ", exists:", path.exists())

path.as_uri()

if callable(path.with_suffix):
    print("with_suffix is a method")
else:
    print("with_suffix is a property")

help(path.with_suffix)
