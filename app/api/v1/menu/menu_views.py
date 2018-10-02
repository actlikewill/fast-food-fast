"""
This creates the resources and endpoints for the menu
"""
from flask import request
from flask_restful import Resource, Api, abort
from .. import  API_V1
from .menu_models import Menu
from ..helpers.helpers import validate_string


API = Api(API_V1)
MENU = Menu()

class GetMenu(Resource):
    """This gets the menu list"""
    @classmethod
    def get(cls):
        """This gets the menu list"""
        return {"Menu": MENU.menu}

    @classmethod
    def post(cls):
        """This adds a new menu item"""
        json_data = request.get_json()

        try:

            menu_item = json_data["menu_item"]
            if validate_string(menu_item) == "Invalid":
                return {"Error": "Invalid string, Do not use special charactes or empty strings"}, 400
            new_menu_item = {
                "menu_id": len(MENU.menu) + 1,
                "menu_item": json_data["menu_item"],
                "price": json_data["price"]
            }
            MENU.add_menu_item(new_menu_item)
            return {"Menu item added": new_menu_item}, 201
        except KeyError:
            return {"Error": "This endpoint accepts requests in the following format: 'menu_item':<string>,'price':<integer>. Use double quotes on the key words and string values"}, 400

class GetSingleMenuItem(Resource):
    """This responds to single menu_item requests using the unique menu_item id"""
    @classmethod
    def get(cls, menu_item_id):
        """Returns a single menu_item"""
        menu_item = MENU.get_menu_item("menu_id", menu_item_id)
        if not menu_item:
            abort(404, message='error. That item does not exist')
        return {'Menu_item': menu_item[0]}

    @classmethod
    def put(cls, menu_item_id):
        """Updates a single menu item"""
        try:
            menu = MENU.menu
            if not menu:
                abort(404, message='error. That item does not exist')
            menu_item = MENU.get_menu_item("menu_id", menu_item_id)
            if not menu_item:
                abort(404, message='error. That item does not exist')
            json_data = request.get_json()
            menu_item[0]['menu_item'] = json_data['menu_item']
            menu_item[0]['price'] = json_data['price']
            return {'Updated menu': menu_item[0]}, 201
        except KeyError:
            return {"Error": "Please enter a valid item. 'menu_item':<string>, 'price':<integer>"}, 400

API.add_resource(GetMenu, '/menu', endpoint='menu')
API.add_resource(GetSingleMenuItem, '/menu/<int:menu_item_id>', endpoint='singlemenu')
