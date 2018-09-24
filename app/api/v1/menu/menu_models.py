"""This creates the menu class to store menu items"""

class Menu:
    """The menu class"""
    def __init__(self):
        self.menu = []

    def add_menu_item(self, new_menu_item):
        """This adds items to the menu"""
        self.menu.append(new_menu_item)
        