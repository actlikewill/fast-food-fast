from app import app
from flask import request

@app.route('/', methods=['GET'])
def index():
    return 'Hello World'