




class Users:
    @classmethod
    def insert_user_query(cls, values):
        username = values['username']
        email = values['email']
        password = values['password']
        role = values['role']
        query = """
                INSERT INTO users (username, email, password, role)
                VALUES ({}, {}, {}, {});
                """.format(username, email, password, role)
        return query

    @classmethod
    def get_user_query(cls, username):

        query = """ 
                SELECT username, password, role FROM users WHERE username = '{}';
                """.format(username)
        return query

    @classmethod
    def get_all_users_query(cls):
        query = """
                SELECT * FROM users
                """
        return query

    @classmethod
    def get_user_query_id(cls, user_id):

        query = """ 
                SELECT username, password, role FROM users WHERE id = '{}';
                """.format(user_id)
        return query



    
