# Without running the following code, 
# what values will be printed by line 10?

pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

keys = pets.keys() # returns a view of all dictionary keys.
del pets['Dog'] # deletes key 'Dog' and 'Bark' as a consequence
pets['Snake'] = 'Sssss' # adds 'Snake' key 
print(keys) # dict_keys(['Cat', 'Bird', 'Snake'])