import random

def compare(guess, attempts_left, actual_number) -> int:             # Function to compare the guessed number with the actual number

                                                                       if guess == actual_number:                                
                                                                            attempts_left -= 100  
                                                                            print(f"The number is {actual_number}")
                                                                            print("Congratulations you WIN!")
                                                                        elif guess > actual_number:
                                                                            attempts_left -= 1
                                                                            print("Sorry. It's too much.")
                                                                        elif guess < actual_number:
                                                                            attempts_left -= 1
                                                                            print("Sorry. It's too low.")
                                                                            
                                                                        return attempts_left

# Prompting the user to choose difficulty level
difficulty_level = input("Choose difficulty level. Easy(e) or Hard(h): ")

# Displaying initial message
print("Okay let's play. I thought of a number between 1 and 100.")
actual_number = random.randint(1, 100)  
attempts = 10  

# Handling game logic based on difficulty level chosen
if difficulty_level == "e":  # Easy mode
    while attempts > 0:
        print(f"You have {attempts} attempts left.")
        guess = int(input("Guess the number: "))
        attempts = compare(guess, attempts, actual_number)
        if attempts <= 0:
            print("There are no more attempts. GAME OVER!")

elif difficulty_level == "h": #Hard mode  
    attempts -= 5  
    while attempts > 0:
        print(f"You have {attempts} attempts left.")
        guess = int(input("Guess the number: "))
        attempts = compare(guess, attempts, actual_number)
        if attempts <= 0:
            print("There are no more attempts. GAME OVER!")

else:
    print("Invalid input. Please choose 'e' for Easy or 'h' for Hard.")
