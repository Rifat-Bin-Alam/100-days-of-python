print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("Whats your age: "))
    if age <= 12 :
        print("Please pay 50 taka")
    elif age <=18 :
        print("Please pay 70 taka")
    else:
        print("Pay 120 taka")
else:
    print("Sorry you have to grow taller before you can ride.")
