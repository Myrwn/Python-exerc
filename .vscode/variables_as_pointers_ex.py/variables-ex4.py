# Without running this code, what will it print? Why?

dict1 = {
    'a': [1, 2, 3],
    'b': (4, 5, 6),
}

dict2 = dict(dict1) # dict2 is assigned to a shallow copy of dict1
dict1['a'][1] = 42 # dict1 replaces the key value 2 with the integer 42
print(dict2['a']) # {[1, 2, 3]}
                  