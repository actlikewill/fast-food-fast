from app import app
from flask import request, jsonify
from app.models import Orders

OrderClass = Orders()



@app.route('/api/v1/orders', methods=['GET'])
def get_order():    
    return jsonify({"orders": OrderClass.order_list})

@app.route('/api/v1/orders', methods=['POST'])
def place_order():
    order = {
        "item": request.args.get('item'),
        "quantity": request.args.get('quantity')        
    }
    OrderClass.add_order(order)
    return jsonify({"order placed": order}), 201
