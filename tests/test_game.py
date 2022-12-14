from copy import deepcopy
from doctest import OutputChecker
from unittest import result

import pytest
# import pdbr

import adventure

from adventure import (
    PLAYER,
    do_examine,
    get_place,
    do_shop,
    error,
    debug,
    header,
    is_for_sale,
    write,
    get_item,
    player_has,
    current_place_has,
    do_take,
    do_examine,
    do_drop,
    is_for_sale,
    inventory_change,
    place_add,
    place_remove,
    place_can, 
)

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

    # THEN: Item desc. is printed
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
def test_do_examine_not_place_not_inventory(capsys):
    # GIVEN: A player is in a location
    adventure.PLAYER["place"] = "somewhere"

    # AND: That place doesn't have an item
    adventure.PLACES["somewhere"] = {"items": []}

    # AND: The item is not in player inventory
    adventure.PLAYER["inventory"] = {"duck": 0,}

    # WHEN: The player tries to examine an item
    do_examine(["duck"])
    output = capsys.readouterr().out

    # THEN: It returns an error
    assert "idk what this is" in output


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



def test_is_for_sale(capsys):
    # GIVEN: An item has the key/value "price"
    adventure.ITEMS["doggy"] = {"key": "doggy", "name": "Pupperoni", 
        "description": "One with waggly tail", 
        "price": 25}

    # WHEN: A player checks if an item is for sale
    result = is_for_sale("doggy")

    # THEN: Output returns true
    assert result == True

def test_is_not_for_sale():
    # GIVEN: An item does not have the key/value "price"
    adventure.ITEMS["doggy"] = {
        "key": "doggy",
        "name": "Pupperoni",
        "description": "One with waggly tail",
    }

    # WHEN: A player checks if it's for sale
    result = is_for_sale("doggy")

    # THEN: It returns false
    assert result == False

def test_place_add_player_has():
    # GIVEN: A Player is at a place with an items key
    adventure.PLAYER["place"] = "somewhere"
    adventure.PLACES["somewhere"] = {"items": []}

    # WHEN: Place_add is called with item key
    place_add("fox")

    # THEN: The item is added to current place items
    assert "fox" in adventure.PLACES["somewhere"]["items"]

def test_place_add_when_no_items_key():
    # GIVEN: A place has no 'items' key 
    adventure.PLAYER["place"] = "somewhere"
    adventure.PLACES["somewhere"] = {}

    # WHEN: Place_add is called on that place
    place_add("grey fox")

    # THEN: Items key is created with added item in there
    assert "grey fox" in adventure.PLACES["somewhere"]["items"]

def test_place_add_when_already_there():
    # GIVEN: A place has an item and an items key
    adventure.PLAYER["place"] = "somewhere"
    adventure.PLACES["somewhere"] = {"items": ["pink fox"]}

    # WHEN: Place_add is called on the place
    place_add("pink fox")

    # THEN: The item is not duplicated in items list
    assert adventure.PLACES["somewhere"]["items"].count("pink fox") == 1
    # x = [1, 2, 1, 2, 3]
    # x.count(1)           # return 2
    # x.count(3)           # return 1
    # x.count(5)           # return 0
 
def test_place_remove_with_item():
    # GIVEN: An item is in current place
    adventure.PLAYER["place"] = "somewhere"
    adventure.PLACES["somewhere"] = {"items": ["gold owl"]}

    # WHEN: Item is removed from that location
    place_remove("gold owl")

    # THEN: Item is removed(popped) from the place item list
    assert "gold owl" not in adventure.PLACES["somewhere"]["items"]
    ...

def test_place_remove_without_item():
    # GIVEN: There is no item in current place
    adventure.PLAYER["place"] = "somewhere"
    adventure.PLACES["somewhere"] = {"items": []}

    # WHEN: Item is removed from location
    place_remove("silver owl")

    # THEN: No error is raised
    assert True, "No error is raised"

def test_place_remove_no_item_key():
    # GIVEN: There is no item key in a location
    adventure.PLAYER["place"] = "somewhere"
    adventure.PLACES["somewhere"] = {}

    # WHEN: Item is removed
    place_remove("bronze owl")

    # THEN: No error is raised
    assert True, "No error is raised"
    ...

def test_do_shop(capsys):
    # GIVEN: A Player is in a location
    adventure.PLAYER["place"] = "somewhere"
    
    # AND: There are items for sale
    adventure.ITEMS["cat"] = {"key": "cat", "name": "korg", "description": "cute lil kitty-cat", "price": -15}
    
    # AND: There are also items not for sale
    adventure.ITEMS["rat"] = {"key": "rat", "name": "ronnie", "description": "ugly plague beast"}

    # AND: The both those items are in the same location as the Player, That place has 'shop' action 
    adventure.PLACES["somewhere"] = {"items": ["cat", "rat"], "can": ["shop",]}

    # AND: There is an item for sale that is not in that location
    adventure.ITEMS["worm"] = {"key": "worm", "name": "wermhat", "description": "wiggly worm", "price": -1}
  
    # WHEN: do_shop is called
    do_shop()
    output = capsys.readouterr().out

    # THEN: Items for sale are printed
    assert "lil kitty-cat" in output

    # AND: Items not for sale aren't listed
    assert "ronnie" not in output
    
    # AND: Items not in location are not listed
    assert "wermhat" not in output

def test_place_can():
    # GIVEN: A Place has values for the 'can' key 
    adventure.PLACES["somewhere"] = {"can": ["sleep"]}

    # AND: Player is in that place
    adventure.PLAYER["place"] = "somewhere"

    # WHEN: Place_can is called on a value
    ability = place_can("sleep")

    # THEN: The action is returned as truthy
    assert ability
    ...
