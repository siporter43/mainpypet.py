# Short descr. of script

"""the plan is to write a fncn that will return a letter grade when given a number"""



def main():
  
    #Step 2: Create a part where user inputs their number...
    print("what is the number grade you have, between 1 and 100?")
    grade_num = input(":")
    
    #Step 3: Then make fncn determine if the number is valid. (Make a fncn that take a number and returns a letter)
    grade_letter = return_grade(grade_num)
    print(grade_letter)
    
    print("Jimmy Woo")

def return_grade(number):
    print("The number grade is", number)
    
    #Step: So I think we'll need to set a dictionary of letters and their number range...restrict to between 0-100 and A,B,C,D,F
    letters = { (0, 55): "F", (56, 69): "D", (70, 79): "C", (80, 89): "B", (90, 100): "A"}

    #3A: If the number is valid then go ahead and search for the range in which that number lies
    for grade_range, grade in letters.items():
        #3A1: Check which letter is included in that number range. 
        number = int(number)
        if number >= grade_range[0] and  number <= grade_range[1]:
            return grade

    
    # ex. 92 < 55: false,...92<69: false...92<79:false
    #3B: Else, If the number is not in the range, return an error and ask them to input a new number (This would be a loop)
    

#Step 4: The fncn will combine the given info to print a message with the letter grade, number, and phrase of praise
    #4A: Create an f-string like "you chose", user_number, "that means your grade is" corresp_letter, "good enough"


#Imports##########################

# Global Variables#####################

# Functions###############################

main()
