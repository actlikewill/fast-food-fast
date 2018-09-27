"""This is the basic order class"""
class Orders:
    @classmethod
    def add_order_query(cls, values):
        ordered_by = values['ordered_by']
        details = values['details']
        price = values['price']
        status = values['status']
        query = """
                INSERT INTO orders (ordered_by, details, price, status)
                VALUES ({}, {}, {}, {});
                """.format(ordered_by, details, price, status)

        return query

    @classmethod
    def get_single_order(cls, order_id):
        query = """
                SELECT * FROM orders WHERE id = '{}';
                """.format(order_id)
        return query

    @classmethod
    def get_all_orders(cls):
        query = """
                SELECT * FROM orders
                """
        return query

    @classmethod
    def update_order_status(cls, status, order_id):
        query = """
                UPDATE orders SET status = {} WHERE id = '{}';
                """.format(status, order_id)
        return query

    @classmethod
    def get_user_orders(cls, ordered_by):
        query = """
                SELECT * FROM orders WHERE ordered_by = '{}';
                """.format(ordered_by)
        return query  

    

