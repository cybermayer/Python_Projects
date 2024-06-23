#region IMPORT

from tkinter import *
from quiz_brain import QuizBrain

#endregion 

#region INIT

THEME_COLOR = "#375362"

#endregion

class QuizInterface:

    """<DOC

        Represents the graphical user interface for the quiz game.

            ATTRIBUTES:
                        -quiz -> QuizBrain
                        -window -> Tk
                        -score_label -> Label
                        -canvas -> Canvas
                        -question_text -> int
                        -true_button -> Button
                        -false_button -> Button

            METHODS:
                        -__init__ -> None
                        -get_next_question -> None
                        -true_answer -> None
                        -false_answer -> None
                        -give_feedback -> None

    DOC?>"""

    def __init__(self, quiz_brain: QuizBrain):

        """<DOC

            Initialize the QuizInterface with a QuizBrain instance.

                PARAMETERS:
                            - quiz_brain (QuizBrain): The QuizBrain object managing the quiz.

        DOC?>"""

        #region CODE

        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        
        self.score_label = Label(text=f"Your score: {self.quiz.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Some Question Text", fill=THEME_COLOR, font=("Arial", 18, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        
        true_image = PhotoImage(file=r"./images/true.png")
        false_image = PhotoImage(file=r"./images/false.png")
        
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_answer)
        self.true_button.grid(row=2, column=0)
        
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_answer)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

        #endregion CODE

    def get_next_question(self) -> None:

        """<DOC

            Updates the interface with the next question from QuizBrain.

        DOC?>"""

        #region CODE

        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.question_text, fill=THEME_COLOR)
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text, width=250)

        #endregion 

    def true_answer(self) -> None:

        """<DOC

            Handles the user selecting 'True' as an answer.

        DOC?>"""

        #region CODE

        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

        #endregion

    def false_answer(self) -> None:

        """<DOC

            Handles the user selecting 'False' as an answer.

        DOC?>"""

        #region CODE

        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

        #endregion

    def give_feedback(self, is_right) -> None:

        """<DOC

            Provides feedback to the user based on their answer.

                PARAMETERS:
                            - is_right (bool): Indicates if the user's answer was correct.

        DOC?>"""

        #region CODE

        if is_right:
            self.canvas.config(bg="green")
            self.canvas.itemconfig(self.question_text, fill="white")
            self.score_label.config(text=f"Your score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")
            self.canvas.itemconfig(self.question_text, fill="white")
        
        self.window.after(1000, self.get_next_question)

        #endregion
