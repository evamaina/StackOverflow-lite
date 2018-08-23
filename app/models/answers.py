from datetime import datetime
from app.manage import Database
db_connection = Database()

class Answer(object):

    def __init__(self,answer_body,question_id,posted_date,user_id): 
        self.answer_body = answer_body
        self.question_id = question_id
        self.posted_date = datetime.now()
        self.user_id = user_id
        
    def save_answer(self):
        querry = 'INSERT INTO answers(answer_body,question_id, posted_date,user_id) VALUES (%s,%s,%s,%s)'

        cursor = db_connection.cursor()
        cursor.execute(querry,(self.answer_body,self.question_id, self.posted_date,self.user_id))
        db_connection.commit()


        