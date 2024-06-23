#region IMPORT

from turtle import Turtle

#endregion

class AlienBombManager(Turtle):

    """<DOC

        Manages alien bombs in a game.

            METHODS:
                        - __init__ -> None
                        - MakeBomb -> None
                        - moveBombs -> None
                        - DetectLowerLimit -> None
                        - DeleteBomb -> None

    DOC?>"""

    def __init__(self):

        """<DOC

            Initializes the AlienBombManager and implements the Turtle inheritance. 

        DOC?>"""

        #region CODE

        super().__init__()
        self.bombs = []
        self.bomb_fall_speed = 9

        #endregion

    def MakeBomb(self, position_x, position_y) -> None:

        """<DOC

            Creates a new bomb at the specified position.

                PARAMETERS:
                            -position_x (int): X-coordinate of the bomb.
                            -position_y (int): Y-coordinate of the bomb.

        DOC?>"""

        #region CODE

        NewBomb = Turtle()
        NewBomb.penup()
        NewBomb.shape("circle")
        NewBomb.color("lime")
        NewBomb.shapesize(stretch_wid=0.5, stretch_len=0.5)
        NewBomb.goto(position_x, position_y - 5)
        NewBomb.setheading(270)
        self.bombs.append(NewBomb)

        #endregion CODE

    def moveBombs(self) -> None:

        """<DOC

            Moves all bombs downwards according to their fall speed.

        DOC?>"""

        #region CODE

        for bomb in self.bombs:
            bomb.forward(self.bomb_fall_speed)

        #endregion CODE

    def DetectLowerLimit(self) -> None:

        """<DOC

            Detects if any bomb has reached the lower limit of the screen (-290 y-coordinate).

        DOC?>"""

        #region CODE

        for bomb in self.bombs:
            if bomb.ycor() < -290:
                self.DeleteBomb(bomb)

        #endregion

    def DeleteBomb(self, Bomb) -> None:

        """<DOC

            Deletes a bomb from the screen and the bombs list.

                PARAMETERS:
                            -Bomb (Turtle): The bomb to delete.

        DOC?>"""

        #region CODE

        Bomb.clear()
        Bomb.goto(3000, 3000)
        self.bombs.remove(Bomb)
        del Bomb

        #endregion


