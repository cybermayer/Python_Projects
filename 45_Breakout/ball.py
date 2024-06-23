#region IMPORT

import pygame
from random import randint

#endregion

#region INIT

BLACK = (0, 0, 0)

#endregion

class Ball(pygame.sprite.Sprite):

    """<DOC

        Represents a ball in a pygame application.

            METHODS:
                    - __init__ -> None
                    - update -> None
                    - bounce -> None

    DOC?>"""

    def __init__(self, color, width, height):

        """<DOC

            Initializes the Ball object.

                PARAMETERS:
                            -color (tuple): The color of the ball.
                            -width (int): The width of the ball.
                            -height (int): The height of the ball.

        DOC?>"""

        #region CODE

        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.velocity = [randint(4, 8), randint(-8, 8)]
        self.rect = self.image.get_rect()

        #endregion 

    def update(self):

        """<DOC

            Updates the position of the ball based on its velocity.

        DOC?>"""

        #region CODE

        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        #endregion CODE

    def bounce(self):
        
        """<DOC

            Changes the direction of the ball's velocity to simulate a bounce.

        DOC?>"""

        #region CODE

        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8, 8)

        #endregion CODE
