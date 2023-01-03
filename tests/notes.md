# Notes

This document is in markdown. Here are some links for more information:

* [Cheatsheet](https://commonmark.org/help/)
* [Tutorial](https://commonmark.org/help/tutorial/)

## Testing

To run tests we use `pytest` at the command line.

```bash
pytest tests/test_name.py
```

## Troubleshooting

### `KeyError`

A `KeyError` happens when you try to use subscription to get a value from a
dictionary if the key does not exist.

```python
x = {"a": 1, "b": 2}

print(x["a"])           # will print 1
print(x["c"])           # will raise a KeyError
```

You can avoid this error by using the `.get()` method. If the key is not in the
dictionary, it will return `None` instead of raising an error.

```python
x = {"a": 1, "b": 2}

print(x.get("a"))           # will print 1
print(x.get("c"))           # will print None
```

You can pass a second argument to `.get()` to change the value that is returned
when a key is missing.

```python
x = {"a": 1, "b": 2}

print(x.get("a", 0))        # will print 1
print(x.get("c", 0))        # will print 0
```

This is especially handy if you do something with the value immediately.

```python
x = {"a": 1, "b": 2}

x.["c"] + 1              # will fail with a KeyError
x.get("c") + 1           # will fail with a TypeError (can't do None + 1)
x.get("c", 0) + 1        # will evaluate to 1
```

So when creating tests... MAKE SURE TO IMPORT THE FNCN

```

To test:
1. From terminal:
        pytest ....tests/test file



HOW to deal with things that aren't there, but could be there

Also, when attempting to create a new item instance you can use either "if" of
'setdefault'

if key not in PLAYER["inventory"]:
        PLAYER["inventory"][key] = 0
    
PLAYER["inventory"].setdefault(key, 0) # NOTE: same as below

if "items" not in place:
        place["items"] = []

Fncns like below were built as a way to not get TypeErrors and overall smoothen
how game runs get_item checks a key to see if it exists in ITEMS dict, abort
otherwise. This fncn is called in other fncns like do_shop in order to bypass
the need check if an item is there, while not having to code every time. In
do_shop this fncn is called so that subscription issues/type problems aren't run
into. AND IT RETURNS an item DICT

is_for_sale checks if there's a 'price' associated with the item. If no,
the falsy-ness moves it along. In do_shop this fncn is called to check
that property. True or False ending

in our "do"_ fncn tests we are trying to see what the user sees, not what's returned

IMPORTANT-- return stops stuff, does not print 
        also, output capsys shows us 
