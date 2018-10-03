import psycopg2
from flask import request
from flask_restful import Resource, Api
from ....db.db import connect
from .. import API_V2
from flask_jwt_extended import jwt_required, get_jwt_identity
from .menu_models import Menu

API_V2 = Api(API_V2)

class GetMenu(Resource):
    @staticmethod
    def get():
        query = Menu.get_all_menu_query()
        conn = connect()
        cur = conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        if not rows:
            return {"Sorry": "No Items in the menu yet."}, 200
        return {"Menu": rows}, 200

    @staticmethod
    @jwt_required
    def post():
        current_user = get_jwt_identity()
        role = current_user['role']
        if role != 'admin':
            return {"Sorry": "Route restricted to admin only"}, 403
        try:
            data = request.get_json()
            query = Menu.add_menu_query(data)
            item = data['menu_item']
            conn = connect()
            cur = conn.cursor()
            cur.execute(query)
            cur.close()
            conn.commit()
            success_message = """ Menu Item {} Created""".format(item)
            return {"Success": success_message}, 201
        except(KeyError, TypeError):
            return {"Error": "you did not enter data correctly"}, 400
        except psycopg2.ProgrammingError:
            return {"SyntaxError": "you did not enter data correctly"}, 400

API_V2.add_resource(GetMenu, '/menu')
