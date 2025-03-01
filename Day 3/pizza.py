print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M or L: ")
price = 0

if size == "S" or size == "s":
    price = 15
elif size == "M" or size == "m":
    price = 20
elif size == "L" or size == "l":
    price = 25

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni == "Y" or pepperoni == "y":
    if size == "S" or size == "s":
        price += 2
    else:
        price += 3

extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y" or extra_cheese == "y":
    price += 1

print(f"Your final bill is: ${price}.")
