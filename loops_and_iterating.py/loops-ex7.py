# Write a find_integers function that returns a list of all the integers from my_tuple:

my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)

def find_integers(my_tuple):
    result = []
    for number in my_tuple:
        if type(number) is int:
            result.append(number)
    return result

#print(find_integers(my_tuple))