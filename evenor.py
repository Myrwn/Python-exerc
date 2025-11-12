False or (True and False) # -> False or (False [because 'and' checks for the first falsy value or the last value if all are truthy] -> False [Because or checks for the first truthy value or if all values are false the first value.]) 
True or (1 + 2) # - > True or (3) -> True (because: or evaluates the first truthy value, or the last value if all are falsy.)
(1 + 2) or True # - > (3) or True - > 3 (or = first truthy, or last value if all fasly.)
True and (1 + 2) # - > True and (3) - > 3 (and = returns the last value if all truthy.)
False and (1 + 2) # - > False and (3) - > False (and = returns the first falsy value.)
(1 + 2) and True # - > (3) and True - > True (and = returns the last value if all truthy)
(32 * 4) >= 129 # - > False (because 128 < 129)
False != (not True) # - > False != (False) is False because False == False
True == 4 # - > False, because == checks for equality and 4 is not equal to True.
False == (847 == '847') # - > False == (False) is True, because False is False ( the int 847 is not equal to the str 847.).