from flask import jsonify, request
from ....db.db import connect
from .. import API_V2
from .order_model import Orders
from ...auth.user_views import token_required_jsonify

@API_V2.route('/orders', methods=['GET'])
@token_required_jsonify
def get_orders(current_user):
    if current_user['role'] != 'admin':
        return jsonify({"Sorry": "Only admin allowed access to this route."})
    query = Orders.get_all_orders()
    conn = connect()
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()

    return jsonify({"Orders": rows})

@API_V2.route('/orders', methods=['POST'])
@token_required_jsonify
def add_order(current_user):
    try:
        data = request.get_json()
        query = Orders.add_order_query(data)
        details = data['details']
        conn = connect()
        cur = conn.cursor()
        cur.execute(query)
        cur.close()
        conn.commit()
        success_message = """ New order {} Created""".format(details)
        return jsonify({"Success": success_message}), 201
    except(KeyError, TypeError):
        return jsonify({"Error": "you did not enter data correctly"})

@API_V2.route('/orders/<int:order_id>', methods=['GET'])
@token_required_jsonify
def get_one_order(current_user, order_id):
    if current_user['role'] != 'admin':
        return jsonify({"Sorry": "Only admin allowed access to this route."})

    query = Orders.get_single_order(order_id)
    conn = connect()
    cur = conn.cursor()
    cur.execute(query)
    row = cur.fetchone()

    return jsonify({"Order": row})


    



