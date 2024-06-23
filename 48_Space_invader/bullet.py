from turtle import Turtle

class Bullet(Turtle):
    
    """<DOC

            Represents a bullet fired by the spaceship in the game.
    
                METHODS:
                        -__init__ -> None
                        -BulletMove -> None
                        -DetectTopLimit -> bool
                        -DestroyBullet -> None

    DOC?>"""

    def __init__(self, position_x, position_y):
        
        """<DOC

                Initializes the Bullet object.

                    PARAMS:
                            -position_x (int) -> x-coordinate of the bullet
                            -position_y (int) -> y-coordinate of the bullet

        DOC?>"""

        #region CODE

        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("lime")
        self.shapesize(stretch_wid=0.2, stretch_len=0.6)
        self.bullet_speed = 13
        self.goto(position_x, position_y + 20)
        self.setheading(90)

        #endregion

    def BulletMove(self):
        
        """<DOC

            Moves the bullet upwards based on its speed.

        DOC?>"""

        #region CODE

        self.forward(self.bullet_speed)

        #endregion

    def DetectTopLimit(self):
        
        """<DOC

            Checks if the bullet has reached the top limit of the screen.

                RETURNS:
                        -bool: True if bullet is above the top limit, False otherwise.

        DOC?>"""

        #region CODE

        if self.ycor() > 260:
            self.hideturtle()
            self.clear()
            self.goto(2000, 2000)
            return True
        return False

        #endregion

    def DestroyBullet(self):
        
        """<DOC

                Destroys the bullet by moving it off-screen and hiding it.

        DOC?>"""

        #region CODE

        print("Bullet destroyed")
        self.goto(1000, 1000)
        self.hideturtle()

        #endregion
