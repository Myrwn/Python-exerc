#The following code causes an infinite loop 
#(a loop that never stops iterating). Why?

#ounter = 0 # counter created outside the loop

#while counter < 5: # while statement initialized 
   # print(counter) # print statement inside the loop

# The main problem, is that there is no condition to turn the 
# while statement falsy. As such, the counter will always stay 
# under 5 and cause an infinite loop. 

#solution

counter = 0

while counter <= 5:
    print(counter) # print statement here helps output all numbers from 0 until the while condition becoems falsy.
    counter += 1