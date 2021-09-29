"""This is our cool new project in which we'll create a text based adventure game :)
            https://alissa-huskey.github.io/python-class/exercises/adventure.html"""

# Part 1.2
    # [x] Define a main() function, and have it print "Welcome!"
    # [x] In main() make a while loop with the condition True.
    # [x] In the loop, call the input() function, with the prompt "> ". 
    # Assign the returned value to the variable reply.
    # [x] Outside of main(): Use an if statement to check if __name__ == "__main__".
    # [x] In the if statement, call main()

# Part 1.3
    # Make do_quit()
        # [x] Make a do_quit() function.
        # [x] In it, print "Goodbye."
        # [ ] Then call quit()
#     In main(), in the while loop:

# [ ] After getting reply, check if reply is equal to q or quit.
# [ ] If so, call do_quit()
# [ ] Otherwise, print a messsage like: "No such command." then continue

"""Imports"""



"""Global Variables"""



"""FNCNs"""

def main():
    print("Welcome!")
    while True:
        reply = input(">")

def check_main():
    if __name__ == "__main__":
        main()

def do_quit():
    print("Goodbye, nerd")
    quit()




"""Runner"""

# main()

check_main()
