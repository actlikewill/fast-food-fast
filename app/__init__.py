"""
This file has the factory function for the app
"""
from flask import Flask, Blueprint
from instance.config import CONFIG



def create_app(config_name):
    """
    This takes in the app configuration and returns the application
    instance
    """
    app = Flask(__name__)
    app.config.from_object(CONFIG[config_name])
    CONFIG[config_name].init_app(app)
    from app.api.v1 import API_V1 as api_v1_blueprint
    app.register_blueprint(api_v1_blueprint, url_prefix='/api/v1')

    return app
