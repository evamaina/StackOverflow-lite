from datetime import datetime

class Answer():
    """class to implement answer fuctionality"""

    def __init__(self ,answer_body,username):
        self.answer_body = answer_body
        self.username = username
        self.answer_date = datetime.now()
        self.answers = []

    def post_answer(self, answer_id, question_id, answer_body, date_posted,username):
        new_answers = {
                  "answer_id":answer_id,
                  "answer_body":answer_body,
                  "date_posted":date_posted,
                  "question_id":question_id,
                  "posted_by":username
                  }

        self.answers.append(new_answers)
        return (self.answers)