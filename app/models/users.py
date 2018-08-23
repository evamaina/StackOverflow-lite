from datetime import datetime, timedelta
from app.manage import Database
from flask import current_app
import jwt
db_connection = Database()
class User(object):

    def __init__(self,first_name,last_name,username, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = password
        
    def save_user(self):
        querry = 'INSERT INTO users (first_name, last_name,username,\
                              email, password) VALUES (%s,%s,%s,%s,%s)'

        cursor = db_connection.cursor()
        cursor.execute(querry,(self.first_name,self.last_name,self.username,\
                               self.email,self.password))
        db_connection.commit()

    @staticmethod
    def token_generator(user_id):

        '''method which generates token for users'''
        try:
            paylod = {
                'exp': datetime.utcnow() + timedelta(minutes=100),
                'iat': datetime.utcnow(),
                'sub': user_id

            }
            token = jwt.encode(
                paylod, current_app.config['SECRET_KEY']
            )
            return token 

        except Exception as e:
            return e

    @staticmethod
    def decodetoken(token):
        '''decodes the token'''
        try:
            paylod = jwt.decode(
                token, current_app.config['SECRET_KEY'])
            token_blacklisted = Tokens.verify_token(token)
            if token_blacklisted:
                return 'Invalid token please login'
            return paylod['sub']
        except jwt.ExpiredSignatureError:
            return 'Token expired'
        except jwt.InvalidTokenError:
            return 'This token is invalid'

class Tokens():
    def __init__(self, token):
        self.token = token

    @staticmethod
    def verify_token(token):
        '''query db to  check if token exist
        '''
        query = 'SELECT token FROM tokens WHERE token =%s'
        cursor = db_connection.cursor()
        cursor.execute(query, (str(token),))
        blacklisted_token = cursor.fetchone()
        if blacklisted_token:
            return True
        return False

    def save_token(self, token):
        ''' persit token '''
        cursor = db_connection.cursor()
        query = 'INSERT INTO tokens (token) VALUES (%s)'
        cursor.execute(query, (token,))
        db_connection.commit()


