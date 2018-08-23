from flask import Flask, request, jsonify
from validate_email import validate_email
from datetime import datetime
from config import app_config
from app.models.questions import Question
from app.models.answers import Answer
from app.models.users import User
from app.common.validation import *
from app.manage import Database

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

        user = User(first_name,last_name,username,email,password)
        user.save_user()
        query = "SELECT  user_id FROM users WHERE email=%s"
        cursor = db_connection.cursor()
        row = cursor.execute(query, (email,))
        user_id = cursor.fetchone()
        token = User.token_generator(user_id)
    
        
        return jsonify({'Message':
                        "User successfully created","token": str(token)}), 201

    db_connection.create_tables()

    @app.route("/api/v2/login", methods=["POST"])
    def login_user():
        request_data = request.get_json()
        username = request_data["username"]
        password = request_data["password"]
        query = "SELECT * FROM users WHERE username=%s AND password=%s;"
        cursor = db_connection.cursor()
        cursor.execute(query, (username,password))
        row = cursor.fetchone()
        if row:
            return jsonify({"message": "User logged in successfully"}), 200
        return jsonify({"message": "Enter correct username or password"}), 401   


    
    return app