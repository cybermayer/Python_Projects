#region IMPORT

import pygame

#endregion

#region CONSTANTS

BLACK = (0, 0, 0)

#endregion

class Brick(pygame.sprite.Sprite):

    """<DOC

        Represents a brick in a pygame application.

            METHODS:
                    - __init__ -> None

    DOC?>"""

    def __init__(self, color, width, height):

        """<DOC

            Initializes the Brick object.

                PARAMETERS:
                            -color (tuple): The color of the brick.
                            -width (int): The width of the brick.
                            -height (int): The height of the brick.

        DOC?>"""

        #region CODE

        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()

        #endregion CODE
