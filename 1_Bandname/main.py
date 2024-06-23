# Band Name Generator
# This script helps you create a unique name for your band by combining the type of pets you have with your dog's name.

# Print an introductory message to the user
print("Let's find out the name of your band\n")

# Prompt the user to input the type of pets they have, excluding dogs
cat = input("What kind of pets do you have? (except dogs)\n")

# Prompt the user to input their dog's name
dog = input("What's your dog's name?\n")

# Generate the band name by combining the dog's name with the type of pets
print("Your band's name: " + dog + "'s " + cat + "\n")

# Encourage the user to come up with some hit songs for their new band
print("Write some hits!")
