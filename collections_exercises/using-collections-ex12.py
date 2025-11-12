#Write some code that determines and prints whether 
# the number 3 appears inside each of these lists:

numbers1 = [1, 3, 5, 7, 9, 11]
numbers2 = []
numbers3 = [2, 4, 6, 8]
numbers4 = ['1', '3', '5']
numbers5 = ['1', 3.0, '5']

# my code: 

print(3 in numbers1) # prints True
print(3 in numbers2) # prints False
print(3 in numbers3) # prints False
print(3 in numbers4) # prints False 
print(3 in numbers5) # prints True because 3 == 3.0