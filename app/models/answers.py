from datetime import datetime
from app.manage import Database
db_connection = Database()

class Answer():
    """class to implement answer fuctionality"""

    def __init__(self,answer_body,question_id,user_id,posted_date):
      self.answer_body = answer_body
      self.question_id= question_id
      self.user_id = user_id
      self.posted_date = datetime.now()
      
    

    def save_answer(self):
      querry = 'INSERT INTO answers(answer_body,question_id,user_id,posted_date) VALUES (%s,%s,%s,%s)'

      cursor = db_connection.cursor()
      cursor.execute(querry,(self.answer_body,self.question_id,
                             self.user_id,self.posted_date))
      db_connection.commit()
        

      
