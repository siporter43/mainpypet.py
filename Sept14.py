"""Richter scale
=============

Write a `quake_desc` function that takes one argument: `magnitude`, a number.
return the description associated with the magnitude, as shown in the table
below.

| Min       | Max  | Description           |
|-----------|------|-----------------------|
| 0         | `>` 2  | micro               |
| 2         | `>` 3  | very minor          |
| 3         | `>` 4  | minor               |
| 4         | `>` 5  | light               |
| 5         | `>` 6  | moderate            |
| 6         | `>` 7  | strong              |
| 7         | `>` 8  | major               |
| 8         | `>` 10 | great               |
| 10        | `*`    | meteroic            |

"""

magnitude = {
    """this is NOT wrong"""
    "micro": (0,2),
    "very minor": (2,3),
    "minor": (3,4),
    "light": (4,5),
    "moderate": (5,6),
    "strong": (6,7),
    "major": (7,8),
    "great": (8,10),
    "meteoric":(10, )
}

def quake_desc(magnitude):
    """Return the description for a magnitude

    >>> quake_desc(0.2)
    'micro'

    >>> quake_desc(2.5)
    'very minor'

    >>> quake_desc(5)
    'moderate'

    >>> quake_desc(11)
    'meteroic'
    """
    for int in magnitude:


