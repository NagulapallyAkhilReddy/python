
#changed after mam's explanation(CAME),mine was not bad though
class QuizBrain:
    def __init__(self,question_list):
        self.question_list=question_list
        self.question_number=0
        self.length=len(question_list)
        self.score=0

    def is_questions_left(self):
        return self.question_number<self.length
    def check_answer(self,user_answer,correct_answer):
        if user_answer == correct_answer:
            print("you got it right")
            self.score += 1
        else:
            print("you got it wrong")
        print(f'the correct answer was :{correct_answer} ')
        print(f'your current score is {self.score}')
    def next_question(self):

        # while self.question_number<self.length:#improvised the code after mam's explanation, mine was not bad though
            q=self.question_list[self.question_number]
            self.question_number+=1
            a=input(f'Q.{self.question_number} : {q.text}. (True/False)? : ').lower()
            c_a=q.answer.lower()
            self.check_answer(a, c_a)
            # if a==q.answer.lower():
            #     print("you got it right")
            #     self.score+=1
            # else:
            #     print("you got it wrong")
            # print(f'the correct answer was :{q.answer} ')
            # print(f'your current score is {self.score}')
        # if self.question_number==self.length:
        #     print("the quiz is completed")
        #     print(f"your final score is {self.score}")






