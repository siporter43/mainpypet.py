TODO
====

Misc
----


* [x] write a docstring and type annotations for the `is_for_sale()` function
* [x] write annotations and docstrings for 1-2 functions each coding session

Part 9.5
--------

* [x] Part 9.5:   Add `inventory_change()`
* [x]             Write `test_inventory_change()`  (should fail)
* [x]     9.5 A   Define `inventory_change()`
* [x]     9.5 B   Replace code in `do_take()` that modifies inventory with a call
                  to your new `inventory_change()` function
* [x]   (extra)   Write a test for `do_drop()` that should pass and reflect its
                  current behavior
* [x]     9.5 C   Replace code in `do_drop()` that modifies inventory with a call
                  to your new `inventory_change()` function
				  Make sure that the `test_do_drop()` test still passes.

Part 9.6
--------

* [ ]Part 9.6:     Add `place_add()`
* [x]              Write `test_place_add()` 
        [x] 9.6 A     Define `place_add(key) `
* [x]              Write `test_place_add_when_no_items_key()` 
                   (Should test when there is no "items" key in the current place dictionary)
* [x]              Modify place_add() to make above test pass 
* [x]              Write `test_place_add_when_already_there()`             
                   Should test when the `key` is already in the current place "items" list
* [x]              Modify place_add() to make above test pass 
                   [x] 9.6 B Call place_add() in do_drop()
* [x]              Find where you add the item to the place. Replace those lines with a call to place_add() and pass the name argument.
                   
* [x]              You can also remove the line where you get the current place using the get_place() function.
* [x]              write a test like: place_remove_without_items_key() 
                   place does not have the "items" key
* [x]              write a test like: place_remove_when_no_item()
                   when place does have the "items" key, but key is not in the list


Part 10
--------

* [-] Part 10.1       
* [ ] Do 10.1 A
* [ ] Write (passing) test for current behavior of do_shop()
      (Note: be sure to look at other do_*() tests to remember how it works.)
* [ ] Modify test (to fail)for new behavior:
* [ ] - instead of listing all for-sale items, only list for-sale items in the
        current place
* [ ] Modify do_shop() to pass modified test
* [-] Part 10.2
* [ ] Write (failing) test for new place_can() function that should:
* [ ] take one argument: action
* [ ] a place dict may now have a "can": []
* [ ] 
