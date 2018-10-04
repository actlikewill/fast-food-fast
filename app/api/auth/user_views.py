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
from .user_models import Users
from ...db.db import fetch_all_from_db, fetch_one_from_db, save_to_db
from flask import request, make_response

AUTH = Api(AUTH)

class LoginUser(Resource):
    """This class handles user login request and token generation"""
    @staticmethod
    def post():
        """
        The login function generates the access token
        The payload consists of the username and the role
        """
        try:
            data = request.get_json()

            if not data or not data['username'] or not data['password']:
                return {"Error":"Please enter a username and password"}, 401

            query = Users.get_user_query(data['username'])

            row = fetch_one_from_db(query)

            if not row:
                return {"Sorry":"User not found"}, 404

            dbusername = row[0]
            dbpassword = row[1]
            dbrole = row[2]

            if data['password'] != dbpassword:
                return {"Error":"Your username and/or password are incorrect"}, 401
            token = create_access_token(identity={"user":dbusername, "role":dbrole})

            return {"msg":"Login Successful", "token": token}, 200
        except KeyError:
            return {"Error": "You did not enter data correctly"}, 400

class GetUser(Resource):
    """
    This class handle the queries to the users table
    """
    @staticmethod
    @jwt_required
    def get():
        """Gets all users. Only available to admin"""

        current_user = get_jwt_identity()
        role = current_user['role']
        if role != 'admin':
            return {"Sorry": "Route restricted to admin only"}, 403

        query = Users.get_all_users_query()
        rows = fetch_all_from_db(query)

        users = []

        for item in rows:
            user = {
                "user_id":item[0],
                "user_name":item[1],
                "user_email":item[2]
            }
            users.append(user)

        return {"Users" : users}

    @staticmethod
    def post():
        """
        This handles the creation of new users
        """
        try:
            data = request.get_json()
            user = data['username']

            query = Users.insert_user_query(data)
            save_to_db(query)

            success_message = """ User {} Created""".format(user)
            return  {"Success": success_message}, 201
        except KeyError:
            return {"Error":"You did not enter data correctly"}, 400
        except psycopg2.ProgrammingError:
            return {"Syntax Error":"You did not format data correctly. "}, 400
        except psycopg2.IntegrityError:
            return {"Error":"A username with those credentials already exists"}, 401


class GetSingleUser(Resource):
    @staticmethod
    @jwt_required
    def get(user_id):
        """This fetches a single user given the id"""

        current_user = get_jwt_identity()
        role = current_user['role']
        if role != 'admin':
            return {"Sorry": "Route restricted to admin only"}, 403
        try:
            query = Users.get_user_query_id(user_id)
            row = fetch_one_from_db(query)    
            if not row:
                return {"Sorry": "User not found"}, 404

            user = {
                "user_id":row[0],
                "user_name":row[1],
                "email":row[2]
            }

            return {"User": user}
        except psycopg2.DataError:
            return {"Error":"Integer required"}, 400


AUTH.add_resource(LoginUser, '/login', endpoint='user')
AUTH.add_resource(GetUser, '/users', endpoint='getusers')
AUTH.add_resource(GetSingleUser, '/users/<user_id>', endpoint='getuser')
