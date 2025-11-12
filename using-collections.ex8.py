# Explain why the code below
# prints different values on lines 3 and 4.

text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8 
# first we will evaluate the text[21:35] before we move to the .rfind method
# text[21:35] = 'for the fjords' 
# beginning at 21 inclusive 35 excluded ('!') according to 0 based indexing.
# 'for the fjords'.rfind('f') searches for the last place where the string 'f' is detectable.
# when we print(text[21:35].rfind('f')) the last indexable f is found on index[8]
print(text.rfind('f', 21, 35))    # 29 
# this reads finding the substring 'f' inside the string 
# "It's probably pining for the fjords!"
# evaluating only through the indexes 21 to 35 (end bound being exlusive). 
# Last detectable instance of the susbtring 'f' is found on index 29.