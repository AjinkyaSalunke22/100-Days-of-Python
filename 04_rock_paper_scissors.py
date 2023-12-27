rock = '''

Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''

Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''

Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

hand_gestures = [rock, paper, scissors]

rounds = True

while (rounds):
    user_input = int(input("Enter 0 for 'Rock', 1 for 'Paper', and 2 for Scissors. \n"))
    rand_no = random.randint(0,3)

    print(hand_gestures[user_input])
    print("Computer Choose:- \n",hand_gestures[rand_no])

    if ((user_input == 0) and (rand_no == 0)):
        print("It's a tie ;)")
    elif ((user_input == 0) and (rand_no == 1)):
        print("You loose :(")
    elif ((user_input == 0) and (rand_no == 2)):
        print("You win !")
    elif ((user_input == 1) and (rand_no == 0)):
        print("You win !")
    elif ((user_input == 1) and (rand_no == 1)):
        print("It's a tie ;)")
    elif ((user_input == 1) and (rand_no == 2)):
        print("You loose :(")
    elif ((user_input == 2) and (rand_no == 0)):
        print("You loose :(")
    elif ((user_input == 2) and (rand_no == 1)):
        print("You win !")
    elif ((user_input == 2) and (rand_no == 2)):
        print("It's a tie ;)")

    next_round = input("Do you want to play it again ? Y/N \n").lower()

    if (next_round == 'y'):
        rounds = True
    elif (next_round == 'n'):
        rounds = False
        print("Thanks for playing.")