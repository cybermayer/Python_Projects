#region IMPORT

from turtle import Turtle
import random
import math

#endregion

#region INIT

DIRECTIONS = [90, 270]  # List of directions in degrees
MU = 10  # Movement unit for the ball
TLC = (-620, 310)  # Top-left corner coordinates
BLC = (-620, -310)  # Bottom-left corner coordinates
TRC = (620, 310)  # Top-right corner coordinates
BRC = (620, -310)  # Bottom-right corner coordinates
DTU = 620  # Distance to the upper limit

#endregion

class Ball(Turtle):

    """<DOC

        Represents the ball in the game.

            METHODS:
                        -__init__ -> None
                        -summon_ball -> None
                        -move_ball -> None
                        -detect_top -> bool
                        -detect_bottom -> bool
                        -specify_dir -> bool
                        -racket_bounce -> None
                        -wall_bounce -> None

    DOC?>"""

    def __init__(self):

        """<DOC

            Initialize the ball object.

        DOC?>"""

        super().__init__()
        self.summon_ball()

    def summon_ball(self) -> None:

        """<DOC

            Creates the appearance and initial direction of the ball.

        DOC?>"""

        #region CODE

        self.clear()
        self.color("white")
        self.shape("circle")
        self.shapesize(1, 1)
        rdir = random.choice(DIRECTIONS)
        self.setheading(rdir)
        self.penup()

        #endregion CODE

    def move_ball(self) -> None:

        """<DOC

            Moves the ball forward by MU units.

        DOC?>"""

        #region CODE

        self.forward(MU)

        #endregion CODE

    def detect_top(self) -> bool:

        """<DOC

            Checks if the ball has hit the top wall.

        DOC?>"""

        #region CODE

        if self.ycor() >= 300:
            top_bounce = True
        else:
            top_bounce = False
                                            
        return top_bounce

        #endregion CODE

    def detect_bottom(self) -> bool:

        """<DOC

            Checks if the ball has hit the bottom wall.

        DOC?>"""

        #region CODE

        if self.ycor() <= -300:
            bottom_bounce = True
        else:
            bottom_bounce = False
                                                
        return bottom_bounce

        #endregion CODE

    def specify_dir(self) -> bool:

        """<DOC

            Determines if the ball is moving left to right.

        DOC?>"""

        #region CODE

        if self.heading() >= 0 and self.heading() < 180:
            left_to_right = True
        else:
            left_to_right = False
                                                    
        return left_to_right

        #endregion CODE

    def racket_bounce(self) -> None:

        """<DOC

            Changes the direction of the ball upon hitting the racket.

        DOC?>"""

        #region CODE

        left_to_right = self.specify_dir()
        if left_to_right:
            self.setheading(random.randint(190, 351))
        else:
            self.setheading(random.randint(10, 171))

        #endregion CODE

    def wall_bounce(self) -> None:

        """<DOC

            Handles bouncing off the walls based on current direction.

        DOC?>"""

        #region CODE

        left_to_right = self.specify_dir()
        top_bounce = self.detect_top()
        bottom_bounce = self.detect_bottom()

        if not left_to_right and top_bounce:
            self.setheading(DIRECTIONS[1])
            adj_leg = self.distance(TLC)
            op_leg = DTU
            max_turn = int(math.degrees(math.atan(op_leg / adj_leg)))
            self.left(random.randint(10, max_turn))

        elif not left_to_right and bottom_bounce:
            self.setheading(DIRECTIONS[1])
            adj_leg = self.distance(BLC)
            op_leg = DTU
            max_turn = int(math.degrees(math.atan(op_leg / adj_leg)))
            self.right(random.randint(10, max_turn))

        elif left_to_right and top_bounce:
            self.setheading(DIRECTIONS[0])
            adj_leg = self.distance(TRC)
            op_leg = DTU
            max_turn = int(math.degrees(math.atan(op_leg / adj_leg)))
            self.right(random.randint(10, max_turn))

        elif left_to_right and bottom_bounce:
            self.setheading(DIRECTIONS[0])
            adj_leg = self.distance(BRC)
            op_leg = DTU
            max_turn = int(math.degrees(math.atan(op_leg / adj_leg)))
            self.left(random.randint(10, max_turn))

        #endregion CODE
