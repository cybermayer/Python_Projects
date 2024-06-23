# Rock, Paper, Scissors Game
# This script simulates a game of Rock, Paper, Scissors where the player competes against the computer.

import random

# Prompt the user to choose Rock (0), Paper (1), or Scissors (2)
intYourC = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors"))

# ASCII art representations for Rock, Paper, and Scissors
asciiRock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
asciiPaper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
asciiScissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Print the user's choice
print("Your choice")
if intYourC == 0:
    print(asciiRock)
elif intYourC == 1:
    print(asciiPaper)
elif intYourC == 2:
    print(asciiScissors)

# Generate the computer's choice randomly
intCompC = random.randint(0, 2)

# Print the computer's choice
print("Computer choice")
if intCompC == 0:
    print(asciiRock)
elif intCompC == 1:
    print(asciiPaper)
elif intCompC == 2:
    print(asciiScissors)

# Determine the outcome of the game
if (intYourC == 0 and intCompC == 0) or (intYourC == 1 and intCompC == 1) or (intYourC == 2 and intCompC == 2):
    print("Draw!")
elif (intYourC == 0 and intCompC == 2) or (intYourC == 1 and intCompC == 0) or (intYourC == 2 and intCompC == 1):
    print("You Win!")
elif (intYourC == 0 and intCompC == 1) or (intYourC == 1 and intCompC == 2) or (intYourC == 2 and intCompC == 0):
    print("You Lose!")
