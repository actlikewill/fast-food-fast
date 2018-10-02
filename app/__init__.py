"""
This file has the factory function for the app
"""
from flask import Flask, Blueprint
from instance.config import CONFIG
from .db.db import create_tables
from flask_jwt_extended import JWTManager



def create_app(config_name):
    """
    This takes in the app configuration and returns the application
    instance
    """
    app = Flask(__name__)
    app.config.from_object(CONFIG[config_name])
    CONFIG[config_name].init_app(app)
    create_tables()
    from app.api.v1 import API_V1 as api_v1_blueprint
    app.register_blueprint(api_v1_blueprint, url_prefix='/api/v1')
    from app.api.auth import AUTH as auth
    app.register_blueprint(auth, url_prefix='/auth')

    return app
