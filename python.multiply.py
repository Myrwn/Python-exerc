def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# Global identifiers: 
# first_number on lines 7, 9, 10
# second_number on lines 8, 9, 10
# product on lines 9, 10 
# get_num on line 4, 7, 8
# multiply on line 1, 9

# Local identifiers:
# prompt on line 4, 5 
# left, right on 1, 2

# Build in identifiers: 
# float on line 5
# input on line 5 
# print on line 10 

# keywords(not asked but for my own practice); 
# def on lines 1, 4
# return on lines 2, 5










