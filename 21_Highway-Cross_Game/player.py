#region IMPORT

from turtle import Turtle

#endregion 

#region INIT

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

#endregion

class Player(Turtle):

    """<DOC

        Represents the player's turtle in the game.

            METHODS:
                        -__init__ -> None
                        -go_up -> None
                        -go_to_start -> None
                        -is_at_finish_line -> bool

    DOC?>"""

    def __init__(self) -> None:

        """<DOC

            Initialize the Player object.

        DOC?>"""

        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def go_up(self) -> None:

        """<DOC

            Moves the player turtle upwards by MOVE_DISTANCE units.

        DOC?>"""
        
        self.forward(MOVE_DISTANCE)

    def go_to_start(self) -> None:

        """<DOC

            Moves the player turtle to the starting position.

        DOC?>"""

        self.goto(STARTING_POSITION)

    def is_at_finish_line(self) -> bool:

        """<DOC

            Checks if the player turtle has reached the finish line.

                    RETURNS:    True if the player's y-coordinate is greater than FINISH_LINE_Y, False otherwise

        DOC?>"""

        if self.ycor() > FINISH_LINE_Y:

            return True
        
        else:
            
            return False
