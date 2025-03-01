print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    bill=0

    if age <= 12:
        print("Your ticket is 5 taka.")
        bill=5
    elif age <= 18:
        print("Your ticket is 7 taka.")
        bill=7
    else:
        print("Your ticket is 12 taka.")
        bill=12

    photo = input("Do you want photo? Y for yes extra 3 taka N for No ")
    if photo == "y" :
        bill = bill+3
        print(f"Your bill is {bill}")


else:
    print("Sorry you have to grow taller before you can ride.")
