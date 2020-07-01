print('Ello Govna')

# Variables

def hr():
  print('--------------------')

friend = {
  'name' : 'Boyo',
  'hungry' : True,
  'spicy' : True,
  'tired' : True,
  'weight' : 10,
  'age' : 30,
  'hp' : 50,
  'photo' : '([0]-I-[0])',
}

bro = {
  'name': 'Adrian',
  'age': 32,
  'weight': 12,
  'hp' : 77,
  'hungry': True,
  'spicy': True,
  'tired': True,
  'photo': '([#]_^_[#])',
}

pets = [friend, bro]

# functions

hr()

# I added this bit to do testing. I think you're running into a error (line 8-9) from trying to call 'friend' and 'bro' before they've been defined (line 13-22 & 49-58)
"""print('jayson was here')
pets = [friend, bro]
print (pets)"""
# To help for readability and solve that error, I'd recommend organizing your code into sections, with your variables and dictionaries at the top, then your functions, and then the parts where you actually call your functions and print your things.
# you can use comments to make section headers to help



print ('hello '  +  friend['name'])
print (friend['photo'])

# So in lines 39-44 and 67-73, you seem to be doing the same function. 

def feed(friend):
  if friend['hungry'] == True:
    friend['hungry'] = False
    friend['weight'] = friend ['weight'] + 1
  else:
    print('Boyo is no hungries')
#Ask about why this no longer happens in the code 

print(friend)
hr()

print('Hello ' + bro['photo'])
hr()
print('No hello for yous ' + friend['photo'] + ' No take backs')
hr()

hr()

print (bro)
feed(bro)
print (bro)

hr()

print (friend)
feed (friend)
print (friend)

hr()

for pets in pets:
  feed(pets)
  print (pets)

  hr()

  feed(pets)

  hr()


  if pets['spicy'] == True:
    pets['spicy'] = False
    pets['hp'] = pets['hp'] - 5
  else:
    print ('YOU have no power in this realm, Fools!')
    print (';p')
hr()

punch(pets)
punch(bro)
print(pets)
hr()

punch(friend)
print(friend)
hr()

punch(friend)
print(friend)
hr()

feed(pets)
print (pets)
hr()

def hug(pets):
  if pets['tired'] == True:
    pets['tired'] = False
    pets['hp'] = pets['hp'] + 4
  else:
    print("You're not really my type")

hug(pets)
print (pets)
hr()

