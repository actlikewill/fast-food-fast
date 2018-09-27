from flask import jsonify, request
from ....db.db import connect
from .. import API_V2
from .menu_models import Menu
from ...auth.user_views import token_required_jsonify


@API_V2.route('/menu', methods=['GET'])
def get_menu():

    query = Menu.get_all_menu_query()
    conn = connect()
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()

    return jsonify({"Menu2": rows})

@API_V2.route('/menu', methods=['POST'])
@token_required_jsonify
def add_menu_item(current_user):
    if current_user['role'] != 'admin':
        return jsonify({"Sorry": "Admin required"})
    try:
        data = request.get_json()
        query = Menu.add_menu_query(data)
        item = data['menu_item']
        conn = connect()
        cur = conn.cursor()
        cur.execute(query)
        cur.close()
        conn.commit()
        success_message = """ Menu Item {} Created""".format(item)
        return jsonify({"Success": success_message})
    except(KeyError, TypeError):
        return jsonify({"Error": "you did not enter data correctly"})

