#region IMPORT

from turtle import Turtle

#endregion

class Barrier(Turtle):
    
    """<DOC

            Manages a barrier in the game consisting of multiple bricks.
    
                METHODS:
                        -__init__ -> None
                        -DeleteBrick -> None

    DOC?>"""

    def __init__(self, x_position, y_position):
        
        """<DOC

                Initializes the Barrier object with rows and columns of bricks.
    
                    PARAMETERS:
                                -x_position (int): X-coordinate position for the barrier.
                                -y_position (int): Y-coordinate position for the barrier.

        DOC?>"""

        #region CODE

        super().__init__()
        self.bricks = []
        xcor = x_position
        ycor = y_position
        for row in range(0, 5):  # barrier rows
            for brick in range(0, 60):  # Barrier 'columns'
                if brick == 21 or brick == 41:
                    xcor += 20
                newBrick = BarrierBrick(xcor=xcor, ycor=ycor)
                self.bricks.append(newBrick)
                xcor += 8
            ycor += 9
            xcor = x_position

        #endregion

    def DeleteBrick(self, brick):
        
        """<DOC

                Deletes a specified brick from the barrier.
    
                    PARAMETERS:
                                -brick (BarrierBrick): The brick object to delete.

        DOC?>"""

        #region CODE

        brick.clear()
        brick.goto(3000, 3000)
        self.bricks.remove(brick)
        del brick

        #endregion

class BarrierBrick(Turtle):
    
    """<DOC

            Represents an individual brick in the barrier.

    DOC?>"""

    def __init__(self, xcor, ycor):
        
        """<DOC

                Initializes a BarrierBrick object with specified coordinates.
    
                    PARAMETERS:
                                -xcor (int): X-coordinate position for the brick.
                                -ycor (int): Y-coordinate position for the brick.

        DOC?>"""

        #region CODE

        super().__init__()
        self.shape("square")
        self.color("lime")
        self.penup()
        self.shapesize(stretch_wid=0.3, stretch_len=0.3)
        self.speed("fastest")
        self.goto(xcor, ycor)

        #endregion
