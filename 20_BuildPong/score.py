#region IMPORT

from turtle import Turtle

#endregion 

class Score(Turtle):

    """<DOC

        Represents the score display for the game.

            METHODS:
                        -__init__ -> None
                        -update -> None
                        -increase_left_score -> None
                        -increase_right_score -> None

    DOC?>"""

    def __init__(self):

        """<DOC

            Initialize the Score object.

        DOC?>"""

        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.left_score = 0
        self.right_score = 0
        self.update()

    def update(self) -> None:

        """<DOC

            Updates the score display on the screen.

        DOC?>"""

        self.goto(-50, 310)
        self.write(f"{self.left_score}", False, "center", ("Bauhaus 93", 30, "bold"))
        self.goto(50, 310)
        self.write(f"{self.right_score}", False, "center", ("Bauhaus 93", 30, "bold"))

    def increase_left_score(self) -> None:

        """<DOC

            Increases the left player's score and updates the display.

        DOC?>"""

        self.clear()
        self.left_score += 1
        self.update()

    def increase_right_score(self) -> None:

        """<DOC

            Increases the right player's score and updates the display.

        DOC?>"""

        self.clear()
        self.right_score += 1
        self.update()
