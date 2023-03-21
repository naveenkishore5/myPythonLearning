from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for each in question_data:
    question = each['text']
    answer = each['answer']
    new_question = Question(question, answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_have_questions():
    quiz.next_question()

print('You have completed the quiz')
print(f'Your final score was {quiz.score}/{quiz.question_number}')






