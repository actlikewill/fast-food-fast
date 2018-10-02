"""
This is the Basic user class.
"""
class Users:
    """
    The class generates the queries that will be
    used to interact with the database.
    """
    @staticmethod
    def insert_user_query(values):
        username = values['username']
        email = values['email']
        password = values['password']
        role = values['role']
        query = """
                INSERT INTO users (username, email, password, role)
                VALUES ('{}', '{}', '{}', '{}');
                """.format(username, email, password, role)
        return query

    @staticmethod
    def get_user_query(username):

        query = """
                SELECT username, password, role FROM users WHERE username = '{}';
                """.format(username)
        return query

    @staticmethod
    def get_all_users_query():
        query = """
                SELECT * FROM users
                """
        return query

    @staticmethod
    def get_user_query_id(user_id):

        query = """ 
                SELECT username, password, role FROM users WHERE id = '{}';
                """.format(user_id)
        return query
