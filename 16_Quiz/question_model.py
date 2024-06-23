class Question:
    
    """<DOC

        Models a question with a text and an answer.

            METHODS:
                        -__init__ -> None

    DOC?>"""

    def __init__(self, text: str, answer: str) -> None:
        """<DOC

            Initialize a Question object with text and answer.

                    ARGS:    text: The text of the question
                             answer: The answer to the question

        DOC?>"""

        #region CODE

        self.text = text
        self.answer = answer

        #endregion CODE
