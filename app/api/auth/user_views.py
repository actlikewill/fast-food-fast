"""
This is the users view which will handle login and
token generation
"""

import psycopg2
from . import AUTH
from flask_jwt_extended import (
    jwt_required, create_access_token,
    get_jwt_identity
)
from flask_restful import Resource, Api
from instance.config import Config
from .user_models import Users
from ...db.db import connect
from flask import request, jsonify, make_response

secret = Config().SECRET_KEY
AUTH = Api(AUTH)

class LoginUser(Resource):
    """This class handles user login request and token generation"""
    @staticmethod
    def post():
        """
        The login function generates the access token
        The payload consists of the username and the role
        """
        data = request.get_json()

        if not data or not data['username'] or not data['password']:
            return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

        query = Users.get_user_query(data['username'])

        conn = connect()
        cur = conn.cursor()
        cur.execute(query)
        row = cur.fetchone()

        if not row:
            return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

        dbusername = row[0]
        dbpassword = row[1]
        dbrole = row[2]
        
        if data['password'] != dbpassword:
            return {"Error":"Invalid Password"}, 401
        token = create_access_token(identity={"user":dbusername, "role":dbrole})

        return {"token": token}, 200

class GetUser(Resource):
    """
    This class handle the queries to the users table
    """
    @staticmethod
    @jwt_required
    def get():
        """Gets all user. Only available to admin"""

        current_user = get_jwt_identity()
        role = current_user['role']
        if role != 'admin':
            return {"Sorry": "Route restricted to admin only"}, 403

        query = Users.get_all_users_query()
        conn = connect()
        cur = conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
    
        return {"Users" : rows}

    @staticmethod
    def post():
        """
        This handles the creation of new users
        """
        try:
            data = request.get_json()
            query = Users.insert_user_query(data)
            user = data['username']
            conn = connect()
            cur = conn.cursor()
            cur.execute(query)
            cur.close()
            conn.commit()
            success_message = """ User {} Created""".format(user)
            return  {"Success": success_message}, 201
        except KeyError:
            return {"Error":"You did not enter data correctly"}, 400
        except(psycopg2.ProgrammingError):
            return {"Syntax Error":"You did not format data correctly. "}, 400


class GetSingleUser(Resource):
    @staticmethod
    @jwt_required
    def get(user_id):
        """This fetches a single user given the id"""

        current_user = get_jwt_identity()
        role = current_user['role']
        if role != 'admin':
            return {"Sorry": "Route restricted to admin only"}, 403
        query = Users.get_user_query_id(user_id)
        conn = connect()
        cur = conn.cursor()
        cur.execute(query)
        user = cur.fetchone()

        return {"User": user}


AUTH.add_resource(LoginUser, '/login', endpoint='user')
AUTH.add_resource(GetUser, '/users', endpoint='getusers')
AUTH.add_resource(GetSingleUser, '/users/<user_id>', endpoint='getuser')