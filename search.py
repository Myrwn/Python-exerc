# You are 27 years old.
#In 10 years, you will be 37 years old.
#In 20 years, you will be 47 years old.
#In 30 years, you will be 57 years old.
#In 40 years, you will be 67 years old.


age = int(input("How old are you? "))
print(f"You are {age} years old")
print()

for future in range(10,50,10):
    print(f"In {future} years , you will be {age + future } years old ")

