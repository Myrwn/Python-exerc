# In your own words, explain the difference between these two expressions.

#my_object1 == my_object2 # both objects have the same value
#my_object1 is my_object2 # both objects reference the same address in memory. 

# print(my_object1 == my_object2) - is True when the objects have the same value
# print(my_object1 is my_object2) - is True when the objects share the same adress in memory
# # -> print(id(my_object1) == id(my_object2))