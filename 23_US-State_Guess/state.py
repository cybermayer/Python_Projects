#region IMPORT

from turtle import Turtle
import time
import pandas
import time
import answer

#endregion 

#region INIT

states_csv = pandas.read_csv(r"50_states.csv")
states_dict = states_csv.to_dict()
states_frame = pandas.DataFrame(states_dict)
states_lists = states_frame["state"].to_list()
xcors = states_frame["x"].to_list()
ycors = states_frame["y"].to_list()

#endregion

class State(Turtle):

    """<DOC

        Represents the states on a map in a game and implement Turtle inheritance.
    
        ATTRIBUTES:
    
            - states_list: List of state names.
            - xcor_list: List of x-coordinates for states.
            - ycor_list: List of y-coordinates for states.
    
    
        METHODS:
                    - __init__ -> None
                    - show_on_map -> None

    DOC?>"""

    def __init__(self):

        """<DOC

            Initialize the State object with state lists and coordinates.

        DOC?>"""

        super().__init__()
        self.states_list = states_lists
        self.xcor_list = xcors 
        self.ycor_list = ycors 
        
    def show_on_map(self, player_guess) -> None:

        """<DOC

            Show a state on the map based on player's guess.

        PARAMS:

            - player_guess: The name of the state to show.

        DOC?>"""

        xcor = self.xcor_list[self.states_list.index(player_guess)]
        ycor = self.ycor_list[self.states_list.index(player_guess)]
        self.hideturtle()
        self.penup()
        self.goto(xcor, ycor)
        self.write(player_guess, False, "center", ("Arial", 10,"normal")) 
