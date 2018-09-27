"""This creates the menu class"""

class Menu:

    @classmethod
    def add_menu_query(cls, values):
        menu_item = values['menu_item']
        description = values['description']
        price = values['price']
        query = """
                INSERT INTO menu (menu_item, description, price)
                VALUES ({}, {}, {});
                """.format(menu_item, description, price)
        return query


    @classmethod
    def get_menu_query(cls, menu_item):

        query = """ 
                SELECT menu_item, description, price FROM menu WHERE menu_item = '{}';
                """.format(menu_item)
        return query

    @classmethod
    def get_all_menu_query(cls):
        query = """
                SELECT * FROM menu
                """
        return query

        
