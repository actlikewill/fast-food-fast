class Order:
    def __init__(self, item_name, item_quantity):        
        self.item_name = item_name        
        self.item_quantity = item_quantity
        self.order_no = 1



class Orders:    
    def __init__(self):
        self.order_list = []

    def add_order(self, order_obj):
        new_order_obj = Order(order_obj['item'], order_obj['quantity'])

        order_number = len(self.order_list) +1

        new_order = {
            "item": new_order_obj.item_name,
            "quantity": new_order_obj.item_quantity,
            "orderId": order_number
        }        
        self.order_list.append(new_order)