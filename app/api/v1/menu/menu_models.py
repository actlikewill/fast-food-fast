"""This creates the menu class to store menu items"""

from ..helpers.helpers import get_dict_item

class Menu:
    """The menu class"""
    def __init__(self):
        self.menu = []
        self.menu_list = []

    def add_menu_item(self, new_menu_item):
        """This adds items to the menu"""
        self.menu.append(new_menu_item)

    def get_menu_keys(self):
        """This returns a list of all menu items"""
        for menu_item in self.menu:
            self.menu_list.append(menu_item['menu_item'])
        return self.menu_list

    def get_menu_item(self, menu_id):
        """Gets a specific menu item from the menu"""
        menu_item = get_dict_item(self.menu, 'menu_id', menu_id)
        return menu_item
        