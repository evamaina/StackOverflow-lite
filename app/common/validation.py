from app.app import *
from app.manage import conn, cur
import re


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
    if not re.match(r"^[a-z0-9_]*$", json["username"]):
        return jsonify({"Message": "Enter a valid username"}), 400

    if not(json["password"].strip()):
        return jsonify({'Message':
                        'Password is required'}), 400
    
    return True


def validate_email_exist(email):
    query = "SELECT * FROM users WHERE email='{}'".format(email)
    cur.execute(query)
    row = cur.fetchone()
    if row:
        return True
    return False


def validate_username_exist(username):
    query = "SELECT * FROM users WHERE username='{}'".format(username)
    cur.execute(query)
    row = cur.fetchone()
    if row:
        return True
    return False


def validate_user_email(json):

    if not re.match(r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',
                    json["email"]):
        return jsonify({"Message": "Enter a valid email"}), 400
    return True


def validate_question(json):
    if not(json["title"].strip()):
        return jsonify({'Message':
                        'Title is required'}), 400
    if not(json["content"].strip()):
        return jsonify({'Message':
                        'Content is required'}), 400

    return True


def validate_answer(json):

    if not(json["answer_body"].strip()):
        return jsonify({'Message':
                        'Answer body is required'}), 400
    return True
