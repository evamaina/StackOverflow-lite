from datetime import datetime

class Question(object):

    def __init__(self, title, content): 
        self.title = title
        self.content = content
        self.date_posted = datetime.now()
        self.questions = []
        
    def post_question(self,question_id, title, content,date_posted):
        new_question = {
            'question_id': question_id,
            'title': title,
            'content': content,
            'date_posted':date_posted}

        self.questions.append(new_question)
        return (self.questions)
