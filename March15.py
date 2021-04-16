

# functions

def main():
    fh = open("data/contacts.txt")
    contents = fh.read()
    fh.close()
    print(contents)

def greet():
    greetings = ["hello mello yello", "bonjour", "love ya heyo"]
    fh = open("data/greetings.txt", "w")
    for item in greetings:
        fh.write(f"{item}\n")
    fh.close()
    print("I'm such a cutie-pie")

def reply():
    replies = ["go home, nerd", "please stop talking to me", "SILENCE", "Oh hi MARK"]
    fh = open("data/greetings.txt", "a")
    for item in replies:
        fh.write(f"{item}\n")
    fh.close()
    print("GET in MY BELLY")

def spite_words():
    spite = "Donkey Tots"
    fh = open("../project_trello/spite.txt", "w")
    fh.write(spite)
    fh.close()
    print("Party Factory")

# script runner

# main()
# greet()
# reply()
# spite_words()
