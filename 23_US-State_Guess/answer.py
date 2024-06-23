#region IMPORT

from turtle import Turtle
import time
from state import State

#endregion 

class Answer(State):
    
    """<DOC

        Represents the answer checking functionality in the game.
        
            INHERITED ATTRIBUTES:
                                - states_list: List of state names.
                                - already_guessed: List of states that have already been guessed.
        
            METHODS:
                                - __init__ -> None
                                - is_repeat -> bool
                                - check_answer -> bool

    DOC?>"""

    def __init__(self):
        
        """<DOC

            Initialize the Answer object.

        DOC?>"""
        
        super().__init__()
        self.already_guessed = []

    def is_repeat(self, player_guess) -> bool:
        
        """<DOC

            Check if the player's guess has already been guessed.

            PARAMS:
                - player_guess: The name of the state guessed by the player.
    
            RETURNS:
                - bool: True if the guess is a repeat, False otherwise.

        DOC?>"""
        
        is_repeat = False
        for states in self.already_guessed:
            if states == player_guess:
                is_repeat = True
                return is_repeat
        return is_repeat

    def check_answer(self, player_guess) -> bool:
        
        """<DOC

            Check if the player's guess is correct.
    
            PARAMS:
                - player_guess: The name of the state guessed by the player.
    
            RETURNS:
                - bool: True if the guess is correct, False otherwise.

        DOC?>"""
        
        for states in self.states_list:
            if states == player_guess:
                self.already_guessed.append(player_guess)
                result = True
                return result
        return False

class Write(Turtle):
    
    """<DOC

        Represents the visual feedback writer in the game.
    
            METHODS:
                        - __init__ -> None
                        - correct_answer -> None
                        - wrong_answer -> None
                        - repeat_answer -> None
                        - win -> None

    DOC?>"""

    def __init__(self):
        
        """<DOC

            Initialize the Write object and implement Turtle inheritance.

        DOC?>"""
        
        super().__init__()

    def correct_answer(self) -> None:
        
        """<DOC

            Displays a message for correct answer feedback.

        DOC?>"""
        
        self.clear()
        self.penup()
        self.hideturtle()
        self.color("green")
        self.write("Correct Answer!", False, "center", ("Bauhaus 93", 25, "bold"))
        time.sleep(1)
        self.clear()

    def wrong_answer(self) -> None:
        
        """<DOC

            Displays a message for wrong answer feedback.

        DOC?>"""
        
        self.clear()
        self.penup()
        self.hideturtle()
        self.color("red")
        self.write("Wrong Answer!", False, "center", ("Bauhaus 93", 25, "bold"))
        time.sleep(1)
        self.clear()

    def repeat_answer(self) -> None:
        
        """<DOC

            Displays a message for repeated answer feedback.

        DOC?>"""
        
        self.clear()
        self.penup()
        self.hideturtle()
        self.color("yellow")
        self.write("Repeated Answer!", False, "center", ("Bauhaus 93", 25, "bold"))
        time.sleep(1)
        self.clear()

    def win(self) -> None:
        
        """<DOC

            Displays a message for winning the game.

        DOC?>"""
        
        self.clear()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.write("ALL THE 50", False, "center", ("Bauhaus 93", 20, "bold"))
        time.sleep(3)
        self.clear()
