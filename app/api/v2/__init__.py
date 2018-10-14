"""
This initializes the blueprint for version 1 of the api
"""
from flask import Blueprint, jsonify

API_V2 = Blueprint('api_v2', __name__)

from .menu import menu_views
from .orders import order_views

@API_V2.app_errorhandler(404)
def not_found(err):
    return jsonify({"Error": "That route does not exist"}), 404

@API_V2.app_errorhandler(500)
def server_error(err):
    return jsonify({"Error": "The server encountered an internal error. Please try again"})
