"""
This initializes the blueprint for version 1 of the api
"""
from flask import Blueprint

AUTH = Blueprint('AUTH', __name__)

from .auth import user_views 
