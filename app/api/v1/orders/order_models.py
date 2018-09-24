"""
This file creates the order class which lays out the basic structure
of the order table
"""

from ..helpers.helpers import get_dict_item

class Orders:
    """The basic order class"""
    def __init__(self):
        self.order_list = []
        self.order_keys = []

    def add_order(self, order):
        """Adds an order to the list"""
        self.order_list.append(order)

    def get_order(self, order_id):
        """Gets a specific order from the order list"""
        order = get_dict_item(self.order_list, 'order_id', order_id)
        return order

    def get_order_keys(self, order_data):
        """Gets a list of all current order items and appends to list"""
        for key in order_data.keys():
            self.order_keys.append(key)
        return self.order_keys
    
    def reset_order_keys(self):
        """Clears the current order keys to prepare for the next order"""
        self.order_keys = []
        