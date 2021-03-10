from project_trello.feb9_testing import letter_grade
from project_trello.feb9_testing import endgame

def test_endgame():
    print("running tests for the endgame() function")
    assert endgame(True) == "Congratulations, you won!"


def test_letter_grade():
    print("Jimmy Woo")
    assert letter_grade(1) == "F", "number scores bw 0-59 should return F"
    assert letter_grade(69) == "D", "number scores bw 60-69 should return D"
    assert letter_grade(70) == "C", "number scores bw 70-79 should return C"
    assert letter_grade(81) == "B", "number scores bw 80-89 should return B"
    assert letter_grade(99) == "A", "number scores bw 90-100 should return A"
    assert letter_grade(110) == False, "number scores over 100 should return False"
    assert letter_grade(-5) == False, "number scores under 0 should return False"
    print("Eat the eating")

# test_letter_grade()

def test_letter_grade_fail():
    assert letter_grade(19) == "F", "number scores should be bw 0-59 and show an F"
    print("Robots aren't real")




# test_letter_grade_fail()
test_letter_grade()

# pytest tests/test_feb9_testing.py
