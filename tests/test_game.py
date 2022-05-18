from ast import arg
from copy import deepcopy

import pytest
# import pdbr

import adventure

from adventure import PLAYER, do_examine, get_place, error, debug, header, write, get_item, player_has, current_place_has, do_take, do_examine

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
    with pytest.raises(SystemExit):
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
    # adventure.ITEMS["duck"] = {"name":"duck", "can_take": True}

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

def test_do_examine_with_item(capsys):
    # GIVEN: The player is in a place where there is an item that can be examined
    adventure.PLAYER["place"] = "somewhere"
    # breakpoint()
    adventure.ITEMS["duck"] = {"name": "duck", "description": "It's just a duck, bucko"}
    adventure.PLACES["somewhere"] = {"items": ["duck"]}

    # WHEN: The player attempts to examine it     
    do_examine(["duck"])
    output = capsys.readouterr().out

    # THEN: Item desc. is returned
    assert "just a duck, bucko" in output

# WRITE test to test what happens when the item is missing from above
