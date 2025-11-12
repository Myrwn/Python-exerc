# Which of the following values 
# can't be used as a key in a 
# dict object, and why?

# Logic for determining the answer:
    # dict keys must be immutable
    # dict keys must be hashable 
    # immutable means the object can not be changed through mutation
    # hashable means the item has a unique id number named 'hash'
    # hash(1) works because integer 1 has a has number attached to it
    #my_list = [1, 2, 3]
    #hash(my_list)  # error: unhashable type 'list'

'cat' # strings can be used as keys in a dict object, since its hashable and immutable
(3, 1, 4, 1, 5, 9, 2) # tuples can be used since they are immutable and hashable
['a', 'b'] # lists can not be used since the are not hashable and are mutable.
{'a': 1, 'b': 2} # "Dictionaries cannot be used as keys because they are mutable, which makes them unhashable."
range(5) # the built in function range is hashable and immutable, therefore it can be used as a dict key.
{1, 4, 9, 16, 25} # sets are mutable therefore it can not be used as a dict objct
3 # integer types are hashable and immutable, therefore they can be used as dict keys
0.0 # float types are hashable and immutable, therefore they can be used as dict keys.
frozenset({1, 4, 9, 16, 25}) # frozensets are immutable and hashable, therefore they can be used as dict keys.