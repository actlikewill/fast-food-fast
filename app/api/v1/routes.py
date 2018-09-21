"""
This creates the resources and endpoints for the api
"""
from flask import jsonify, request
from flask_restful import Resource, Api, abort
from . import  API_V1
from .models import Orders

API = Api(API_V1)

ORDERS = Orders()

class GetOrders(Resource):
    """This responds to queries to the whole order class"""
    def get(self):
        """This gets the list of all orders if any"""
        orders = ORDERS.order_list
        if not orders:
            return {"sorry": "no orders yet"}
        return {'Orders': ORDERS.order_list}

    def post(self):
        """This receives arguments and creates an order"""
        if not request.args:
            return jsonify({"sorry":"no arguments passed"})
        if not request.args.get('item'):
            return jsonify({"sorry":"no item argument passed"})
        if not request.args.get('quantity'):
            return jsonify({"sorry":"no quantity argument passed"})
        order = {
            "item": request.args.get('item'),
            "quantity": request.args.get('quantity'),
            "order_id":len(ORDERS.order_list) + 1,
            "status": "Pending"
        }
        ORDERS.add_order(order)
        return {"Order Placed": order}, 201

class SingleOrder(Resource):
    """This responds to single order requests using the unique order id"""
    def get(self, order_id):
        """Returns a single order"""
        orders = ORDERS.order_list
        order = [order for order in orders if order['order_id'] == order_id]
        if not order:
            abort(404, message='error')
        return {'Your order': order[0]}


    def put(self, order_id):
        """Updates a single order"""
        orders = ORDERS.order_list
        if not orders:
            abort(404, message='error')
        order = [order for order in orders if order['order_id'] == order_id]
        if not order:
            abort(404, message='error')
        order[0]['status'] = request.args.get('status')
        return {'Updated order': order[0]}, 201

API.add_resource(GetOrders, '/orders', endpoint='orders')
API.add_resource(SingleOrder, '/orders/<int:order_id>', endpoint='order')
