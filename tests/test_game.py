from copy import deepcopy

import pytest
# import pdbr

import adventure

from adventure import get_place, error, debug, header, write

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
def test_get_place():
    fake_place = {"name": "something"}
    adventure.PLACES["something"] = fake_place
    result = get_place("something")
    assert not result == fake_place

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
