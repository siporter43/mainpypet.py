"""Today is a day for string formatting"""
from pathlib import Path

def format_email(user, domain, extension):
    return f"{user}@{domain}.{extension}"

print(format_email("cat", "hotmail", "gov"))

print(format_email("billy", "yahoo", "boot"))

print(format_email("doge", "mail", "mail"))

def game_file():
    path = Path("Adventure.py")
    print(f"We're creating the file {path} right now!")
    path.touch()


game_file()
