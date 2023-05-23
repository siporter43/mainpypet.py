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
* [x] Do 10.1 A
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
* [x] Part 10.3
        Writing notes for each test in do_buy
       X 1. with no args
       X 2. with wrong location (no buy property)
       X 3. with right location, invalid item
       X 4. with invalid item (not an item in the game)
       X 5. with right location, item not at location
        X 6. with right location, right item, no gems
        
        X [Need to redo player_has tests, to test for qty prop...]
        X 7. with right location, right item, enough gems

* [x] Part 10.4: Clean up the shop
       [x] A. Show price in do_shop
                [x] Print item 'price' with desc and name, use abs() to make price positive
                [x] Use string formatting to align into columns
        [x] B. Handle long desc.
                [x] in 'for' loop call textwrap.shorten() with 2 args
                item desc and desired max width ->Assign to desc var
                [x] in write fncn replace --- with desc (see above)
        [x] B,2. Add short summary items in dict
                [x] In each dict in ITEMS add a key 'summary' with one line descr
                [x] in do_shop replace item[desc] with item[summary]
        [x] C. Show price in do_examine
                [x] In do_shop check if: 
                        [x]place supports 'shop'
                        [x]place has item with place_has
                        [x]item is for sale by calling is_for_sale
                [x] Print price
        [x] D. Show inventory quant in do_examine
                [x]Check if player has item in inv. using player_has with -name-
                [x] Print quant from Player inv dict for -name-

* [x] Part 11: Tests, More

        [x] 11.6 Test inventory_change()
                [x] A. Add teardown
                [x] B. Write test_inventory_change()
                        [x] Import inventory_change fncn
                        [x] Add a test_inv_ch fncn
                        [x] Add key with qty
                        [x] Call inv_ch with key value
                        [x] Assert statement that checks addition of inv
                        [x] Run test
        [x] 11.7 Test do_drop()
                [x] A. Write test_do_drop_no_args
                [x] B. Write test_do_drop_missing_item

Part 12: Read Things
-------
* [x] Part 12.1 Add command
        [x] A. In test_game.py
                [x] Import do_read fncn
                [x] Add test_do_read() with parameter capsys
                [x] Call do_read with empty list as arg
                [x] Write assert statement that checks debug message 
                [x] Run test to get error
        [x] B. add do_read to adventure.py
        [x] C. in main()
                [x] Add elif for do_read
* [x] Part 12.2 Ensure item
        [x] A. in test_game.py
                [x] Change test name
                [x] Add assertion that checks for error
                [x] Run test. Should fail
        [x] B. in adv.py in do_read
                [x] Check if args is falsy, print error if so
                [x] Run test to pass
* [x] Part 12.3 Ensure item is there
        [x] A. in test_game.py
                [x] Add test_do_read_missing_item() with param capsys
                [x] Call do_read with a list and any str that's not an item key for an arg
                [x] Assign capsys... to output
                [x] Write an assert statement checking debug message
                [x] Write an assert that checks "Sorry, I don't know what this is" in output
                [x] Run failing test
        [x] B. In adv.py in do_read
                [x] Assign first item of args list to a var name with lower
                [x] Write an if statement that checks if player or place has item:
                        [x] Use error() to print message like "Sorry idk what args is"
                        [x] return
                [x] Run the passing test
* [x] Part 12.4 Ensure item is readable
        [x] A. In test_game.py write test_do_unreadable_item()
                [x] Add a fake unreadable item to current place.. needs to be empty dict
                [x] Call do_read w/ args 'read <fake thing> '
                [x] Check the output for error
                        [x] import place_add
                        [x] add test_do_unreadable_item() w/ capsys
                        [x] Add fake item to adv.ITEMs with a key
                        [x] Use place_add to add fake item to current place
                        [x] Call do_read w/ a list containing new key as the arg
                        [x] capsys to output
                        [x] Write assert that checks message 'I can't read key'
                        [x] Run failing test
        [x] READ https://alissa-huskey.github.io/python-class/practices/testing/pytest-tests.html#part-1-3-reading-test-output
        [x] B. In adv.py in do_read()
                [x] 1. Use get_item to get item from dict and assign to var. item
                [x] 2. Check if the 'message' key in dict. If not
                        [x] Use error() to print 'I can't read'
                        [x] return
                [x] 3. Run passing test
