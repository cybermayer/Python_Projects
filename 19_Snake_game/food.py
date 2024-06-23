from turtle import Turtle
import random

class Food(Turtle):

    """<DOC

        Represents the food in the game.

            METHODS:
                        -__init__ -> None
                        -create_food -> None
                        -refresh_food -> None

    DOC?>"""

    def __init__(self) -> None:

        """<DOC

            Initialize the food object.

        DOC?>"""

        super().__init__()  # Initialize the Turtle superclass
        self.create_food()  # Create the appearance and initial position of the food

    def create_food(self) -> None:

        """<DOC

            Creates the appearance and initial position of the food.

        DOC?>"""

        #region CODE

        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.color("DeepPink4")
        self.penup()
        self.speed("fastest")
        self.refresh_food()

        #endregion CODE

    def refresh_food(self) -> None:

        """<DOC

            Moves the food to a random position within the game area.

        DOC?>"""

        #region CODE

        rx = random.randint(-280, 280)
        ry = random.randint(-280, 280)
        self.goto(rx, ry)

        #endregion CODE
