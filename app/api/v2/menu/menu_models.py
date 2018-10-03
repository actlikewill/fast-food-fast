"""This is the menu class"""

class Menu:

    @staticmethod
    def add_menu_query(values):
        menu_item = values['menu_item']
        description = values['description']
        price = values['price']
        query = """
                INSERT INTO menu (menu_item, description, price)
                VALUES ('{}', '{}', '{}');
                """.format(menu_item, description, price)
        return query


    # @staticmethod
    # def get_menu_query(menu_item):

    #     query = """
    #             SELECT menu_item, description, price FROM menu WHERE menu_item = '{}';
    #             """.format(menu_item)
    #     return query

    @staticmethod
    def get_all_menu_query():
        query = """
                SELECT * FROM menu
                """
        return query
