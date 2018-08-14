from flask_api import FlaskAPI
from flask import request, jsonify

from app.instance.config import app_config



def create_app(config_name):

    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    
    return app

  

      