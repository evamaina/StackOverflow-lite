# from flask_api import FlaskAPI
from flask import Flask, request, jsonify
from validate_email import validate_email
from datetime import datetime
from config import app_config
from app.models.questions import Question
from app.models.answers import Answer
from app.models.users import User


user = User()
# question = Question('title', 'content')
# answer = Answer('answer_body')


def create_app(config_name):

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])

    @app.route("/api/v1/register", methods=["POST"])
    def register_new_user():
        pass
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

        user.create_user(user_id, first_name,last_name,username, email, password,confirm_password)

        return jsonify({
                'Message': 'User successfully created',
                'User': user.users[-1]}), 201

    
    
    return app

    
