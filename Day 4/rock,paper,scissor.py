import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
pic = [rock, paper, scissors]
random_num = random.randint(0,2)

print("Welcome to rock paper and scissors game ")
user_choice = int(input("Type 0 for rock, 1 for paper, 2 for scissors \n"))
#print(f"You choose {pic[choice]}")
computer_choice = pic[random_num]
#print(computer_choice)
if user_choice == random_num:
    print(f"You choose \n{pic[user_choice]}")
    print(f"computer choose \n{computer_choice}")
    print("Match is draw")
elif user_choice == 0 and random_num == 1:
    print(f"You choose \n{pic[user_choice]}")
    print(f"computer choose \n{computer_choice}")
    print("Computer won")
elif user_choice == 0 and random_num == 2:
    print(f"You choose \n{pic[user_choice]}")
    print(f"computer choose \n{computer_choice}")
    print("You won")
elif user_choice == 1 and random_num == 2:
    print(f"You choose \n{pic[user_choice]}")
    print(f"computer choose \n{computer_choice}")
    print("Computer won")
elif user_choice == 1 and random_num == 0:
    print(f"You choose \n{pic[user_choice]}")
    print(f"computer choose \n{computer_choice}")
    print("You won")
elif user_choice == 2 and random_num == 0:
    print(f"You choose \n{pic[user_choice]}")
    print(f"computer choose \n{computer_choice}")
    print("Computer won")
elif user_choice == 2 and random_num == 1:
    print(f"You choose \n{pic[user_choice]}")
    print(f"computer choose \n{computer_choice}")
    print("You won")

else:
    print("Invalid choice please try again")
