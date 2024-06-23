from turtle import Turtle

class SpaceShip(Turtle):
    
    """<DOC

            Represents the player's spaceship in the game.

                METHODS:
                            -__init__ -> None
                            -respawn -> None
                            -go_right -> None
                            -go_left -> None

    DOC?>"""

    def __init__(self):
        
        """<DOC

                Initializes the SpaceShip object and implement Turtle inheritance.

        DOC?>"""

        #region CODE

        super().__init__()
        self.penup()
        self.shape("ship")
        self.color("lime")
        self.setheading(90)
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.respawn()

        #endregion

    def respawn(self):
        
        """<DOC

                Resets the spaceship's position to the starting position.

        DOC?>"""

        #region CODE

        self.clear()
        self.goto(0, -260)

        #endregion

    def go_right(self):
        
        """<DOC

                Moves the spaceship to the right by 25 units.

        DOC?>"""

        #region CODE

        new_y = self.ycor()
        new_x = self.xcor() + 25
        self.goto(new_x, new_y)

        #endregion

    def go_left(self):
        
        """<DOC

                Moves the spaceship to the left by 25 units.

        DOC?>"""

        #region CODE

        new_y = self.ycor()
        new_x = self.xcor() - 25
        self.goto(new_x, new_y)

        #endregion
