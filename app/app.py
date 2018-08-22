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

user = User()
question = Question()
answer = Answer()


def create_app(config_name):

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
