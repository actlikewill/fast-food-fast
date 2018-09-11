"""
This creates the endpoints for the requests made by to the API.
The user should be able to place orders, fetch a specific order
using its Id and update the status of an existing order.
"""
from flask import request, jsonify, abort
from app import app
from app.models import Orders

ORDERS = Orders()

@app.route('/api/v1/orders', methods=['GET'])
def get_orders():
    """
    Fetches a list of all orders
    """
    return jsonify({"orders": ORDERS.order_list})

@app.route('/api/v1/orders', methods=['POST'])
def place_order():
    """
    Creates an order object for using the arguments passed
    """
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
    return jsonify({"Place Order": order}), 201

@app.route('/api/v1/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    """
    Gets a specific order from the order list using its unique Id
    """
    orders = ORDERS.order_list
    order = [order for order in orders if order['order_id'] == order_id]
    if not order:
        abort(404)
    return jsonify({'order': order[0]})

@app.route('/api/v1/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    """
    Updates the order status
    """
    orders = ORDERS.order_list
    if not orders:
        abort(404)
    order = [order for order in orders if order['order_id'] == order_id]
    if not order:
        abort(404)
    order[0]['status'] = request.args.get('status')
    return jsonify({'Updated order': order[0]}), 201

@app.errorhandler(404)
def not_found(error):
    """Special error handler"""
    return jsonify({"error":"Not found"}), error.code
