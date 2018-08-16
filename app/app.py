from flask import Flask, request, jsonify
from validate_email import validate_email
from datetime import datetime
from config import app_config
from app.models.questions import Question
from app.models.answers import Answer
from app.models.users import User


user = User()
question = Question('title', 'content')
# answer = Answer('answer_body')


def create_app(config_name):

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])

    @app.route("/api/v1/register", methods=["POST"])
    def register_new_user():
        request_data = request.get_json()
        user_id = str(len(user.users) + 1)
        first_name = request_data["first_name"]
        last_name = request_data["last_name"]
        username = request_data["username"]
        email = request_data["email"]
        password = request_data["password"]
        confirm_password = request_data["confirm_password"]
        is_valid_email = validate_email(email)
        if not(first_name.strip()):
            return jsonify({'Message':
                            'First name is required'}), 401
        if not(last_name.strip()):
            return jsonify({'Message':
                            'Last name is required'}), 401
        if not(username.strip()):
            return jsonify({'Message':
                            'Username is required'}), 401
        if not (is_valid_email):
            return jsonify({'Message':
                            'Enter valid email'}), 401
        if not(password.strip()):
            return jsonify({'Message':
                            'Password is required'}), 401
        if not(confirm_password.strip()):
            return jsonify({'Message':
                            'You must confirm your password'}), 401
        for usser in user.users:
            if username == usser["username"] or email == usser["email"]:
                return jsonify({"message": "User already exist"}), 409

        if(password != confirm_password):
            return jsonify({"message": "password mismatch"}), 409

        user.create_user(user_id, first_name, last_name,
                         username, email, password, confirm_password)

        return jsonify({
            'Message': 'User successfully created',
            'User': user.users[-1]}), 201

    @app.route("/api/v1/login", methods=["POST"])
    def login_user():
        request_data = request.get_json()
        username_or_email = request_data["username_or_email"]
        password = request_data["password"]
        for usser in user.users:
            if (usser["username"] == username_or_email or
                    usser["email"] == username_or_email) and usser["password"] == password:
                return jsonify({"message": "User logged in successfully", "User": usser}), 200

        return jsonify({"message": "Enter correct username or password"}), 404

    @app.route("/api/v1/question", methods=["POST"])
    def post_question():
        request_data = request.get_json()
        question_id = str(len(question.questions) + 1)
        title = request_data["title"]
        content = request_data["content"]
        date_posted=  datetime.now()
        if not(title.strip()):
            return jsonify({'Message':
                           'Title is required'}), 401
        if not(content.strip()):
            return jsonify({'Message':
                            'Content is required'}), 401
    
        question.post_question(question_id, title, content,date_posted)
        return jsonify({
                'Message': 'Question posted',
                'Question': question.questions[-1]}), 201

    @app.route("/api/v1/questions", methods=["GET"])
    def get_all_questions():
        return jsonify({"Questions":question.questions}),200


    @app.route("/api/v1/question/<id>", methods=["GET"])
    def get_a_question_by_id(id):
        for quest in question.questions:
            if id == quest["question_id"]:
                return jsonify({"message":"Question found"}),200
        return jsonify({"message":"Question not found"}),404

    return app
