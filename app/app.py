from flask_api import FlaskAPI
from flask import Flask, request, jsonify
from validate_email import validate_email
# from flask_restful import Resource, Api

from config import app_config

def create_app(config_name):

    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])

    @app.route("/api/v1/register", methods=["POST"])
    def register_new_user():

    return app