from turtle import Turtle

LCX = -620  # Left corner x-coordinate
LCY = -310  # Left corner y-coordinate
DTU = 620   # Distance to upper limit

class Gameboard(Turtle):
    
    """<DOC

        Represents the game board in the game.

            METHODS:
                        -__init__ -> None

    DOC?>"""

    def __init__(self):

        """<DOC

            Initialize the Gameboard object.

        DOC?>"""

        super().__init__()
        self.hideturtle()
        self.speed("normal")
        self.pencolor("white")
        self.penup()
        self.setposition(LCX, LCY)
        self.right(90)
        self.pensize(10)
        self.pendown()
        self.forward(DTU)
        self.forward(DTU)
        self.left(90)
        self.forward(DTU)
        self.left(90)
        self.forward(DTU)
        self.forward(DTU)
        self.left(90)
        self.forward(DTU)
        self.left(90)
        self.penup()
        self.goto(0, LCY)
        self.left(90)
        self.pensize(5)
        
        # Draw grid lines
        for n in range(int(DTU / 20 / 2) + 1):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
