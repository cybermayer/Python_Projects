#region IMPORT

from turtle import Turtle

#endregion

class Fleet(Turtle):

    """<DOC

            Manages a fleet of aliens in a game.
    
                METHODS:
                        -__init__ -> None
                        -MoveFleet -> None
                        -changeFleetDirection -> None
                        -DetectLeftRightBoundaries -> None
                        -DetectLowerBoundary -> bool
                        -FleetDescent -> None
                        -DeleteAlien -> None

    DOC?>"""

    def __init__(self, x_position, y_position):

        """<DOC

                Initializes the Fleet object with aliens positioned in rows and columns.
    
                    PARAMETERS:
                                -x_position (int): X-coordinate position for the fleet.
                                -y_position (int): Y-coordinate position for the fleet.

        DOC?>"""

        #region CODE

        super().__init__()
        self.aliens = []
        xcor = x_position
        ycor = y_position
        for row in range(0, 3):  # barrier rows
            for alien in range(0, 8):  # Barrier 'columns'
                newAlien = Alien(xcor=xcor, ycor=ycor)
                self.aliens.append(newAlien)
                xcor += 45
            ycor += 40
            xcor = x_position

        #endregion

    def MoveFleet(self) -> None:

        """<DOC

                Moves the entire fleet of aliens.

        DOC?>"""

        #region CODE

        for alien in self.aliens:
            alien.forward(alien.speed)

        #endregion

    def changeFleetDirection(self) -> None:

        """<DOC

                Changes the direction of the entire fleet and initiates descent.

        DOC?>"""

        #region CODE

        self.FleetDescent()
        for alien in self.aliens:
            if alien.heading() == 0:
                alien.setheading(180)
            else:
                alien.setheading(0)

        #endregion

    def DetectLeftRightBoundaries(self) -> None:

        """<DOC

                Detects if any alien in the fleet has reached the left or right screen boundaries.

        DOC?>"""

        #region CODE

        for alien in self.aliens:
            if alien.xcor() > 265 or alien.xcor() < -265:
                self.changeFleetDirection()
                break

        #endregion

    def DetectLowerBoundary(self) -> None:

        """<DOC

                Detects if any alien in the fleet has reached the lower screen boundary.
    
                    RETURNS:
                            -bool: True if any alien is below the lower boundary, False otherwise.

        DOC?>"""

        #region CODE

        for alien in self.aliens:
            if alien.ycor() < -190:
                return True
        return False

        #endregion

    def FleetDescent(self) -> None:
        
        """<DOC

                Initiates descent for the entire fleet, increasing their speed and moving them downwards.

        DOC?>"""

        #region CODE

        for alien in self.aliens:
            alien.speed *= 1.01
            alien.goto(alien.xcor(), alien.ycor() - 5)

        #endregion

    def DeleteAlien(self, Alien) -> None:

        """<DOC

                Deletes a specified alien from the fleet.
    
                    PARAMETERS:
                                -Alien (Alien): The alien object to delete.

        DOC?>"""

        #region CODE

        Alien.clear()
        Alien.goto(3000, 3000)
        self.aliens.remove(Alien)
        del Alien

        #endregion

class Alien(Turtle):

    """<DOC

            Represents an individual alien in the game.

    DOC?>"""

    def __init__(self, xcor, ycor):

        """<DOC

            Initializes an Alien object with specified coordinates and implements Turtle inheritance.

                PARAMETERS:
                            -xcor (int): X-coordinate position for the alien.
                            -ycor (int): Y-coordinate position for the alien.

        DOC?>"""

        #region CODE

        super().__init__()
        self.shape('alien.gif')
        self.color("lime")
        self.penup()
        self.shapesize(stretch_wid=1.2, stretch_len=1.2)
        self.speed("fastest")
        self.goto(xcor, ycor)
        self.setheading(0)
        self.speed = 4

        #endregion
