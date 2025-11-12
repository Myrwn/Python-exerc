# Write one line of code to print the activities that Cocoa enjoys.

cats = {
    'Pete': {
        'Cheddar': {
            'color': 'orange',
            'enjoys': {
                'sleeping',
                'snuggling',
                'meowing',
                'eating',
                'birdwatching',
            },
        },
        'Cocoa': {
            'color': 'black',
            'enjoys': {
                'eating',
                'sleeping',
                'playing',
                'chewing',
            },
        },
    },
}

print(cats['Pete']['Cocoa']['enjoys'])
 # we first access the dictionary named cats
 # After, we enter in the nested dictionary named 'Pete'
 # Through 'Pete' we enter the nested dictionary named 'Cocoa'
 # And lastly, we enter the the activities Cocoa enjoys through
# through the key 'enjoys'.