from app.app import *
from validate_email import validate_email
from app.manage import Database
db_connection = Database()

def validate_user_registration(json):
    if not(json["first_name"].strip()):
        return jsonify({'Message':
                        'First name is required'}), 400  
    if not(json["last_name"].strip()):
        return jsonify({'Message':
                        'Last name is required'}), 400    
    if not(json["username"].strip()):
        return jsonify({'Message':
                        'Username is required'}), 400
    if not(json["password"].strip()):
        return jsonify({'Message':
                        'Password is required'}), 400 
    return True


def validate_email_exist(email):
    query= "SELECT * FROM users WHERE email='{}'".format(email)
    cur = db_connection.cursor()
    cur.execute(query)
    row = cur.fetchone()
    if row:
    	return True
    return False

def validate_username_exist(username):
    query= "SELECT * FROM users WHERE username='{}'".format(username)
    cur = db_connection.cursor()
    cur.execute(query)
    row = cur.fetchone()
    if row:
    	return True
    return False

def validate_user_email(json):
    if not(validate_email(json["email"])):
        return jsonify({'Message':
                        'Enter a valid email'}), 400
    return True