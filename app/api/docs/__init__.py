"""
This initializes the blueprint for the docs
"""
from flask import Blueprint, redirect

HOME = Blueprint('home', __name__)


@HOME.route('/')
def index():
    return redirect('https://fastfoodfast18.docs.apiary.io')
    