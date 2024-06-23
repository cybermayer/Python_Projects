#region IMPORT

from turtle import Turtle

#endregion

class Scoreboard(Turtle):
    
    """<DOC

            Manages the scoreboard for the game, displaying score, lives, and high score.
    
                METHODS:
                        -__init__ -> None
                        -RefreshScore -> None
                        -RemoveLife -> None
                        -GameOver -> None
                        -Reset -> None

    DOC?>"""

    def __init__(self):
        
        """<DOC

                Initializes the Scoreboard object with initial values.

        DOC?>"""

        #region CODE

        super().__init__()
        self.score = 0
        self.lives = 3
        self.high_score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color("lime")
        self.penup()
        self.hideturtle()
        self.goto(-290, 270)
        self.RefreshScore()

        #endregion

    def RefreshScore(self):
        
        """<DOC

                Refreshes and updates the displayed score, high score, and lives remaining.

        DOC?>"""

        #region CODE

        self.clear()
        score_text = f"Score: {self.score}. High Score: {self.high_score}.   You have {self.lives} lives left!"
        self.write(arg=score_text, align="left", font=("Arial", 15, "bold"), move=False)

        #endregion

    def RemoveLife(self):
        
        """<DOC

                Decrements the lives count and updates the scoreboard.

        DOC?>"""

        #region CODE

        self.lives -= 1
        self.RefreshScore()

        #endregion

    def GameOver(self, reason):
        
        """<DOC

                Displays a game over message based on the reason provided.
    
                    PARAMETERS:
                                -reason (str): Reason for game over ("Lives", "Won", "Invaded").

        DOC?>"""

        #region CODE

        self.goto(0, -240)
        if reason == "Lives":
            self.write("No more lives! Game over!!", align="center", font=('Arial', 20, 'bold'), move=False)
        elif reason == "Won":
            self.write("You eliminated all aliens! Well done!!", align="center", font=('Arial', 20, 'bold'), move=False)
        elif reason == "Invaded":
            self.write("The aliens have landed! Game over!!", align="center", font=('Arial', 20, 'bold'), move=False)
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(str(self.high_score))

        #endregion

    def Reset(self):
        
        """<DOC

                Resets the scoreboard, updating high score if the current score exceeds it.

        DOC?>"""

        #region CODE

        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.RefreshScore()

        #endregion
