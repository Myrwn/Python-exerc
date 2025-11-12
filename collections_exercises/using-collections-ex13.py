cats = ('Cocoa', 'Cheddar',
        'Pudding', 'Butterscotch')
print('Butterscotch' in cats) # True 
print('Butter' in cats) # False, because in operator needs an exact match when in a tuple.
print('Butter' in cats[3]) # True, unlike the above example, it checks for the substring 'Butter' inside 'Butterscotch'
print('cheddar' in cats) # False, because membership is case-sensitive.