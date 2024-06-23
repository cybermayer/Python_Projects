#region IMPORT

import turtle

#endregion

#region INIT

LEFTUP = ((-590, -20), (-590, -10), (-590, 0), (-590, 10), (-590, 20))
RIGHTUP = ((590, -20), (590, -10), (590, 0), (590, 10), (590, 20))
screen = turtle.Screen()

#endregion

class Racket:

    """<DOC

        Represents the rackets used by players in the game.

            METHODS:
                        -__init__ -> None
                        -create_left_racket -> None
                        -create_right_racket -> None
                        -right_move_up -> None
                        -right_move_down -> None
                        -left_move_up -> None
                        -left_move_down -> None
                        -move_zero -> None

    DOC?>"""

    def __init__(self):

        """<DOC

            Initialize the Racket object.

        DOC?>"""

        self.left_parts = []
        self.right_parts = []
        self.create_left_racket()
        self.create_right_racket()

    def create_left_racket(self) -> None:

        """<DOC

            Creates the left racket parts.

        DOC?>"""

        for leftups in LEFTUP:
            new_part = turtle.Turtle("square")
            new_part.shapesize(1, 1)
            new_part.speed("fastest")
            new_part.penup()
            new_part.color("white")
            new_part.goto(leftups)
            self.left_parts.append(new_part)

    def create_right_racket(self) -> None:

        """<DOC

            Creates the right racket parts.

        DOC?>"""

        for rightups in RIGHTUP:
            new_part = turtle.Turtle("square")
            new_part.shapesize(1, 1)
            new_part.speed("fastest")
            new_part.penup()
            new_part.color("white")
            new_part.goto(rightups)
            self.right_parts.append(new_part)

    def right_move_up(self) -> None:

        """<DOC

            Moves the right racket parts upward.

        DOC?>"""

        if self.right_parts[4].ycor() < 290:
            screen.tracer(0)
            for rps in self.right_parts:
                new_y = rps.ycor()
                x = rps.xcor()
                new_y += 20
                rps.goto(x, new_y)
            screen.tracer(1)

    def right_move_down(self) -> None:

        """<DOC

            Moves the right racket parts downward.

        DOC?>"""

        if self.right_parts[4].ycor() > -290:
            screen.tracer(0)
            for rps in self.right_parts:
                new_y = rps.ycor()
                x = rps.xcor()
                new_y -= 20
                rps.goto(x, new_y)
            screen.tracer(1)

    def left_move_up(self) -> None:

        """<DOC

            Moves the left racket parts upward.

        DOC?>"""

        if self.left_parts[4].ycor() < 290:
            screen.tracer(0)
            for lps in self.left_parts:
                new_y = lps.ycor()
                x = lps.xcor()
                new_y += 20
                lps.goto(x, new_y)
            screen.tracer(1)

    def left_move_down(self) -> None:

        """<DOC

            Moves the left racket parts downward.

        DOC?>"""

        if self.left_parts[0].ycor() > -290:
            screen.tracer(0)
            for lps in self.left_parts:
                new_y = lps.ycor()
                x = lps.xcor()
                new_y -= 20
                lps.goto(x, new_y)
            screen.tracer(1)

    def move_zero(self) -> None:

        """<DOC

            Moves both rackets to the zero position.

        DOC?>"""

        screen.tracer(0)
        while self.left_parts[2].ycor() != 0:
            if self.left_parts[2].ycor() > 0.00:
                self.left_move_down()
            elif self.left_parts[2].ycor() < 0.00:
                self.left_move_up()
        while self.right_parts[2].ycor() != 0:
            if self.right_parts[2].ycor() > 0.00:
                self.right_move_down()
            elif self.right_parts[2].ycor() < 0.00:
                self.right_move_up()
        screen.tracer(1)
