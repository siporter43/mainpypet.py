#this is the guessing number game python3
import random
number = random.randint(1,25)

max_guesses = 6
print('Party')

player = input("Hello! What is your name? ")
print("Wut is the haps " + player + " -_-")

print("I'm thinking between a bunch of numbers. Let's say between 1 and 25. Figure it out, chump")
print()

# for guess_count in range(0, 6):
    
# guess_count = 0
# while guess_count < 6:

# for guess_count in range(max_guesses):
    # print("Guess", str(guess_count + 1), "of", max_guesses)

for guess_count in range(1, max_guesses+1):
    print("Guess", guess_count, "of", max_guesses)
    guess = input("Your guess: ")
    guess = int(guess)

    if guess < number:
        print("You thinking too small, chump")

    elif guess > number:
        print('You higher than a bong on a ladder')
    
    else:
        break
    print()
################################################################################

#the above print fncn is used just to create a spaced line
if guess == number:
    guess_count = str(guess_count)
    print('Good job, ' + player + '! You guessed right in ' +guess_count + 
          ' guesses! You were probably top of your class at Clown College')
else:
    number = str(number)
    print('Nopitty Nope Nope. The number I was thinking of was ' + number + 
          '.  Well, at least you were valedictorian at Chico State')