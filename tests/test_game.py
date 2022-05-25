from copy import deepcopy
from doctest import OutputChecker

import pytest
# import pdbr

import adventure

from adventure import PLAYER, do_examine, get_place, error, debug, header, write, get_item, player_has, current_place_has, do_take, do_examine, do_drop

PLAYER_STATE = deepcopy(adventure.PLAYER)
PLACES_STATE = deepcopy(adventure.PLACES)
ITEMS_STATE = deepcopy(adventure.ITEMS)


def revert():
    """Revert game data to its original state."""
    adventure.PLAYER = deepcopy(PLAYER_STATE)
    adventure.PLACES = deepcopy(PLACES_STATE)
    adventure.ITEMS = deepcopy(ITEMS_STATE)


@pytest.fixture(autouse=True)
def teardown(request):
    """Auto-add teardown method to all tests."""
    request.addfinalizer(revert)


def test_truth():
    assert True

# [x] import get_place from adventure
# [x] call get_place() with the fake place key and assign it to a variable like result
# [x] assert that result equals fake_place
# @pytest.mark.skip(reason="under construction")
def test_get_place():
    adventure.PLACES["somewhere"] = {"name": "left"}
    fake_place = get_place("somewhere")
    assert fake_place == {"name": "left"}, "We are error"

def test_error(capsys):
    error("IDK my bff Jill?")
    output = capsys.readouterr().out
    assert "IDK my bff Jill?" in output, "The formatted message shout be printed"

def test_debug(capsys):
    debug("What the f?")
    output= capsys.readouterr().out
    assert "What the f?" in output, "The formatted message shout be printed"

def test_header(capsys):
    header("I hope this is header")
    output= capsys.readouterr().out
    assert "I hope this is header" in output, "The formatted message shout be printed"

def test_write(capsys):
    write("No, YOU WRITE!")
    output= capsys.readouterr().out
    assert "No, YOU WRITE!" in output, "The formatted message shout be printed"

def test_get_item_missing_from_items():
    adventure.PLAYER["inventory"]["hats"] = 11
    with pytest.raises(SystemExit) as err:
        get_item("hats")

def test_get_item(capsys):
    adventure.ITEMS["hats"] = {"name": "cap"}
    item = get_item("hats")
    assert item == {"name": "cap"}, "Our errors shall be written"

def test_player_has():
    # GIVEN: player has item in inventory
    adventure.PLAYER["inventory"]["purse"] = 1

    # WHEN: we call to ask if they have the item
    result = player_has("purse")

    # THEN: it will return true 
    assert result == True

def test_player_has_0():
    # GIVEN: player has no item in inventory
    adventure.PLAYER["inventory"]["kitten"] = 0

    # WHEN: we call to ask if they have an item
    result = player_has("kitten")

    # THEN: it will return False
    assert result == False

def test_player_no_key():
    # GIVEN: key nonexistent in inventory
    adventure.PLAYER["inventory"] = {}

    # WHEN: we call to ask for the key
    result = player_has("feet")

    # THEN: it will return False
    assert result == False

def test_current_place_has():
    # GIVEN: if somewhere the player is in has a particular item
    adventure.PLAYER["place"] = "somewhere"
    adventure.PLACES["somewhere"] = {"items": ["dog"]}

    # WHEN: we call to ask if an item exists in that space
    result = current_place_has("dog")

    # THEN: it will return True
    assert result == True

def test_current_place_has_0():
    # GIVEN: if somewhere the player is in has no item
    adventure.PLAYER["place"] = "somewhere"
    adventure.PLACES["somewhere"] = {"items": []}

    # WHEN: we call to ask if an item exists in that space
    result = current_place_has("dog")

    # THEN: it will return False
    assert result == False

def test_current_place_has_no_item():
    # GIVEN: if somewhere the player is has no items key
    adventure.PLAYER["place"] = "somewhere"
    adventure.PLACES["somewhere"] = {"name": "somewhere"}

    # WHEN: we call to ask if an item exists in that space
    result = current_place_has("dog")

    # THEN: it will return True
    assert result == False

def test_do_take_with_item(capsys):
    # GIVEN: an item the player wants to take is in the current place
    adventure.PLAYER["place"] = "somewhere"
    adventure.PLACES["somewhere"] = {"items":["duck"]}

    # AND: that item is not in the players inventory
    adventure.PLAYER["inventory"] = {}

    # AND: the item exists and is takable
    adventure.ITEMS["duck"] = {"name":"duck", "can_take": True}

    # WHEN: When the player tries to take it
    do_take(["duck"])
    output = capsys.readouterr().out
    # breakpoint()
    
    # THEN: It is added to player inventory
    assert adventure.PLAYER["inventory"]["duck"] == 1
    
    # AND: It is removed from the place
    assert "duck" not in adventure.PLACES["somewhere"]["items"]

    # AND: The fncn tells you what happened 
    assert "You pick up the duck" in output