* [x] Part 12.5 Read things
        [x] A. In test_game.py write test_do_read_in_place
                [x] 1. Add test 
                [x] 2. Create dict repr fake item with keys: title and message
                [x] 3. Use place_add to add item to place
                [x] 4. Call do_read on item
                [x] 5. Assign capsys
                [x] 6. Write an assert that title is in output
                [x] 7. Write an assert that message is in output
                [x] 8. Run failing test
        [x] B. In adv.py in do_read
                [x] 1. If "title" key exists in the item dict,use header fncn to print. 
                        Otherwise print "It reads..."
                [x] 2. Use wrap fncn to print "message" from item dict
        [x] C. Modify ITEMS: add to 'book'
                [x] 1. Add key 'title' to book
                [x] 2. Add 'message' to book
        [x] D. In test.py define test_do_read_in_inv
* [x] Part 12.6 Indent message
        [x] A. In test_game.py modify test_do_r_in_inv()
                [x] 1. Call .splitlines() on output and assign to var 'lines'
                [x] 2. Write assert st checking if lasst item in 'lines' = fake item's message w/ 4 spaces at beginning
                [x] 3. Run failing test
        [x] B. In test_game.py define test_wrap
                [x] 1. Add test_wrap(capsys)
                [x] 2. Call wrap with string longer than WIDTH
                [x] 3. Assign results to output
                [x] 4. Call .splitlines on output = 'line'
                [x] 5. Write assert that tests that length of lines > 1
                [x] 6. Write assert that tests output contains first few words of text arg
                [x] 7. Write assert that tests output ends w/ last few words of text arg followed by new line
                [x] 8. Make sure strings in lines start w/ 2 spaces
                [x] 9. Run passing test
        [x] C. In test.game.py define test_wrap_w_indent
                [x] 1. Add test_wrap_w_indent(capsys)
                [x] 2. Call wrap() w/ str longer than WIDTH followed by keyword indent = 2
                [x] 3. Assign capsys.roe.out to output
                [x] 4. Assn var lines to call spltlines on output
                [x] 5. Write assert lines > 1
                [x] 6. Assert output contains first words in text
                [x] 7. Assert output ends with last few words in text followed by 
                /n
                [x] 8. Make sure each str in var lines starts w 4 spaces
                [x] 9. Run failing test 
        [x] D. In adv.py modify wrap()
                [x] 1. Add optional indent parameter w def value 1
                [x] 2. When calculating margin, mult existing val by indent
                [x] 3. Run passing test_wrap 
        [x] E. In adv.py modify do_read()
                [x] 1. When printing item message with wrap(), add kwd arg indent w value 2
                [x] 2. Run test_do_read_in_inv -> Should pass
                [x] 3. All tests should pass
* [x] Part 12.7 Allow for stanzas
        [x] A. In test_game.py Modify test_do_read_in_place()
                [x] 1. Modify value of "message" key in fake item dict to be a tuple or list w mult items
                [x] 2. Add an assert that checks to make sure output contains 2 blank lines followed by indentation, followed by first few words of message items
                [x] 3. Run failing test
        [x] B. 
        [x] C. In adv.py modify wrap()
                [x] 1. Write an if statement checking if text is a string using isinstance fncn
                        [x] If so, make a list or tuple w text and assign to var text
                [x] 2. Make empty list and assign to var blocks
                [x] 3. Use a for loop to iterate over text using var name stanza
                        [x] Indent line(s) where you assign paragraph to be in for loop
                        [x] In call to textwrap.fill() use stanza for first arg instead of text
                        [x] Append paragraph to blocks
                [x] 4. Either:
                        [] Use arg unpacking to send all items in blocks list as sep args to print(), and kwd arg sep to print 
                                2 newlines bw each arg
                        [x] Join the blocks list using 2 newlines as the delimiter, then print
                [x] 5. Run passing 
        [x] D. In adv.py modify items
                [x] 1. Change "message" in "book" to be a list or a tuple of strings

Part 13: Health
* [x] Part 13.1 Add health_change()
        [x] A. In test_game.py define test_health_change
        [x] B. In adv.py define health_change()
* [] Part 13.2 Parameterize the test
        [] A. In test_game.py modify test_health_change() and Parameterize
                [x] 1. Change given Values to variables
                [x] 2. Add variables as parameters to test fncn
                [] 3. Call @pytest.mark.parameterize() with variables
                        start, amount, result, message
