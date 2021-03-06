def hip():
    """We're printing out hip hip hooray 3 times"""
    i = 0
    while i<3:
        print("Hip hip hooray!")
        i += 1

def game_score():
    """In this code we're writing a scoreboard for a game with 3 rounds"""
    i = 1
    while i <= 3:
        print("Round:", i)
        n = 1
        while n <= 3:
            print("Player", n, "score: ____________")
            n += 1
        i += 1
        
game_score()
