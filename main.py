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
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if choice == 0:
  print(rock)
elif choice == 1:
  print(paper)
elif choice == 2:
  print(scissors)
else:
  print("Invalid choice :(")
print("Computer choice : ")
import random
x = random.randint(0,2)
if x == 0 :
  print(rock)   
elif x == 1:
  print(paper)
elif x == 2:
  print(scissors)

if x == choice:
  print("Game tied.")
elif choice == 0 and x == 1:
  print("you lose :(")
elif x == 0 and choice == 1:
  print("You Won.  :)")
elif choice == 1 and x == 2:
  print("you lose :(")
elif choice == 2 and x == 1:
  print("You Won.  :)")
elif choice == 2 and x == 0:
  print("you lose :(")
elif choice == 0 and x == 2:
  print("You Won.  :)")








