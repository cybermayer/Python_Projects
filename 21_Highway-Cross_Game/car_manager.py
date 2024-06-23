#region IMPORT

from turtle import Turtle
import random

#endregion

#region INIT

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

#endregion 

class CarManager:

    """<DOC

        Manages the cars in the game, including creation and movement.

            METHODS:
                        -__init__ -> None
                        -create_car -> None
                        -move_cars -> None
                        -level_up -> None

    DOC?>"""

    def __init__(self):

        """<DOC

            Initialize the CarManager object.

        DOC?>"""

        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self) -> None:

        """<DOC

            Creates a new car with a random color and position if a random condition is met.

        DOC?>"""

        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self) -> None:

        """<DOC

            Moves all cars backward based on the current car speed.

        DOC?>"""

        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self) -> None:
        
        """<DOC

            Increases the car speed when called, to make the game more challenging.

        DOC?>"""

        self.car_speed += MOVE_INCREMENT
