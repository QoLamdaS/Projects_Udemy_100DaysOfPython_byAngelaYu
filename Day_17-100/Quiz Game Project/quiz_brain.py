class QuizBrain :
    def __init__(self, question_list):
        self.q_number = 0
        self.q_list = question_list
    
    def still_has_questions(self):
        return self.q_number < len(self.q_list)

    def next_question(self):
        current_question = self.q_list[self.q_number]
        self.q_number += 1
        input(f"Q.{self.q_number}: {current_question.text} (True/False)? ")
