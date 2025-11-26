# Use a while loop 
# to print the numbers in my_list, 
# one number per line. 
# Then, do the same with a for loop.

# Solution for a while loop:

my_list = [6, 3, 0, 11, 20, 4, 17]
index = 0 # creating a variable index outside of the loop

while index < len(my_list): # while index remains below the lenth number of my_list execute the folloing block
    print(my_list[index]) # outputs the index of my_list starting from 0
    index += 1 # since index < len(my_list) is true, use augmented assignment on index +1
#output
#6
#3
#0
#11
#20
#4
#17

# Solution for a for loop: 

my_list = [6, 3, 0, 11, 20, 4, 17]

for item in my_list: # execute the next block of code for every item inside my_list.
    print(item)