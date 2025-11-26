#Use a while loop to print all numbers in my_list 
#with even values, one number per line.
# Then, print the odd numbers using a ' for' loop.

my_list = [6, 3, 0, 11, 20, 4, 17]
index = 0 # creating an index variable outside the while and for loops.

while index < len(my_list): # while index is smaller than the lenght of my_list run the next block.
    if my_list[index] % 2 == 0: # even values evaluation
        print(my_list[index]) # printing even values
    index += 1 # index augmentation with each iteration.

for item in my_list: # go over every single item in my_list and run the next block(s).
        if item % 2 != 0: # for every item that is devided and does not return 0, run the following block
            print(item) # printing all the odd numbers.