def test_do_take_without_item(capsys):
    # GIVEN: an item the player wants to take an item that isn't in the current place
    adventure.PLAYER["place"] = "somewhere"
    adventure.PLACES["somewhere"] = {"name": "somewhere", "items": []}

    # AND: that item is not in the players inventory
    adventure.PLAYER["inventory"] = {}

    # AND: the item exists and is takable
    adventure.ITEMS["duck"] = {"name":"duck", "can_take": True}

    # WHEN: When the player tries to take it
    do_take(["duck"])
    output = capsys.readouterr().out
    # breakpoint()
    
    # THEN: It is not added to player inventory
    assert "duck" not in adventure.PLAYER["inventory"]
    
    # AND: It is not removed from the place
    assert "duck" not in adventure.PLACES["somewhere"]["items"]

    # AND: The fncn tells you what happened 
    assert "I don't see duck" in output

# item IS in place and NOT in inventory
def test_do_examine_with_item(capsys):
    # GIVEN: The player is in a place where there is an item that can be examined
    adventure.PLAYER["place"] = "somewhere"
    # breakpoint()
    adventure.ITEMS["duck"] = {"name": "duck", "description": "It's just a duck, bucko"}
    adventure.PLACES["somewhere"] = {"items": ["duck"]}

    # AND: The item is not in player inventory
    adventure.PLAYER["inventory"] = {}

    # WHEN: The player attempts to examine it     
    do_examine(["duck"])
    output = capsys.readouterr().out

    # THEN: Item desc. is returned
    assert "just a duck, bucko" in output


# NOT in inventory, NOT in place
def test_do_examine_no_location_item(capsys):
    # GIVEN: The player is in a location
    adventure.PLAYER["place"] = "somewhere"

    # AND: The object is not in that place
    adventure.PLACES["somewhere"] = {"items": []}

    # AND: Item is not in player item inventory
    adventure.PLAYER["inventory"] = {}

    # WHEN: The player tries to examine the object
    do_examine(["duck"])
    output = capsys.readouterr().out

    # THEN: An error message is returned
    assert "idk what this is: duck" in output

# TODO: IS in inventory, NOT in place
def test_do_examine_not_place_in_inventory(capsys):
    # GIVEN: A player is in a location
    adventure.PLAYER["place"] = "somewhere"

    # AND: That place doesn't have an item
    adventure.PLACES["somewhere"] = {"items": []}

    # AND: The item is in player inventory
    adventure.PLAYER["inventory"] = {"duck": 1,}

    # AND: The item has a description
    adventure.ITEMS["duck"] = {"name": "Ducky", "description": "An air monster with beak"}

    # WHEN: The player tries to examine the item
    do_examine(["duck"])
    output = capsys.readouterr().out

    # THEN: It prints item description
    assert "air monster" in output

# TODO: NOT in inventory, NOT in place
#       (but lower priority)

def test_do_drop_player_has(capsys):
    # GIVEN: A player has an item in inventory
    adventure.PLAYER["inventory"]["kitten"] = 1
    
    # AND: A player is in a place 
    adventure.PLAYER["place"] = "somewhere"
    
    # AND: The place currently does not have the item
    adventure.PLACES["somewhere"] = {"name": "somewhere", "items": []}

    # WHEN: A player tries to drop that item
    do_drop(["kitten"])
    output = capsys.readouterr().out
    # breakpoint()

    # THEN: We tell user their item is dropped
    assert "gently toss" in output

    # AND: Item is dropped in location
    assert "kitten" in adventure.PLACES["somewhere"]["items"]

    # AND: Item is no longer in player inventory
    assert "kitten" not in adventure.PLAYER["inventory"]

def test_do_drop_player_has_not(capsys):
    # GIVEN: A player does not have an item in inventory
    adventure.PLAYER["inventory"]["kitty"] = 0 

    # AND: A player is in a place
    adventure.PLAYER["place"] = "somewhere"

    # WHEN: A player tries to drop an item
    do_drop(["kitty"])
    output = capsys.readouterr().out

    # THEN: An error is returned
    assert "don't have any kitty" in output
