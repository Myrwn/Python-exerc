#Print all of the even numbers in the following 
#list of nested lists. Don't use any while loops.

my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]


for sublist in my_list: # iterating over the outer lists
    for item in sublist: # iterating over the inner list 
        if item % 2 == 0: # computing even numbers
            print(item) # printing all the even numbers, one by one.