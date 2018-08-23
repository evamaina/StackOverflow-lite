from datetime import datetime
from app.manage import Database
db_connection = Database()

class Question(object):

    def __init__(self,user_id,title,content,posted_date):
        self.user_id = user_id 
        self.title = title
        self.content = content
        self.posted_date = datetime.now()
        
    def save_question(self):
        querry = 'INSERT INTO questions (title,content,user_id,posted_date) VALUES (%s,%s,%s,%s)'

        cursor = db_connection.cursor()
        cursor.execute(querry,(self.title,self.content,self.user_id,\
                               self.posted_date))
        db_connection.commit()