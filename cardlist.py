my_cards = ["7C" , "KH" , "JD" , "QS" , "5H"]
print(my_cards)



my_chapters = [
    "I'm not feelin your attitude",
    "Bet",
    "Come at me, Bro",
    "Knuck if you buck",
    "FIST FIGHT",
    "End Daydream Sequence"
]

for x, element in enumerate(my_chapters):
    print("Chapter", (x + 1),":", element)


#    item  balance
#            =  0  # before iterating
#    + 8     =  8  # first iteration
#    + 5     = 13  # second iteration
my_numbers = [1, 4, 7, 9, 11, 13]
def running_sum(my_numbers):
    tot=0
    for item in my_numbers:
        tot += item
        print (item, tot)
running_sum(my_numbers)



my_str= "bond, james, 760-867-5309"
my_str_part = my_str.split(",")
print (my_str_part)
print (my_str_part[1].title(), my_str_part[0].title(), my_str_part[2])


# example
groceries = [ "milk", "eggs", "hamburger" ]
for i, item in enumerate(groceries):
    if item == "hamburger":
        groceries[i] = "extra-firm soy"
###

###need to change the thing 
my_smile= "oh hai :smile:"  
my_smile= my_smile.split()
print (my_smile)
# value1 == value2
for i, item in enumerate(my_smile):
    if item == ":smile:":
        #print (item)  
        my_smile[i]= "😄"
print(my_smile)
my_smile = " ".join(my_smile)
print (my_smile)

#dictionary for character changes#
chars = {
    "l": "1",
    "s": "$",
    "a": "@",
    "i": "!",
    "e": "3",
    "o": "0",
    "t": "7",
    " ": "_"
}

a_string = "hello"
a_list= list(a_string)
print(a_list)
for i, c in enumerate(a_string):
    if c == "l":
        a_list[i]+ "1"

print 