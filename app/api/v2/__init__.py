"""
This initializes the blueprint for version 1 of the api
"""
from flask import Blueprint

API_V2 = Blueprint('api_v2', __name__)

from .menu import menu_views 
