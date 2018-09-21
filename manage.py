"""This creates runs the application"""

from flask_script import Manager
from app import create_app

APP = create_app('default')
MGR = Manager(APP)

if __name__ == '__main__':
    MGR.run()
