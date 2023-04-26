from copy import deepcopy

from doctest import OutputChecker
from unittest import result

import pytest
# import pdbr

import adventure

from adventure import (
    PLAYER,
    WIDTH,
    MARGIN,
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
    do_buy,
    do_read,
    wrap,
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

# Testing for when an instance of an item exists in inventory
def test_player_has():
    # GIVEN: player has item in inventory
    adventure.PLAYER["inventory"]["purse"] = 1

    # WHEN: we call to ask if they have the item
    result = player_has("purse")

    # THEN: it will return true 
    assert result == True

# Testing for when there is 0 in inventory
def test_player_has_0():
    # GIVEN: player has no item in inventory
    adventure.PLAYER["inventory"]["kitten"] = 0

    # WHEN: we call to ask if they have an item
    result = player_has("kitten")

    # THEN: it will return False
    assert result == False

# Testing for when no key is given when fncn called
def test_player_no_key():
    # GIVEN: key nonexistent in inventory
    adventure.PLAYER["inventory"] = {}

    # WHEN: we call to ask for the key
    result = player_has("feet")

    # THEN: it will return False
    assert result == False

# Testing for when Player has multiple items in inventory
def test_player_has_mult_items():
    # GIVEN: Player has multiple items in inventory
    adventure.PLAYER["inventory"] = {}
    adventure.PLAYER["inventory"]["piggy"] = 5
    adventure.PLAYER["inventory"]["puppy"] = 1

    # WHEN: We call if Player has any item there
    result = player_has("piggy")
    
    # THEN: it will return True
    assert result == True

# test player_has for inventory discrepancy comparing inv to called fncn
def test_player_has_more():
    # GIVEN: Player has gems in inventory
    adventure.PLAYER["inventory"]["gems"] = 5

    # AND: Qty is less than gems in inventory
    qty = 6
   
    # WHEN: Player_has fncn called with qty 
    result = player_has("gems", qty)
   
    # THEN: it will return false
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
    # what_the_function_returned = do_take(list_of_what_the_player_typed)
    what_the_player_saw = capsys.readouterr().out
    # breakpoint()
    
    # THEN: It is not added to player inventory
    assert "duck" not in adventure.PLAYER["inventory"]
    
    # AND: It is not removed from the place
    assert "duck" not in adventure.PLACES["somewhere"]["items"]

    # AND: The fncn tells you what happened 
    assert "I don't see duck" in what_the_player_saw

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

def test_do_drop_no_args(capsys):
    # GIVEN: Player has inventory
    adventure.PLAYER["inventory"] = {"kitten":3}

    # AND: Player is in location
    adventure.PLAYER["place"] = "library"

    # WHEN: do_drop called w/o arg
    do_drop([])
    output = capsys.readouterr().out

    # THEN: Error is raised
    assert "What you wanna drop" in output


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
    adventure.ITEMS["cat"] = {"key": "cat", "name": "korg", "summary": "cute lil kitty-cat", "price": -15}
    
    # AND: There are also items not for sale
    adventure.ITEMS["rat"] = {"key": "rat", "name": "ronnie", "summary": "ugly plague beast"}

    # AND: The both those items are in the same location as the Player, That place has 'shop' action 
    adventure.PLACES["somewhere"] = {"items": ["cat", "rat"], "can": ["shop",]}

    # AND: There is an item for sale that is not in that location
    adventure.ITEMS["worm"] = {"key": "worm", "name": "wermhat", "summary": "wiggly worm", "price": -1}
  
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


# do_buy with no args
def test_do_buy_no_args(capsys):
    # GIVEN: Player is in location
    adventure.PLAYER["place"] = "somewhere"

    # WHEN: Player attempts to buy w/o arg
    do_buy([])
    output = capsys.readouterr().out
    # 
    # breakpoint()
    # THEN: It should fail and player should get an error
    assert "get out" in output 

# do_buy with wrong location
def test_do_buy_wrong_place(capsys):
    # GIVEN: Player is in a place
    adventure.PLAYER["place"] = "somewhere"

    # AND: Place has no buy property
    adventure.PLACES["somewhere"] = {"can": []}

    # WHEN: Player attempts to buy
    do_buy(["hat"])
    output = capsys.readouterr().out
    # breakpoint()
    # THEN: It should print an error
    assert "Go to a real store" in output

# do_buy with item not for sale
def test_do_buy_item_no_buy_prop(capsys):
    # GIVEN: Player is in an appropriate place
    adventure.PLAYER["place"] = "bodega"

    # AND: Location has buy property
    adventure.PLACES["bodega"] = {"can": ["buy",], "items": ["dumpster fire", "politicians"]}
    
    # AND: Player has gems
    adventure.PLAYER["inventory"] = {'gems': 50},

    # AND: A given item is not for sale
    adventure.ITEMS["dumpster fire"] = {"key": "dumpster fire", "name": "Politics", "description": "real real bad"}
  
    # WHEN: Player attempts to buy
    do_buy(["dumpster fire"])
    output = capsys.readouterr().out

    # THEN: An error should be printed
    assert "Not for sale to a hobbit like you!" in output

# do_buy with non-existant item
def test_do_buy_item_not_exist(capsys):
    # GIVEN: Player is in an appropriate place
    adventure.PLAYER["place"] = "bodega"

    # AND: Location has buy property
    adventure.PLACES["bodega"] = {"can": ["buy",], "items": ["kit", "caboodle"]}
    
    # AND: Player has gems
    adventure.PLAYER["inventory"] = {'gems': 50},

    # WHEN: Player attempts to buy an item not listed in code
    do_buy(["elephant"])
    output = capsys.readouterr().out

    # THEN: An error should be printed
    assert "I'm not a conjurer of cheap tricks!" in output

# do_buy with item that can be bought, not at location
def test_do_buy_item_not_here(capsys):
    # GIVEN: Player is in an appropriate place
    adventure.PLAYER["place"] = "pawn shop"

    # AND: Location has buy property
    adventure.PLACES["pawn shop"] = {"can": ["buy",], "items": ["ugly shoes", "broken bells"]}
    
    # AND: Player has gems
    adventure.PLAYER["inventory"] = {'gems': 50},

    # AND: There exists an item that has buy in a different location
    adventure.ITEMS["big guitar"] = {"key": "big guitar", "name": "Dusty the Stratocaster", "description": "6 strings, no blings", "price": -10}
    
    # WHEN: Player attempts to buy that item
    do_buy(['big guitar'])
    output = capsys.readouterr().out
    
    # THEN: An error should be printed 
    assert "Beat it" in output

# do_buy with correct location/item but no gems
def test_do_buy_no_gems(capsys):
    # GIVEN: Player is at appropriate place
    adventure.PLAYER["place"] = "store"

    # AND: Location has buy property
    adventure.PLACES["store"] = {"can": ["buy",], "items": ["pickled ginger", "gabagool", "coyote snout"]}

    # AND: Item exists that can be bought in location
    adventure.ITEMS["gabagool"] = {"key": "gabagool", "name": "yabba gabagool", "description": "yummy curing meat", "price": -20}

    # AND: Player doesn't have enough gems
    adventure.PLAYER["inventory"] = {"gems": 5}

    # WHEN: Player attempts to buy item
    do_buy(["gabagool"])
    output = capsys.readouterr().out

    # THEN: An error should be printed
    assert "Get a Job" in output

# do_buy with correct location/item/gems
def test_do_buy_all_correct(capsys):
    # GIVEN: Player is at appropriate location
    adventure.PLAYER["place"] = "store"

    # AND: Location has buy property
    adventure.PLACES["store"] = {"can": ["buy",], "items": ["time machine", "coffee machine", "ex machina"]}

    # AND: Item exists tha can be bought in location
    adventure.ITEMS["time machine"] = {"key": "time machine", "name": "Delorean", "description": "TIME IS ALIVE", "price": -10}

    # AND: Player has enough gems
    adventure.PLAYER["inventory"] = {"gems": 30}

    # WHEN: Player attempts to buy item
    do_buy(["time machine"])
    output = capsys.readouterr().out

    # THEN: No error raised
    assert "Let's get you all sorted then" in output
    
    # AND: The item is put into player inventory
    assert "time machine" in adventure.PLAYER["inventory"]

    # AND: Gems should be deducted from player inventory
    assert adventure.PLAYER["inventory"]

    # AND: Item should be removed from location
    assert "time machine" not in adventure.PLACES["store"]


# inv_ch adding 1 to item already in inv
def test_inventory_change_plus():
    # GIVEN: Player has item in inventory
    adventure.PLAYER["inventory"] = {"shoes": 5}

    # WHEN: Inv_ch called with an item/int
    inventory_change("shoes", 1)

    # THEN: Item in Player Inv qty should increase by one
    assert adventure.PLAYER["inventory"]["shoes"] > 5

# inv_ch w/o second arg
def test_inventory_change_no_second():
    # GIVEN: Player has inventory
    adventure.PLAYER["inventory"] = {"candy": 11}

    # WHEN: Inv_ch called with item but w/o qty
    inventory_change("candy")

    # THEN: Inventory will increase by 1
    assert adventure.PLAYER["inventory"]["candy"] == 12

# inv_ch key not in dict
def test_inventory_change_missing_key():
    # GIVEN: Player has inventory
    adventure.PLAYER["inventory"] = {}

    # WHEN: Inv_ch called w/o key
    inventory_change("almonds")

    # THEN: An error will be raised
    assert adventure.PLAYER["inventory"]["almonds"] == 1
    
# inv_ch w/ negative num
def test_inventory_change_neg():
    # GIVEN: Player has inv
    adventure.PLAYER["inventory"] = {"cookies": 13}

    # WHEN: Inv_ch called with negative num
    inventory_change("cookies", -3)

    # THEN: Qty in inv is reduced
    assert adventure.PLAYER["inventory"]["cookies"] == 10
    
# inv_ch removal
def test_inventory_change_removal():
    # GIVEN: Player has item in inventory 
    adventure.PLAYER["inventory"] = {"brownies": 4}

    # WHEN: inv_ch called on all units
    inventory_change("brownies", -4)

    # THEN: Item will not be shown
    assert "brownies" not in adventure.PLAYER["inventory"]

# do_read w/ empty list
def test_do_read_no_args(capsys):
    # GIVEN: None

    # WHEN: An empty list is passed
    do_read([])
    output = capsys.readouterr().out

    # THEN: The fncn runs
    assert "Trying to read" in output

    # AND: An error should be printed
    assert "What are you trying to read" in output

# do_read w/ missing item
def test_do_read_missing_item(capsys):
    # GIVEN: None


    # WHEN: An arg is passed that isn't not an item key
    do_read(["boring memoir"])
    output = capsys.readouterr().out

    # THEN: Then fncn runs its debug
    assert "Trying to read" in output

    # AND: An error is raised 
    assert "Sorry, chum" in output

# do_read w/ unreadable item
def test_do_read_unreadable_item(capsys):
    # GIVEN: Player is in place
    adventure.PLACES["Canada"] = {"key": "Canada","name": "Still Canada", "items": []}
    
    adventure.PLAYER["place"] = "Canada"

    # AND: An item is unreadable
    adventure.ITEMS["fake item"] = {"key": "fake", "name": "fake item"}

    # AND: Item is in current place
    place_add("fake item")

    # WHEN: Player tries to read item
    do_read(["fake item"])
    output = capsys.readouterr().out

    # THEN: An error should be printed
    assert "I really can't read" in output

# do_read in place
def test_do_read_in_place(capsys):
    # GIVEN: Player is in place
    adventure.PLACES["California"] = {"key": "California","name": "SF", "items": []}
    
    adventure.PLAYER["place"] = "California"

    # AND: Items have titles and messages 
    adventure.ITEMS ={"brochure": {"key": "brochure", "name": "adverts", "title": "Reasons to Revolt", "message": "It's better than fighting dragons"},
                      "magazine": {"key": "mag", "name": "Cosmo", "title": "Eating Healthy", "message": "Devour the Aristocracy"}, 
                      "dissertation": {"key":"dissertation", "name":"diss track", "title": "Monarchs Suck", "message": "Yup it does"}
                        }
    # AND: An item is in current place
    place_add("brochure")

    # WHEN: Player tries to read item
    do_read(["brochure"])
    output = capsys.readouterr().out

    # THEN: The title should be in output
    # breakpoint()
    assert "Reasons" in output

    # AND: The message should be in output
    assert "better than" in output

# do_read of player inv if it isn't in a place
def test_do_read_in_inventory(capsys):
    # GIVEN: Player is in place
    adventure.PLACES["California"] = {"key": "California","name": "SF", "items": []}
    
    adventure.PLAYER["place"] = "California"
    
    # AND: Player has item in inv that is not in place that can be read
    adventure.ITEMS["comics"] = {"key": "comics", "name": "Batman Issue 2", "title": "Full of Bats", "message": "Please don't eat Bats!"}
    
    adventure.PLAYER["inventory"] = {}

    inventory_change("comics")

    # WHEN: Player tries to read item
    do_read(["comics"])

    output = capsys.readouterr().out

    lines = output.splitlines()

    # THEN: Title should be in output
    assert "Full of Bats" in output

    # AND: Message should be in output
    assert "don't eat" in output

    # AND: Last item in lines = item message
    assert lines[-1] == "        Please don't eat Bats!"

# wrap test to make sure it works correctly w/ regards to gl.width
def test_wrap(capsys):
    # GIVEN: 

    # WHEN: We try to wrap around a string longer than WIDTH
    # breakpoint()
    wrap("Bingo " * WIDTH)

    output = capsys.readouterr().out

    lines = output.splitlines()

    # THEN: 'Lines' is more than 1
    assert len(lines) > 1

    # AND: Output has first few words of str
    assert "  Bingo" in output

    # AND: Output ends with last few string words, followed by new line
    assert output.endswith("Bingo\n")

    # AND: Each str in lines starts w 2 spaces
    assert str(lines[2]).startswith("  ")

# wrap test to make sure things are wrong with extra indent. FAILING TEST
def test_wrap_with_indent(capsys):
    # GIVEN:

    # WHEN: We try to wrap with a indent = 2
    # breakpoint()
    wrap("Humdinger" * WIDTH, 2)
    
    output = capsys.readouterr().out

    lines = output.splitlines()
    
    # THEN: "lines" is more than 1
    assert len(lines) > 1

    # AND: Each str starts with 8 spaces
    assert lines[0].startswith("        Humdinger")
    ...
