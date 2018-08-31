from datetime import datetime, timedelta
from app.manage import conn, cur
from flask import current_app
import jwt
from werkzeug.security import generate_password_hash

class User(object):

    def __init__(self,first_name,last_name,username, email, password,confirm_password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.confirm_password=confirm_password
        
    def save_user(self):
        querry = 'INSERT INTO users (first_name, last_name,username,\
                              email, password) VALUES (%s,%s,%s,%s,%s)'

        cur.execute(querry,(self.first_name,self.last_name,self.username,\
                               self.email,self.password))
        conn.commit()

    @staticmethod
    def token_generator(user_id):

        '''method which generates token for users'''
        try:
            paylod = {
                'exp': datetime.utcnow() + timedelta(minutes=300),
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
        cur.execute(query, (str(token),))
        blacklisted_token = cur.fetchone()
        if blacklisted_token:
            return True
        return False

    def save_token(self, token):
        ''' persit token '''

        query = 'INSERT INTO tokens (token) VALUES (%s)'
        cur.execute(query, (token,))
        conn.commit()


