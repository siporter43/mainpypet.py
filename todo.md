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
* [x] Write (passing) test for current behavior of do_shop()
      (Note: be sure to look at other do_*() tests to remember how it works.)
* [x] Modify test (to fail)for new behavior:
* [x] - instead of listing all for-sale items, only list for-sale items in the
        current place
* [ ] Modify do_shop() to pass modified test
* [x] Write notes for fncns get_items is_for_sale
* [-] Part 10.2
* [x] talk to Alissa before you move on
* [x] Write (failing) test for new place_can() function that should:
* [x] take one argument: action
* [x] a place dict may now have a "can": []
* [x] Get the current place by calling get_place() and assign it to the variable place
* [x] Check if action is not in the list of place items by calling .get() on place with the             key "can" and an empty list for the default argument.
        *[x] If so, return True
        *[x] Otherwise, return False

* [x] In do_shop() at the very beginning of the function check if shopping is supported in the current place by calling place_can() with the argument "shop".
* [x] If not, print an error message like Sorry, you can't action here. then return
* [-] Part 10.3
        Writing notes for each test in do_buy
       X 1. with no args
       X 2. with wrong location (no buy property)
       X 3. with right location, invalid item
       X 4. with invalid item (not an item in the game)
       X 5. with right location, item not at location
        X 6. with right location, right item, no gems
        
        X [Need to redo player_has tests, to test for qty prop...]
        X 7. with right location, right item, enough gems

[ ] Part 10.4: Clean up the shop
*       [ ] A. Show price in do_shop
                [x] Print item 'price' with desc and name, use abs() to make price positive
                [ ] Use string formatting to align into columns
