"""This is the menu class"""
from ....db.db import connect

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


    @staticmethod
    def get_menu_list():

        query = """
                SELECT menu_item, price FROM menu;
                """
        conn = connect()
        cur = conn.cursor()
        cur.execute(query)
        row = cur.fetchall()

        menu_list = []

        for item in row:
            menu_dict = {
                "menu_item":item[0],
                "price":item[1]
            }
            menu_list.append(menu_dict)
        
        return menu_list

    @staticmethod
    def get_all_menu_query():
        query = """
                SELECT * FROM menu
                """
        return query

    @classmethod
    def get_menu_keys(cls):
        menu_list = cls.get_menu_list()
        menu_keys = []
        for item in menu_list:
            menu_keys.append(item['menu_item'])
        return menu_keys

    
    
