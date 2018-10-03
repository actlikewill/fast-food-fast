# import psycopg2
# from flask import request
# from flask_restful import Resource, Api
# from ....db.db import connect
# from .. import API_V2
# from flask_jwt_extended import jwt_required, get_jwt_identity
# from .order_models import Orders
# from ..menu.menu_models import Menu

# API_V2 = Api(API_V2)

# class PlaceOrder(Resource):
#     @staticmethod
#     # @jwt_required
#     def post():
#         query = Menu.get_menu_list()
#         conn = connect()
#         cur = conn.cursor()
#         cur.execute(query)
#         menu_list = cur.fetchall()

#         all_menu = []

#         for item in menu_list:
#             menu_dict = {
#                 "menu_item":item[0],
#                 "price":item[1]
#             }
#             all_menu.append(menu_dict)       
        
#         menu_keys = []

#         for item in menu_list:
#             menu_keys.append(item[0])

#         incoming_order = request.get_json()
#         details = incoming_order['details']
#         order_keys = []
#         for key in details.keys():
#             order_keys.append(key)

#         order = []

#         out_of_stock = set(order_keys) - set(menu_keys)
#         for item in out_of_stock:
#             order.append(item)
        
#         try:
#             if not out_of_stock:
#                 for item, quantity in details

#         # try:
#         #     data = request.get_json()
#         #     query = Orders.add_order_query(data)
#         #     details = data['details']
#         #     conn = connect()
#         #     cur = conn.cursor()
#         #     cur.execute(query)
#         #     cur.close()
#         #     conn.commit()
#         #     success_message = """ New order {} Created""".format(details)
#         #     return {"Success": success_message}, 201
#         # except(KeyError, TypeError):
#         #     return {"Error": "you did not enter data correctly."}, 400
#         return {"menu_list":all_menu}

# API_V2.add_resource(PlaceOrder, '/orders')