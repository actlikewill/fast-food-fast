"""
Lays out the basic structure of how the orders will be saved
"""
class Order:
    """
    This creates a basic order object
    """
    def __init__(self, item_name, item_quantity):
        self.item_name = item_name
        self.item_quantity = item_quantity
        self.order_no = 1



class Orders:
    """
    Creates the basic cart of orders placed
    """
    def __init__(self):
        self.order_list = []

    def add_order(self, order_obj):
        """
        Adds the order instance to the cart
        """
        new_order_obj = Order(order_obj['item'], order_obj['quantity'])

        order_number = len(self.order_list) +1

        new_order = {
            "item": new_order_obj.item_name,
            "quantity": new_order_obj.item_quantity,
            "order_id": order_number,
            "status": "Pending"
        }
        self.order_list.append(new_order)
        