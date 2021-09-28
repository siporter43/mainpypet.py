"""Today is a day for string formatting"""


def format_email(user, domain, extension):
    return f"{user}@{domain}.{extension}"

print(format_email("cat", "hotmail", "gov"))

print(format_email("billy", "yahoo", "boot"))

print(format_email("doge", "mail", "mail"))

