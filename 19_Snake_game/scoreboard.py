from turtle import Turtle

class Scoreboard(Turtle):

    """<DOC

        Represents the scoreboard for displaying score and game over messages.

            METHODS:
                        -__init__ -> None
                        -add_score -> None
                        -game_over -> None

    DOC?>"""

    def __init__(self):

        """<DOC

            Initialize scoreboard.

        DOC?>"""

        super().__init__()  # Initialize the Turtle superclass
        self.hideturtle()
        self.penup()
        self.goto(0, 327)
        self.color("blue")
        self.score = 0
        self.write(
            f"Your score: {self.score}", False, "center", ("Courier", 16, "bold"))

    def add_score(self) -> None:

        """<DOC

            Increments the score by 1 and updates the scoreboard.

        DOC?>"""

        #region CODE

        self.hideturtle()
        self.penup()
        self.goto(0, 327)
        self.color("blue")
        self.score += 1
        self.write(
            f"Your score: {self.score}", False, "center", ("Courier", 16, "bold"))

        #endregion CODE

    def game_over(self) -> None:

        """<DOC

            Displays the game over message on the scoreboard.

        DOC?>"""

        #region CODE

        self.hideturtle()
        self.penup()
        self.goto(0, 327)
        self.color("blue")
        self.write("GAME OVER!", False, "center", ("Courier", 16, "bold"))

        #endregion CODE
