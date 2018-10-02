"""
This initializes the blueprint for authorizing and genrating tokens
"""
from flask import Blueprint

AUTH = Blueprint('auth', __name__)

from . import user_views
