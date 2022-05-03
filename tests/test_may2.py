import may2
from may2 import add, subt, hello, subtotal

# GIVEN: the prerequisites to running your test, such as the data
# WHEN: you run the code you want to test
# THEN: what the results should be

# simple tests with returned values
def test_add():
    result = add(200,22)
    assert result == 222

def test_subt():
    result = subt(999, 222)
    assert result == 777

# testing a function that prints stuff, you have to use the capsys fixture
def test_hello(capsys):
    # GIVEN: nothing in particular

    # WHEN: we call the hello() function
    hello()

    # THEN: the text "hello" should be printed with a newline
    output = capsys.readouterr().out
    assert output == f"hello\n"

# tests that require setup data
def test_subtotal():
    # GIVEN: that there is a "ice cream" item on the menu with a price of 100
    fake_item = {"name": "Rocky Road", "price": 100}
    may2.MENU["ice cream"] = fake_item

    # WHEN: you call the subtotal function with the args "ice cream" and 3
    result = subtotal("ice cream", 3)

    # THEN: result should be 300
    assert result == 300

def test_subtotal_ismissing():
    # GIVEN: that there is no "ricearoni" key in the MENU
    may2.MENU = {}

    # WHEN: You call subtotal() with the "ricearoni" key
    result = subtotal("ricearoni", 5)

    # THEN: the result should be zero
    assert result == 0
