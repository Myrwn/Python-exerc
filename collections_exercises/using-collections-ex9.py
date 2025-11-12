#Write some code to replace the value 6 in the following nested list with 606:

stuff = [
    ['hello', 'world'],
    ['example', 'mem', None, 6, 88],
    [4, 8, 12],
]

stuff[1][3] = 606
# stuff[1] acceses the list on index[1] =
# ['example', 'mem', None, 6, 88]
# stuff[1][3]takes the index[3] of the list 
# and we replace the 6 with 606

print(stuff)