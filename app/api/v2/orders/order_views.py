import psycopg2
from flask import request
from flask_restful import Resource, Api
from ....db.db import save_to_db, fetch_all_from_db, fetch_one_from_db
from .. import API_V2
from flask_jwt_extended import jwt_required, get_jwt_identity
from .order_models import Orders
from ..menu.menu_models import Menu
from ...v1.helpers.helpers import get_dict_item
from datetime import datetime

API_V2 = Api(API_V2)

class PlaceOrder(Resource):
    @staticmethod
    @jwt_required
    def post():
        current_user = get_jwt_identity()
        ordered_by = current_user['user']
        menu_list = Menu.get_menu_list()
        menu_keys = Menu.get_menu_keys()
        details = request.get_json()
        if not details:
            return {"Error": "You did not enter anything"}, 400
        price = 0

        order_keys = []
        for key in details.keys():
            order_keys.append(key)

        out_of_stock = set(order_keys) - set(menu_keys)

        try:
            if not out_of_stock:
                order_details = ''
                for item, quantity in details.items():
                    menu_item = get_dict_item(menu_list, 'menu_item', item)
                    price += int(menu_item[0]['price']) * quantity
                    order_details += "{} - {}, ".format(item, quantity)

                new_order = {
                    "ordered_by":ordered_by,
                    "date_ordered":datetime.now().strftime("%d/%m/%y %H:%M:%S"),
                    "details":order_details,
                    "price":price,
                    "status":"pending"
                }
                query = Orders.add_order_query(new_order)

                save_to_db(query)

                return {"Success":new_order}, 201
        except TypeError:          
           return {"SyntaxError":"You did not enter data correctly. The value needs to be an integer"},400
        string = ''
        for i in out_of_stock:
            string += "{}, ".format(i)
        return {"Error":"The following items are not on the menu. {}. Enter a menu_item as key, and an integer quantity as the value: '<menu_item>':'<quantity>'.".format(string)}, 404

    @staticmethod
    @jwt_required
    def get():
        current_user = get_jwt_identity()
        ordered_by = current_user['user']
        query = Orders.get_user_orders(ordered_by)
        orders = fetch_all_from_db(query)
        if not orders:
            return {"Sorry": "No orders exist"}, 200

        return {"Orders": orders}, 200

class GetSingleOrder(Resource):
    @staticmethod
    @jwt_required
    def get(order_id):
        current_user = get_jwt_identity()
        if current_user['role'] != 'admin':
            return {"Sorry": "Only admin allowed access to this route."}, 403
        query = Orders.get_single_order(order_id)
        order = fetch_one_from_db(query)

        return {"Your Order": order}, 200

    @staticmethod
    @jwt_required
    def put(order_id):
        current_user = get_jwt_identity()
        if current_user['role'] != 'admin':
            return {"Sorry": "Only admin allowed access to this route."}, 403

        try:
            data = request.get_json()
            status = data['status']
            query = Orders.update_order_status(status, order_id)
            save_to_db(query)
            success_message = " Order Updated"
            return {"Success": success_message}, 201
        except(KeyError, TypeError):
            return {"Error": "you did not enter data correctly. Required key is 'status'"}, 400
        except(psycopg2.ProgrammingError):
            return {"Syntax Error": "You have a syntax error"}, 400

class GetAllOrders(Resource):
    @staticmethod
    @jwt_required
    def get():
        current_user = get_jwt_identity()
        if current_user['role'] != 'admin':
            return {"Sorry": "Only admin allowed access to this route."}, 403
        query = Orders.get_all_orders()
        rows = fetch_all_from_db(query)
        if not rows:
            return {"Sorry": "No orders exist"}, 200

        orders = []
        
        for item in rows:
            order = {
            "order_id":item[0],
            "ordered_by":item[1],
            "date_ordered":item[2],
            "details":item[3],
            "price":item[4],
            "status":item[5]
            }
            orders.append(order)      

        return {"Orders": orders}, 200

API_V2.add_resource(PlaceOrder, '/users/orders', endpoint='orders')
API_V2.add_resource(GetSingleOrder, '/orders/<order_id>', endpoint='order')
API_V2.add_resource(GetAllOrders, '/orders', endpoint='get_all_order')



