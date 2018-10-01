"""
This initializes the blueprint for version 1 of the api
"""
from flask import Blueprint

API_V1 = Blueprint('api_v1', __name__)

from .orders import order_views
from .menu import menu_views