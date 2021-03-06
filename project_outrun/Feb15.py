"""We're doing list refresher and deep-dive"""

# Create list of 5 songs. Print the 2nd song.Print the last song. Use concatenation to add 2 more. Use a slice to remove last song

cool_songs = ["Tom's Diner", "Song 2", "Safety Dance", "Hokey Pokey", "Party all the time"]

print ("The second song is:", cool_songs[1])

print("The last song is:", cool_songs[-1])

cool_songs = cool_songs + ["Lovefool", "In the air tonight"]

print(cool_songs)

cool_songs = cool_songs[:-1]

print(cool_songs)

message = "How much for that doggy?"

for letter in message:
    print(letter)


class_list = {"english": 15, "spanish": 20, "arabic": 12, "american": 2}
