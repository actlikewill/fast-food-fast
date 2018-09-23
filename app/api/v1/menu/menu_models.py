

class Menu:
    def __init__(self):
        self.menu = [
            # {
            #     "menu_id": 1,
            #     "menu_item": "Burger",
            #     "price": 200,
            
            # },
            # {
            #     "menu_id": 2,
            #     "menu_item": "Chicken",
            #     "price": 150,
            # }
        ]
        
    def add_menu_item(self, new_menu_item):
        self.menu.append(new_menu_item)
        