#trying to write a list of lunch specials and print them with a number on individual lines
mylist = list()
mylist = []
mylist = [1, 2, 3, 4, 5]

lunch_specials = [
    "ham-dogs",
    "hot burgers",
    "Donut Bucket",
    "chicky tendies",
    "Unfortunate tuna"
]

for lunch_special in lunch_specials:
    print(lunch_special)

lunch_specials.append("dog biscuits")

for lunch_special in lunch_specials:
    print(lunch_special)

fav_movies = ["almost famous", "apocalypse now", "persepolis", "infinity war"]
for num, movie in enumerate(fav_movies):
    print(f"#{num+1}:", movie)

"""
noun_list = ("man", "woman", "camera", "tv", "person")
print(noun_list)
"""

varname = list("my body left for the summer")
varname.sort()
print(varname)
"""
my_statement = "my body left for the summer"
print(my_statement)
vacation = list(my_statement).sort()
print(vacation)
"""
my_str = "words are for nerds"
nerdy = my_str.split()
nerdy.sort()
print(nerdy)

sentence = "+".join(nerdy)
print (sentence)