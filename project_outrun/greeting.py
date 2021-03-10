def greeting(name):
    """Return a welcome message string, including formatted name unless it's blank."""
    name = name.strip().title()
    if not name:
        return "Welcome."
    else:
        return f"Welcome {name}."

    