"""Goal for today is to: Make a script to keep track of contacts.

1. Ask the user for the name and phone number
2. Add the name and phone number to a file named data/contacts.txt.

Reminders:
1. Don't forget to close the file or use a with statement or changes will not be saved!
2. Don't forget to add a \n at the end of every line."""


# goals:
# [x] rename contact_book to add_contact
# [x] add a docstring to the the add_contact function
# [x] start part 2
    # [x] ask user if they want to list or add contacts
    # [x] if they want to then do above
    # [x] if they want a list then open data/contacts.txt and print every line
# [x] move reading the file to get_contacts()
    # [x] make another function called get_contacts
    # [x] move the parts of main() that read data/contacts.txt to that function
    # [x] add a docstring to the get_contacts() function
    # [x] have it return the contents as a string
    # [x] call get_contacts() from main then print the returned string
# [ ] Part 3: Search contacts
    # [x] 1. Now ask the user if they want to list, add, or search contacts.
    # [x] 2. If the user chooses search, then ask them what they want to search for.
    # [ ] 3. Open the file and loop through each line. If the line contains the text that they entered, print the line.
    #      Hint: use the in operator.
    # Bonus:
    # [ ] 4. If nothing was found, print a message that no matching contacts were found.
    # [ ] 5. Make the search cases insensitive by changing both the user input and the line to lower case.

    
def contact_book(contact, phone_number):
    """so this is passing our arguments, setting the stage for adding contacts in the main"""
    fh = open("data/contacts.txt", "a")
    fh.write(f"{contact}: {phone_number} \n")
    fh.close()

def get_contacts():
    """this function is to grab and print our contact list so we don't have to in main"""
    fh = open("./data/contacts.txt")
    contents = fh.read()
    fh.close()
    print("My heart is a black hole :(")
    return contents

def search_contacts():
     """Plan is to have user input a name and then return a name or number...need to use the -in- """
     answer = input("What do you want to search for: Name or Number")
        
def main():
    """ask for user input on action (add or print) then respond"""
    question = input("Wanna add, search, or print contact list (no answer shows the world)?: ")
    if question == "add":
        contact = input("Your name is: ")
        phone_number = input("Your number is: ")
        contact_book(contact, phone_number)   
    elif question == "print": 
        contacts = get_contacts()
        print(contacts)
    else question == "search":
        search = search_contacts()

# contact_book()
# main()


