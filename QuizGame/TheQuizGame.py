import QuestionModel
import Data

question_bank = []
for ques in Data.question_data:
    ques_text = ques["text"]
    ques_ans = ques["answer"]
    new_question = QuestionModel.Question(ques_text,ques_ans)
    question_bank.append(new_question)

# print(question_bank)

# Start The Game

