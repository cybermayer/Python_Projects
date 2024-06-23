import html


class QuizBrain:

    """<DOC

        Represents a quiz game engine.

            ATTRIBUTES:
                        -question_number -> int
                        -score -> int
                        -question_list -> list
                        -current_question -> Question

            METHODS:
                        -__init__ -> None
                        -still_has_questions -> bool
                        -next_question -> str
                        -check_answer -> bool

    DOC?>"""

    def __init__(self, q_list):
        
        """<DOC

            Initialize QuizBrain with a list of questions.

                PARAMETERS:
                            - q_list (list): List of Question objects.

        DOC?>"""

        #region CODE
        
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

        #endregion 

    def still_has_questions(self) -> bool:
        
        """<DOC

            Checks if there are remaining questions.

                RETURNS:
                        - bool: True if there are more questions, False otherwise.

        DOC?>"""

        #region CODE
        
        return self.question_number < len(self.question_list)

        #endregion

    def next_question(self) -> str:
        
        """<DOC

            Retrieves the next question in the quiz.

                RETURNS:
                        - str: The formatted string representing the next question.

        DOC?>"""

        #region CODE
        
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text} (True/False): "

        #endregion

    def check_answer(self, user_answer: str) -> bool:
        
        """<DOC

            Checks if the user's answer matches the correct answer.

                PARAMETERS:
                            - user_answer (str): The user's answer to the question.
    
                RETURNS:
                            - bool: True if the answer is correct, False otherwise.

        DOC?>"""

        #region CODE
        
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False

        #endregion
