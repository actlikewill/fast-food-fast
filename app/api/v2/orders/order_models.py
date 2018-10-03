"""This is the basic order class"""
class Orders:
    @staticmethod
    def add_order_query(values):
        ordered_by = values['ordered_by']
        details = values['details']
        price = values['price']
        status = values['status']
        query = """
                INSERT INTO orders (ordered_by, details, price, status)
                VALUES ('{}', '{}', '{}', '{}');
                """.format(ordered_by, details, price, status)

        return query

    @staticmethod
    def get_single_order(order_id):
        query = """
                SELECT * FROM orders WHERE id = '{}';
                """.format(order_id)
        return query

    @staticmethod
    def get_all_orders():
        query = """
                SELECT * FROM orders
                """
        return query

    @staticmethod
    def update_order_status(status, order_id):
        query = """
                UPDATE orders SET status = '{}' WHERE id = '{}';
                """.format(status, order_id)
        return query

    # @staticmethod
    # def get_user_orders(ordered_by):
    #     query = """
    #             SELECT * FROM orders WHERE ordered_by = '{}';
    #             """.format(ordered_by)
    #     return query
