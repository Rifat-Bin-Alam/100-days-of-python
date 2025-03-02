import random

user_guess = random.randint(0,100)
#showing the gues number too even gets head
if user_guess %2 == 0:
    print(f"{user_guess} Head")
else:
    print(f"{user_guess} Tail")

#or we use
num = random.randint(1,2)
if num == 1:
    print("head")
else:
    print("tail")