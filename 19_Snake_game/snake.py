#region IMPORT

import turtle

#endregion 

#region INIT

SNAKE_TUPLES = [(0, 0), (-20, 0), (-40, 0)]
STEP = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

#endregion

class Snake:

    """<DOC

        Represents the snake in the game.

            METHODS:
                        -__init__ -> None
                        -create -> None
                        -add_part -> None
                        -move -> None
                        -up -> None
                        -down -> None
                        -right -> None
                        -left -> None

    DOC?>"""

    def __init__(self) -> None:

        """<DOC

            Initialize the snake object.

        DOC?>"""

        self.snake_parts = []
        self.create()
        self.head = self.snake_parts[0]

    def create(self) -> None:

        """<DOC

            Creates the initial snake.

        DOC?>"""

        #region CODE

        for tuples in SNAKE_TUPLES:
            new_snake_part = turtle.Turtle("square")
            new_snake_part.color("green")
            new_snake_part.penup()
            new_snake_part.goto(tuples)
            self.snake_parts.append(new_snake_part)
            self.snake_parts[0].color("grey")

        #endregion CODE

    def add_part(self) -> None:

        """<DOC

            Adds a new part to the snake.

        DOC?>"""

        #region CODE

        new_snake_part = turtle.Turtle("square")
        new_snake_part.color("green")
        new_snake_part.penup()
        self.snake_parts.append(new_snake_part)

        #endregion CODE

    def move(self) -> None:

        """<DOC

            Moves the snake forward.

        DOC?>"""

        #region CODE

        snake_length = len(self.snake_parts) - 1
        for nth_part in range(snake_length, 0, -1):
            new_xcor = self.snake_parts[nth_part - 1].xcor()
            new_ycor = self.snake_parts[nth_part - 1].ycor()
            self.snake_parts[nth_part].goto(new_xcor, new_ycor)
        self.head.forward(STEP)

        #endregion CODE

    def up(self) -> None:

        """<DOC

            Sets the snake's direction upwards.

        DOC?>"""

        #region CODE

        if self.head.heading() != DOWN:
            self.head.setheading(UP)

        #endregion CODE

    def down(self) -> None:

        """<DOC

            Sets the snake's direction downwards.

        DOC?>"""

        #region CODE

        if self.head.heading() != UP:
            self.head.setheading(DOWN)

        #endregion CODE

    def right(self) -> None:

        """<DOC

            Sets the snake's direction to the right.

        DOC?>"""

        #region CODE

        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

        #endregion CODE

    def left(self) -> None:

        """<DOC

            Sets the snake's direction to the left.

        DOC?>"""

        #region CODE

        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

        #endregion CODE
