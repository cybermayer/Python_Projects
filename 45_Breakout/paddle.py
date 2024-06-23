#region IMPORT

import pygame

#endregion

#region INIT

BLACK = (0, 0, 0)

#endregion

class Paddle(pygame.sprite.Sprite):

    """<DOC

        Represents a paddle in a pygame application.

            METHODS:
                    -__init__ -> None
                    -moveLeft -> None
                    -moveRight -> None

    DOC?>"""

    def __init__(self, color, width, height):

        """<DOC

            Initializes the Paddle object.

                PARAMETERS:
                            -color (tuple): The color of the paddle.
                            -width (int): The width of the paddle.
                            -height (int): The height of the paddle.

        DOC?>"""

        #region CODE

        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()

        #endregion

    def moveLeft(self, pixels):

        """<DOC

            Moves the paddle to the left by a specified number of pixels.

                PARAMETERS:
                            -pixels (int): Number of pixels to move the paddle to the left.

        DOC?>"""

        #region CODE

        self.rect.x -= pixels
        if self.rect.x < 0:
            self.rect.x = 0

        #endregion CODE

    def moveRight(self, pixels):
        
        """<DOC

            Moves the paddle to the right by a specified number of pixels.

                PARAMETERS:
                            -pixels (int): Number of pixels to move the paddle to the right.

        DOC?>"""

        #region CODE

        self.rect.x += pixels
        if self.rect.x > 700:
            self.rect.x = 700

        #endregion CODE
