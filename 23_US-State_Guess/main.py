import pandas
import turtle
import time
from answer import Answer, Write  #Import Answer and Write classes from answer module
import state  # Import state module

#Initializing screen
screen = turtle.Screen()
screen.setup(width=720, height=500)
screen.bgpic(r"blank_states_img.gif")

#Initializing objects of Answer, State, and Write classes
answer = Answer()
state = state.State()
write = Write()

#Initializing constants and variables
COUNT_STATES = len(state.states_list)  # Total number of states
count_known_states = 0  # Counter for number of correctly guessed states
is_repeat = False  # Flag to track if the guess is a repeat

print(COUNT_STATES) 

# Main game loop
while count_known_states != COUNT_STATES:

    player_guess = screen.textinput("States", "Which states can you remember?")
    
    # Check if the guess is a repeat and handle repeat guesses
    is_repeat = answer.is_repeat(player_guess)
    if is_repeat == True:
        write.repeat_answer()  # Write a message indicating the guess is a repeat
    
    # Handle new guesses
    elif is_repeat == False:
        is_correct = answer.check_answer(player_guess)  # Check if the guess is correct
        
        # Handle correct guesses
        if is_correct == True:
            write.correct_answer()  # Write a message indicating the guess is correct
            state.show_on_map(player_guess)  # Show the guessed state on the map
            count_known_states += 1  # Increment the count of correctly guessed states
            
            # Check if all states are guessed correctly
            if count_known_states == 50:
                time.sleep(2)  # Pause for 2 seconds if all states are guessed
            
        # Handle incorrect guesses
        else:
            write.wrong_answer()  # Write a message indicating the guess is incorrect

# Display fireworks animation after all states are guessed correctly
screen.bgpic(r"fireworks.gif")
screen.setup(width=220, height=220)
write.win()  

screen.exitonclick()  
