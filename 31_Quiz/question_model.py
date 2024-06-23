class Question:

    """<DOC

        Represents a question in the game.

            METHODS:
                    -__init__ -> None
                        
    DOC?>"""

    def __init__(self, q_text, q_answer):

        """<DOC

            Initialize a Question object with text and answer.

                PARAMETERS:
                            - q_text: The text of the question.
                            - q_answer: The answer to the question.

        DOC?>"""
        
        self.text = q_text
        self.answer = q_answer
