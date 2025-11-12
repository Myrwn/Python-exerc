#This is a 3-part question. Consider the following dictionary:

pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

# Part 1: Write some code to print Bark by 
# accessing the element associated with the key Dog.
# Part 2: Write some code to print 
# None when you try to print the value associated with the non-existent key, Lizard.
# Part 3: Write some code to print <silence> when you 
# try to print the value associated with the non-existent key, Lizard.

print(pets['Dog']) # Part 1: printing Bark by accesing the associated key Dog. 

print(pets.get('Lizard'))  # Part 2: printing 'None' by using the method 'get.'
                           # get searches for the inserted keyword. 
                           # if it does not find it, it returns None by default
                           

print(pets.get('Lizard', '<silence>')) # Part 3: printing '<silence>' by using 
                                       # the get. method and passing the argument
                                       # '<silence>'. 
                                       # This prints '<silence>' instead of a name error
                                       # when we pass 'Lizard' to the get. method.