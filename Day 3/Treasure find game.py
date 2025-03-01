print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("Write left of right to choose your path")
choice1 = input("Which path are you going to choose Left or Right? ")
if choice1 == "left" or choice1 == "Left":
    print("Do you want to wait or swim?")
    choice2 = input("Type wait or type swim")
    if choice2 == "wait" or choice2 =="Wait":
        print("Now choose a door between Red, Blue and Yellow")
        choice3 = input("Type red or blue or yellow")
        if choice3 == "Yellow" or choice3 == "yellow":
            print("You won and got the treasure")
        if choice3 == "Red" or choice3 == "red":
            print("You were burn by fire Game over")
        if choice3 == "Blue" or choice3 == "blue":
            print("You were attacked by a wizard Game over")
    else:
        print("Game over a crocodile attacked you")
else:
    print("Game Over. A tiger killed you")
