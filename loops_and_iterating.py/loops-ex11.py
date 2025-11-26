#Print all of the even numbers in the following list of nested lists. 
#This time, don't use any for loops.

my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]
index = 0
index2 = 0
while index < len(my_list):
    index2 = 0
    while index2 < len(my_list[index]):
        number = my_list[index][index2]
        if number % 2 == 0: 
            print(number)
        index2 += 1      # increment inside inner loop
    index += 1           # increment inside outer loop