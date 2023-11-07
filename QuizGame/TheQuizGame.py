import QuestionModel
import Data

question_bank = []
for ques in Data.question_data:
    ques_text = ques["text"]
    ques_ans = ques["answer"]
    new_question = QuestionModel.Question(ques_text, ques_ans)
    question_bank.append(new_question)


# print(question_bank)

# Start The Game

class QuizGame:
    def __init__(self, q_list):
        self.ques_num = 0
        self.ques_list = q_list
        self.score = 0

    def next_ques(self):
        current_ques = self.ques_list[self.ques_num]
        self.ques_num += 1
        user_ans = input(f"Q.{self.ques_num}: {current_ques.text} (True/False)")
        self.check_ans(user_ans, current_ques.answer)

    def ques_left(self):
        return self.ques_num < len(self.ques_list)

    def check_ans(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            self.score += 1
            print("The answer is correct")
        else:
            print("The answer is wrong")
        print(f"The correct answer is - {correct_ans}.")
        print(f"Your score is - {self.score}")


quiz = QuizGame(question_bank)

while quiz.ques_left():
    quiz.next_ques()

print("You have completed the quiz")
print(f"Your final score is: {quiz.score}/{quiz.ques_num}")
