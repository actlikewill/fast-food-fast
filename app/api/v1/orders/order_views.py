"""
This creates the resources and endpoints for the api
"""
from flask import request
from flask_restful import Resource, Api, abort
from .. import  API_V1
from .order_models import Orders
from ..menu.menu_views import MENU

API = Api(API_V1)
ORDERS = Orders()

class GetOrders(Resource):
    """This responds to queries to the whole order class"""
    @classmethod
    def get(cls):
        """This gets the list of all orders if any"""
        orders = ORDERS.order_list
        if not orders:
            return {"sorry": "no orders yet"}
        return {'Orders': ORDERS.order_list}
        
    @classmethod
    def post(cls):
        """This receives arguments and creates an order"""
        order_data = request.get_json()      
        menu = MENU.menu
        menu_list = []
        order_keys = []
        price = 0
        new_order = {}

        for menu_item in menu:
            menu_list.append(menu_item['menu_item'])

        for key in order_data.keys():
            order_keys.append(key)

        not_available = set(order_keys) - set(menu_list)

        if not not_available:                
            for key, value in order_data.items():   
                menu_item = [menu_item for menu_item in menu if menu_item['menu_item'] == key]
                price += menu_item[0]['price'] * value   
                new_order[key] = value

            new_order['order_id'] = len(ORDERS.order_list) + 1
            new_order['status'] = "pending"
            new_order['total_price'] = price
            ORDERS.add_order(new_order)
            return {"Your_order": new_order}, 201
        string = ''
        for i in not_available:
            string += "{}, ".format(i)
        return {"Error":"The following items are not on the menu. {}".format(string)} , 404       

class SingleOrder(Resource):
    """This responds to single order requests using the unique order id"""
    @classmethod
    def get(cls, order_id):
        """Returns a single order"""
        orders = ORDERS.order_list
        order = [order for order in orders if order['order_id'] == order_id]
        if not order:
            abort(404, message='error')
        return {'Your order': order[0]}

    @classmethod
    def put(cls, order_id):
        """Updates a single order"""
        orders = ORDERS.order_list
        if not orders:
            abort(404, message='error')
        order = [order for order in orders if order['order_id'] == order_id]
        if not order:
            abort(404, message='error')
        json_data = request.get_json()
        order[0]['status'] = json_data['status']
        return {'Updated order': order[0]}, 201

API.add_resource(GetOrders, '/orders', endpoint='orders')
API.add_resource(SingleOrder, '/orders/<int:order_id>', endpoint='order')
