from celebrities import data  # Importing the data from the 'celebrities' module
import random 
import os 


def clear() -> int:                                #Function to clear the console screen (Windows).
    
                                                    return os.system('cls') 


def choose_celebrity(from_where) -> dict:          #Selects a random celebrity dictionary from 'from_where'    

                                                    result = random.choice(from_where)
    
                                                    return result


# Choosing an initial celebrity for the game
page1 = choose_celebrity(data)

score = 0  # Initializing the score counter
in_game = True  # Flag to control the game loop

while in_game == True:  # Main game loop

    # Choosing a new celebrity for comparison
    page2 = choose_celebrity(data)

    # Displaying information about the current celebrity (page1)
    print(f"{page1['name']} is a {page1['description']} in {page1['country']} followed by {page1['follower_count']} thousand people")

    # Prompting the user to guess if page2 has more or fewer followers than page1
    choice = input(f"Try to guess if {page2['name']} has more(m) or fewer(f) followers than {page1['name']}: ")

    # Comparing follower counts and updating score based on user's choice
    if choice == "m" and page1["follower_count"] < page2["follower_count"]:
        print(page2)
        page1 = page2  
        score += 1  
        clear()  
        print(f"Correct answer! Your actual score is {score}.")
        
    elif choice == "f" and page1["follower_count"] > page2["follower_count"]:
        print(page2)
        page1 = page2  
        score += 1  
        clear()  
        print(f"Correct answer! Your actual score is {score}.")
        
    elif page1["follower_count"] == page2["follower_count"]:
        print(page2)
        page1 = page2  
        clear()  
        print(f"These pages are followed by the same amount of followers. Your actual score is still {score}.")
        
    else:
        clear()  
        print("Wrong answer!")
        score = 0  
        back_to_game = input("Do you want to try again? yes(y) or no(n): ")
        
            if back_to_game == "y":
                in_game = True  
                page1 = choose_celebrity(data)  #
                elif back_to_game == "n":
                    in_game = False  
                    clear()  

    # End of game message
    print("GOOD BYE!\nI HOPE YOU COME BACK SOON!")
