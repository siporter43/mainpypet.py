"""Today we're doing work with Dictionaries"""

"""imports"""
from pprint import pp, pprint
"""fncns"""

shapes = {
    "triangle": 3,
    "square": 4,
    "pentagon": 5,
    "hexagon": 6,
    "heptagon": 7,
    "octagon": 8
}

def ask_shape():
    answer = input("Please name a shape... ")
    sides = shapes.get(answer, None)
    
    if not sides:
        print(f"I don't know the shape {answer}...maybe take a geometry class")
    else:
        pprint(f"A {answer} has {sides} sides.")



"""runner"""

# pprint(f"A triangle has {shapes['triangle']} sides")

ask_shape()
