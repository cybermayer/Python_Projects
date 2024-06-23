
from question_model import Question  # Importing the Question-model 
from data import question_data  # Importinge question data

nth_question = 0  # Initialize a counter for the current question number
score = 0  # Initialize a counter for the score

# Loop through each question in the question_data list
for i in range(0, len(question_data)):

    # Create a new Question object using the current question's text and answer
    new_question = Question(
        question_data[i]["text"], question_data[i]["answer"])

    # Prompt the user for an answer to the current question
    answer_given = input(f"{new_question.text}\n True or False?")

    # Check if the given answer matches the correct answer for the current question
    if answer_given == new_question.answer:
        nth_question += 1  
        score += 1  
    else:
        nth_question += 1  

    # Print the current progress after each question
    print(f"Your permanent result is {nth_question}/{score}")

# Print the final result after all questions have been answered
print(f"Your final result is {nth_question}/{score}")
