from flask import Flask, request, jsonify
from validate_email import validate_email
from datetime import datetime
from config import app_config
from app.models.questions import Question
from app.models.answers import Answer
from app.models.users import User
from app.common.validation import *


user = User()
question = Question('title', 'content')
answer = Answer('answer_body', 'username')


def create_app(config_name):

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])

    @app.route("/api/v1/register", methods=["POST"])
    def register_new_user():
        request_data = request.get_json()
        user_id = str(len(user.users) + 1)
        validate_user_msg = validate_user_registration(request_data)
        if(validate_user_msg != True):
            return validate_user_msg
        valid_email = validate_user_email(request_data)
        if(valid_email != True):
            return valid_email

        validate_user_exist_msg = validate_user_exist(request_data, user.users)
        if(validate_user_exist_msg != True):
            return validate_user_exist_msg

        user.create_user(user_id, request_data["first_name"], request_data["last_name"],
                         request_data["username"], request_data["email"], request_data["password"])

        return jsonify({
            'Message': 'User successfully created',
            'User': user.users[-1]}), 201

    @app.route("/api/v1/login", methods=["POST"])
    def login_user():
        request_data = request.get_json()
        username_or_email = request_data["username_or_email"]
        password = request_data["password"]
        for person in user.users:
            if (person["username"] == username_or_email or
                    person["email"] == username_or_email) and person["password"] == password:
                if(person["login_status"] == False):
                    person["login_status"] = True
                    return jsonify({"message": "User logged in successfully", "User": person}), 200
                else:
                    return jsonify({"message": "User Already Logged in", "User": person}), 409
            return jsonify({"message": "Enter correct username or password"}), 404
        return jsonify({"message": "User does not exist"}), 404

    @app.route('/api/v1/logout', methods=['POST'])
    def logout_user():
        request_data = request.get_json()
        username_or_email = request_data['username_or_email']
        for person in user.users:
            if (person["username"] == username_or_email or
                    person["email"] == username_or_email) and person["login_status"] == True:
                person["login_status"] = False
                return jsonify({'Message': 'User logged out successfully.'}), 200

        return jsonify({'Message': 'User is not logged in, please login.'}), 401

    @app.route("/api/v1/users", methods=["GET"])
    def get_all_users():
        return jsonify({"Users": user.users}), 200

    @app.route("/api/v1/question", methods=["POST"])
    def post_question():
        request_data = request.get_json()
        question_id = str(len(question.questions) + 1)
        title = request_data["title"]
        content = request_data["content"]
        date_posted = datetime.now()
        validate_question_msg = validate_question(request_data)

        if(validate_question_msg != True):
            return validate_question_msg

        for quest in question.questions:
            if title == quest["title"]:
                return jsonify({"message": "Question already asked", "Question": quest}), 409
        for person in user.users:
            if person["login_status"] == True:
                question.post_question(
                    question_id, title, content, date_posted)
                return jsonify({
                    'Message': 'Question posted',
                    'Question': question.questions[-1]}), 201
        return jsonify({"message": "Login to post a question"}), 400

    @app.route("/api/v1/questions", methods=["GET"])
    def get_all_questions():
        return jsonify({"Questions": question.questions}), 200

    @app.route("/api/v1/question/<id>", methods=["GET"])
    def get_a_question_by_id(id):
        for quest in question.questions:
            if id == quest["question_id"]:
                return jsonify({"message": "Question found", "Question": quest}), 200
        return jsonify({"message": "Question not found"}), 404

    @app.route("/api/v1/answer/<questionId>", methods=["POST"])
    def add_answer(questionId):
        request_data = request.get_json()
        answer_id = str(len(answer.answers) + 1)
        question_id = request_data["question_id"]
        answer_body = request_data["answer_body"]
        username = request_data["username"]
        date_posted = datetime.now()
        validate_answer_msg = validate_answer(request_data)
        if(validate_answer_msg != True):
            return validate_answer_msg

        if(questionId != question_id):
            return jsonify({"Message": "Enter correct id"}), 409

        for quest in question.questions:
            if int(questionId) == int(quest["question_id"]):
                for person in user.users:
                    if person["login_status"] == True:
                        answer.post_answer(answer_id, question_id,
                                           answer_body, username, date_posted)
                        return jsonify({"Message": "Answer added successfully",
                                        "Answer": answer.answers[-1]}), 200
                    return jsonify({"message": "Login to post a answer"}), 400
            return jsonify({"Message": "Question with that id not found"}), 404

    @app.route("/api/v1/answers/<questionId>", methods=["GET"])
    def get_all_answers(questionId):
        return jsonify({"Answers": answer.answers}), 200

    return app
