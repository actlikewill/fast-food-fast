from app import app
from flask import request, jsonify, abort
from app.models import Orders

OrderClass = Orders()



@app.route('/api/v1/orders', methods=['GET'])
def get_orders():    
    return jsonify({"orders": OrderClass.order_list})

@app.route('/api/v1/orders', methods=['POST'])
def place_order():
    order = {
        "item": request.args.get('item'),
        "quantity": request.args.get('quantity'),
        "orderId":len(OrderClass.order_list) + 1        
    }
    OrderClass.add_order(order)
    return jsonify({"Place Order": order}), 201

@app.route('/api/v1/orders/<int:orderId>', methods=['GET'])
def get_order(orderId):
    orders = OrderClass.order_list
    order = [order for order in orders if order['orderId'] == orderId]
    if len(order) == 0:
        abort(404)
    return jsonify({'order': order[0]})
