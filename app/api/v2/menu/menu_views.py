import psycopg2
from flask import request
from flask_restful import Resource, Api
from ....db.db import save_to_db, fetch_all_from_db
from .. import API_V2
from flask_jwt_extended import jwt_required, get_jwt_identity
from .menu_models import Menu

API_V2 = Api(API_V2)

class GetMenu(Resource):
    @staticmethod
    def get():
        query = Menu.get_all_menu_query()
        rows = fetch_all_from_db(query)
        if not rows:
            return {"Sorry": "No Items in the menu yet."}, 200

        menu = []

        for item in rows:
            menu_item = {
                "menu_id":item[0],
                "menu_item":item[1],
                "description":item[2],
                "price":item[3]
            }
            menu.append(menu_item)
        return {"Menu": menu}, 200

    @staticmethod
    @jwt_required
    def post():
        current_user = get_jwt_identity()
        role = current_user['role']
        if role != 'admin':
            return {"Sorry": "Route restricted to admin only"}, 403
        try:
            data = request.get_json()
            item = data['menu_item']
            query = Menu.add_menu_query(data)
            save_to_db(query)
            success_message = """ Menu Item {} Created""".format(item)
            return {"Success": success_message}, 201
        except(KeyError, TypeError):
            return {"Error": "you did not enter data correctly"}, 400
        except psycopg2.ProgrammingError:
            return {"SyntaxError": "you did not enter data correctly"}, 400

API_V2.add_resource(GetMenu, '/menu')
