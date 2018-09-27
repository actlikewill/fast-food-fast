q1 = """
    CREATE TABLE IF NOT EXISTS orders(
    id SERIAL PRIMARY KEY,
    ordered_by VARCHAR(1000) NOT NULL,
    details VARCHAR(1000) NOT NULL,
    price VARCHAR(255) NOT NULL,
    status VARCHAR(255)
);
"""

q2 = """
    CREATE TABLE IF NOT EXISTS users(
    id SERIAL PRIMARY KEY,
    username VARCHAR(1000) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(255)
);
"""
q3 = """
    CREATE TABLE IF NOT EXISTS menu(
    id SERIAL PRIMARY KEY,
    menu_item VARCHAR(1000) NOT NULL,
    description VARCHAR(255) NOT NULL,
    price VARCHAR(255)            
);
"""

queries = [q1, q2, q3]

