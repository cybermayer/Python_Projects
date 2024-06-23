
# This script simulates a simple text-based adventure game where the player makes choices to find the treasure.

# Print the welcome message for the game
print("WELCOME TO THE TREASURE ISLAND")

# Prompt the user to choose a direction: Left (L) or Right (R)
strDir = input("Choose a direction: Left (L) or Right (R)")

# Check if the user chose to go Left
if strDir == "L":
    # Prompt the user to choose an action: Wait here (W) or Swim across the river (S)
    strSW = input("Choose an option: Wait here (W) or Swim across the river (S)")
    
    # Check if the user chose to wait
    if strSW == "W":
    # Prompt the user to choose a door: Red (R), Yellow (Y), or Blue (B)
    strDoor = input("Choose a door you want to step into: Red (R), Yellow (Y) or Blue (B)")
        
        # Check which door the user chose
        if strDoor == "Y":
            print("You win!")
        elif strDoor == "B":
            print("Eaten by beasts!\nGAME OVER!")
        elif strDoor == "R":
            print("Burned by fire.\nGAME OVER!")
        else:
            print("GAME OVER!")
    else:
        print("Attacked by a hippo.\nGAME OVER!")
else:
    print("Eaten by a lion.\nGAME OVER!")

