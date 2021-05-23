

print("Welcome to the Rock, Paper, Scissors Game!")

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_images = [rock, paper, scissor]
import random

make_a_choice = input("What do you choose ? Type 'Rock', 'Paper' or 'Scissors' : \n").lower()
if make_a_choice == 'rock':
    user_choice = 0
elif make_a_choice == 'paper':
    user_choice = 1
elif make_a_choice == 'scissors':
    user_choice = 2
else:
    user_choice = 9

if user_choice == 9:
    print("Please make a valid choice")
else:
    print("You chose {}".format(make_a_choice))
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    if computer_choice == 0:
        print("Computer chose rock")
        print(game_images[computer_choice])
    if computer_choice == 1:
        print("Computer chose paper")
        print(game_images[computer_choice])
    if computer_choice == 2:
        print("Computer chose scissors")
        print(game_images[computer_choice])

    if user_choice == computer_choice:
        print("It's a draw, try again!")
    elif user_choice == 0 and computer_choice == 2:
        print("You Win :)")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose :(")
    elif user_choice > computer_choice:
        print("You Win :)")
    else:
        print("You lose :(")

