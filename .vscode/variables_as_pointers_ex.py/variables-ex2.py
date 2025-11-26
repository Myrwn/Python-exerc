# Without running this code, what will it print? Why?

set1 = {42, 'Monty Python', ('a', 'b', 'c')} # assigning variable name set1 a set
set2 = set1 # assigning set2 to set1
set1.add(range(5, 10)) # method to add range(5,10)
print(set2) 

# {42, 'Monty Python', ('a', 'b', 'c'),(range(5, 10)}

# since set2 = set1 its also true that set1 is set2 
# this means that both variables reference the same object in memory.