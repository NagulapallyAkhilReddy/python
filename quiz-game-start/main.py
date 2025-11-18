from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank=[]

for x in question_data:
    question_bank.append(Question(x["question"],x["correct_answer"]))

quiz=QuizBrain(question_bank)

while quiz.is_questions_left():
    quiz.next_question()

print("You have completed the Quiz")
print(f"your final score was{quiz.score}")