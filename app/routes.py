from app import app
from flask import request, jsonify, abort, make_response
from app.models import Orders

OrderClass = Orders()



@app.route('/api/v1/orders', methods=['GET'])
def get_orders():    
    return jsonify({"orders": OrderClass.order_list})

@app.route('/api/v1/orders', methods=['POST'])
def place_order():
    if  not request.args:    
        return jsonify({"sorry":"no arguments passed"})
    elif not request.args.get('item'):
        return jsonify({"sorry":"no item argument passed"})
    elif not request.args.get('quantity'):
        return jsonify({"sorry":"no quantity argument passed"})
    else:
        order = {
            "item": request.args.get('item'),
            "quantity": request.args.get('quantity'),
            "orderId":len(OrderClass.order_list) + 1,
            "status": "Pending"        
        }
        OrderClass.add_order(order)
        return jsonify({"Place Order": order}), 201

@app.route('/api/v1/orders/<int:orderId>', methods=['GET'])
def get_order(orderId):
    orders = OrderClass.order_list
    order = [order for order in orders if order['orderId'] == orderId]
    if not order:
        abort(404)
    return jsonify({'order': order[0]})

@app.route('/api/v1/orders/<int:orderId>', methods=['PUT'])
def update_order(orderId):
    orders = OrderClass.order_list
    if len(orders) == 0:
        abort(404)
    order = [order for order in orders if order['orderId'] == orderId]
    if not order:
        abort(404)
    order[0]['status'] = request.args.get('status')
    return jsonify({'Updated order': order[0]}), 201

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}))

