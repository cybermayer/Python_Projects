from turtle import Turtle

#region INIT

LC = -310  # Constant representing the left coordinate for the playground boundaries
DT = 620  # Constant representing the total distance of the playground boundaries

#endregion

class Playground(Turtle):

    """<DOC

        Represents the playground area where the game takes place.

            METHODS:
                        -__init__ -> None

    DOC?>"""

    def __init__(self):

        """<DOC

            Initialize the playground object.

        DOC?>"""

        super().__init__()  # Initialize the Turtle superclass
        self.hideturtle()
        self.penup()
        self.setposition(LC, LC)
        self.pensize(32)
        self.pendown()
        self.pencolor("gray20")
        for x in range(4):
            self.forward(DT)
            self.left(90)
