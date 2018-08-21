from app.app import *
from validate_email import validate_email

def validate_user_registration(json):
    if not(json["first_name"].strip()):
        return jsonify({'Message':
                        'First name is required'}), 401  
    if not(json["last_name"].strip()):
        return jsonify({'Message':
                        'Last name is required'}), 401    
    if not(json["username"].strip()):
        return jsonify({'Message':
                        'Username is required'}), 401
    if not(json["password"].strip()):
        return jsonify({'Message':
                        'Password is required'}), 401 
    return True


def validate_user_exist(json,users):
    if len(users)>0:
        for user in users:
            if json["email"] == user["email"]:
                return jsonify({"Message":'user with this email address exist'}),409
        for user in users:
            if json["username"] == user["username"]:
                return jsonify({"Message":"user with this username already exist"}), 409       
    return True

def validate_user_email(json):
    if not(validate_email(json["email"])):
        return jsonify({'Message':
                        'Enter a valid email'}), 401
    return True

def validate_question(json):
    if not(json["title"].strip()):
            return jsonify({'Message':
                            'Title is required'}), 401
    if not(json["content"].strip()):
        return jsonify({'Message':
                        'Content is required'}), 401

    return True

def validate_answer(json):
    # if not(json["username"].strip()):
    #         return jsonify({'Message':
    #                         'Username is required'}), 401
    # if not(json["question_id"].strip()):
    #     return jsonify({'Message':
    #                     'Question id is required'}), 401
    if not(json["answer_body"].strip()):
        return jsonify({'Message':
                        'Answer body is required'}), 401
    return True


