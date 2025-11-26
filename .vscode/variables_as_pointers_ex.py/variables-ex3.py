# Without running this code, what will it print? Why?

dict1 = {
    "Hitchhiker's Guide to the Galaxy": 42,
    'Monty Python': 'The Life of Brian',
    'Airplane!': "Don't call me Shirley!",
}

dict2 = dict(dict1) # dict(dict1) creates a shallow copy
dict2['Monty Python'] = 'Holy Grail' # replaces 'Monty Python' with 'Holy Grail'
print(dict1['Monty Python']) # outputs 'The Life of Brian'
                             # because 