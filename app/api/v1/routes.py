"""
This creates the resources and endpoints for the api
"""
from flask import jsonify, request
from flask_restful import Resource, Api, abort
from . import  API_V1
from .models import Orders, Menu

API = Api(API_V1)
ORDERS = Orders()
MENU = Menu()



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
        # if not request.args:
        #     return jsonify({"sorry":"no arguments passed"})
        # if not request.args.get('item'):
        #     return jsonify({"sorry":"no item argument passed"})
        # if not request.args.get('quantity'):
        #     return jsonify({"sorry":"no quantity argument passed"})

        json_data = request.get_json()
        order = {
            "item": json_data['item'],
            "quantity": json_data['quantity'],
            "order_id":len(ORDERS.order_list) + 1,
            "status": json_data['status']
        }
        ORDERS.add_order(order)
        return {"Order Placed": order}, 201

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


class GetMenu(Resource):
    @classmethod
    def get(cls):
        return {"Menu": MENU.menu}
    
    @classmethod
    def post(cls):
        json_data = request.get_json()
        new_menu_item = {
            "menu_id": len(MENU.menu) + 1,
            "menu_item": json_data["menu_item"],
            "price": json_data["price"]
        }
        MENU.add_menu_item(new_menu_item)
        return {"Menu item added": new_menu_item}

API.add_resource(GetOrders, '/orders', endpoint='orders')
API.add_resource(SingleOrder, '/orders/<int:order_id>', endpoint='order')
API.add_resource(GetMenu, '/menu', endpoint='menu')

