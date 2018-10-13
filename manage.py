"""This runs the application"""

from flask_script import Manager
from app import create_app
from flask_jwt_extended import JWTManager
from flask_cors import CORS

APP = create_app('default')
JWT = JWTManager(APP)
MGR = Manager(APP)
cors = CORS(APP)

if __name__ == '__main__':
    MGR.run()
