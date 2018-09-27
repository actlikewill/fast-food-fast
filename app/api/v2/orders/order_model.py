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

