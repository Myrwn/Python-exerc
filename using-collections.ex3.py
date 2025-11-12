#Write Python code to create a new tuple from (1, 2, 3, 4, 5).
#The new tuple should be in reverse order from the original.
#It should also exclude the first and last members of the original. 
#The result should be the tuple (4, 3, 2).

my_tuple = (1, 2, 3, 4, 5) # creating a new variable named my_tuple for my tuple.

new_my_tuple = my_tuple[1:-1][::-1]
 # new_my_tuple is using 2 slicing operations.
 # [1:-1] = (2, 3, 4) -> first part of our solution
 # [::-1] = (4, 3, 2) -> reversing the order 
 # how to read [::-1]
 # [::-1] means start stop step 
 # [::-1] start and stop are empty
 # [::-1] -1 signals to return the whole collection in reverse
 # thus [::-1](2, 3, 4) returns (4, 3, 2)

print(new_my_tuple)