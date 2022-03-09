"""  https://github.com/siporter43/mainpypet.py/blob/master/MovieList.py
Example of how it should work:

1 Pinocchio
2 Dumbo
3 Bambi
4 Alice in Wonderland
5 Robin Hood


Type the number of your favorite movie. 4

1 Alice in Wonderland
2 Pinocchio
3 Dumbo
4 Bambi
5 Robin Hood

"""

films = [
    "Pinocchio",
    "Dumbo",
    "Bambi",
    "Alice in Wonderland",
    "Robin Hood",
]


# [x] A. Ask the user what item the want to move

def film_review():
    # list the movies
    for i, item in enumerate(films, 1):
        print(i, item)
    
    # ask the user
    # user = index number of movie (i) and the place number
    user = input("Type the number of your favorite movie.")
    number_of_films = len(films)
    
    # [x] B. Make sure it is a movie in the list
    if int(user) > 0 and int(user) <= number_of_films:
        print(user)
    else:
        print("That movie isn't there, friends. Try again")
        return
    answer = int(user) -1
    if answer < number_of_films:
        # [x] C. Print the name of the movie that they picked
        print(f'You picked the movie {films[answer]}.')
    
    place = input("What place in your favorites list would you like to put it?")
    # [x] D. Move the movie to the new position
    new_place = int(place)
    films.insert(new_place, films[answer])
    del films[int(user)]
    
    # [x] E. Print the list again in order with numbers next to each movie
    for i, item in enumerate(films, 1):
        print(i, item)



"""""""""We need to ask:
    What place would you like to move a movie in your favorites list? Input movie number, Place on user List
        ex. (4, 1) fourth movie in 1st spot... Needs to iterate through list...user input(Are you finished with list?)
        ex. if yes then print list, if no then Continue"""



# alternate, but worse, way
# # remove the selected film from the films list
# fav_film = films.pop(answer)

# # go through the rest of the films and add them to the
# # to the fav_films list
# for film in films:
#     fav_films.append(film)





# Runner
film_review()
