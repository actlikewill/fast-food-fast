"""This is where common tasks will be defined"""

import re

def get_dict_item(dict_list, key, var):
    """Loops through a list of dictionaries and returns the one
        with the key value pair
    """
    item = [item for item in dict_list if item[key] == var]
    return item

def validate_string(string):
    """Simple string validation"""
    result = re.match('^[a-zA-Z]*$', string)
    if result and len(string) != 0:
        return "Valid"
    return "Invalid"
    