from flask import Flask, request, jsonify
from validate_email import validate_email
from datetime import datetime
from config import app_config
from app.models.questions import Question
from app.models.answers import Answer
from app.models.users import User
from app.common.validation import *
from app.manage import Database
from app.common.authentication import jwt_required
from werkzeug.security import check_password_hash
db_connection = Database()


def create_app(config_name):

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])

    @app.route("/api/v2/signup", methods=["POST"])
    def register_new_user():
        request_data = request.get_json()
        first_name = request_data["first_name"]
        last_name = request_data["last_name"]
        username = request_data["username"]
        email = request_data["email"]
        password = request_data["password"]
        confirm_password= request_data["confirm_password"]


        validate_email_exist_msg = validate_email_exist(email)
        if(validate_email_exist_msg == True):
            return jsonify({'Message':'user with this email address exist'}),409    
        validate_username_exist_msg = validate_username_exist(username)
        if(validate_username_exist_msg == True):
            return jsonify({"Message":"user with this username already exist"}),409
        validate_user_msg = validate_user_registration(request_data)
        if(validate_user_msg != True):
            return validate_user_msg
        valid_email = validate_user_email(request_data)
        if(valid_email != True):
            return valid_email
        if password != confirm_password:
            return jsonify({"Message":"Password mismatch"})
        user = User(first_name,last_name,username,email,password)
        user.save_user()
        query = "SELECT  user_id FROM users WHERE email=%s"
        cursor = db_connection.cursor()
        row = cursor.execute(query, (email,))
        user_id = cursor.fetchone()
        token = User.token_generator(user_id)   
        return jsonify({'Message':
                        "User successfully created","token": token.decode()}), 201

    

    @app.route("/api/v2/login", methods=["POST"])
    def login_user():
        request_data = request.get_json()
        username = request_data["username"]
        password = request_data["password"]
        query = "SELECT username, password FROM users WHERE username=%s;"
        cursor = db_connection.cursor()
        cursor.execute(query,(username,))
        row = cursor.fetchone()
        if row:
            if check_password_hash(row['password'], password):
                query = "SELECT  user_id FROM users WHERE username=%s"
                row = cursor.execute(query, (username,))
                user_id = cursor.fetchone()
                token = User.token_generator(user_id) 
                return jsonify({"message": "User logged \
                              in successfully", "token":token.decode()}), 200
            return jsonify('wrong password, eneter correct password'),401
        return jsonify({"message": "Enter correct username"}), 401

    
    @app.route("/api/v2/question", methods=["POST"])
    @jwt_required
    def post_question(user_id):
        request_data = request.get_json()
        title = request_data["title"]
        content = request_data["content"]
        posted_date = datetime.now()
        validate_question_msg = validate_question(request_data)

        if(validate_question_msg != True):
            return validate_question_msg
        question = Question(user_id['user_id'],title,content,posted_date)
        query = 'SELECT title FROM questions WHERE title=%s'
        cursor = db_connection.cursor()
        cursor.execute(query, (title,))
        row = cursor.fetchone()
        if not row:
            question.save_question()
            return jsonify({'Message': 'Question posted'}), 200
        return jsonify({"message": "Question already asked"}), 409

    
    @app.route("/api/v2/questions/<question_id>/answers", methods=["POST"])
    @jwt_required
    def add_answer(question_id, user_id):
        request_data = request.get_json()
        answer_body = request_data["answer_body"]
        posted_date = datetime.now()
        validate_answer_msg = validate_answer(request_data)
        if(validate_answer_msg != True):
            return validate_answer_msg

        answer = Answer(answer_body, int(question_id), posted_date,user_id['user_id'])
        query = 'SELECT question_id FROM questions WHERE question_id=%s;'
        query1 = 'SELECT answer_body FROM answers WHERE answer_body=%s;'
        cursor = db_connection.cursor()
        cursor.execute(query, (question_id,))
        row = cursor.fetchall()
        if row:
            cursor.execute(query1, (answer_body,))
            row1 = cursor.fetchall()
            if row1:
                return jsonify({"message": "answer already exist"}), 409
            answer.save_answer()
            return jsonify({"Message": "Answer added successfully"}), 200
        return jsonify({"message": "Question does not exist"}), 400

    @app.route("/api/v2/questions", methods=["GET"])
    def fetch_all_questions():
        query ='SELECT * FROM questions'
        cursor = db_connection.cursor()
        cursor.execute(query)
        row = cursor.fetchall()
        if row:
            return jsonify({"Questions": row}), 200
        return jsonify({"Questions": "No questions found"}), 404

    @app.route("/api/v2/question/<question_id>", methods=["GET"])
    def get_a_question_by_id(question_id):
        query = 'SELECT * FROM questions WHERE question_id=%s;'
        query1 = 'SELECT * FROM answers WHERE question_id=%s;'
        cursor = db_connection.cursor()
        cursor.execute(query, (question_id,))
        row = cursor.fetchone()
        cursor.execute(query1, (question_id,))
        row1 = cursor.fetchall()
        if row1:
            answers = row1
        answers = row1
        if row:
            row['answers'] = answers
            return jsonify({"Question": row}), 200
        return jsonify({"Questions": "Not question found"}), 404

    @app.route("/api/v2/question/<question_id>", methods=["DELETE"])
    @jwt_required
    def delete_question(question_id, user_id):
        cursor = db_connection.cursor()
        query2 = 'SELECT user_id from questions WHERE question_id=%s'
        cursor.execute(query2, question_id)
        row2 = cursor.fetchone()
        if not row2:
            return jsonify('question does not exist')
        if row2['user_id'] != user_id['user_id']:
            return jsonify({"Message":"you cant delete this"})
        query = 'SELECT * FROM questions WHERE question_id=%s;'
        query1 = 'DELETE FROM questions WHERE question_id=%s;'
    
        cursor.execute(query, (question_id,))
        row = cursor.fetchone()
        if row:
            cursor.execute(query1, (question_id,))
            db_connection.commit()
            return jsonify({"Question":"Question delete successfully" }), 200
        return jsonify({"Questions": "No question found"}), 404

    @app.route("/api/v2/question/<question_id>/answers/<answer_id>", methods=["PUT"])
    @jwt_required
    def accept_or_update_answer(question_id, answer_id, user_id):
        ''''''
        query = "SELECT * FROM questions WHERE question_id=%s"
        query1 ="SELECT * FROM answers WHERE answer_id = %s"
        cursor = db_connection.cursor()
        cursor.execute(query, question_id)
        row = cursor.fetchone()
        if row:
            if row['user_id'] == user_id['user_id']:
                query3 = "UPDATE answers SET accepted = true WHERE question_id=%s;"
                cursor.execute(query3, question_id)
                db_connection.commit()
                return jsonify({"Message":"answer accepted"})
            cursor.execute(query1, answer_id)
            row1 = cursor.fetchone()
            if not row1:
                return jsonify({"message":"no answer"}),404
            answer_body = request.json.get("answer_body")
            if row1['user_id'] == user_id['user_id']:
                cursor.execute('UPDATE answers SET answer_body=%s WHERE answer_id=%s', (answer_body, answer_id))
                db_connection.commit()
            return jsonify({"Message":"answer updated"})
        return  jsonify('question not found')          
    db_connection.create_tables()
    return app

        