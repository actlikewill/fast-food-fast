import psycopg2
from instance.config import CONFIG
from .queries import queries

db_url = CONFIG['default'].DATABASE_URL

# class DataBase:
#     def __init__(db_url):
#         self.db_url = db_url

def connect():
    try:
        conn = psycopg2.connect(db_url)
        return conn
    except(Exception, psycopg2.DatabaseError) as error:
        print("Connection Error:", error)

def create_tables():
    print("Creating Tables..")
    try:
        conn = connect()
        cur = conn.cursor()
        for query in queries:
            cur.execute(query)
        print("Success!")
    except(Exception, psycopg2.DatabaseError) as error:
        print("Connection Error:", error)
    finally:
        cur.close()
        conn.commit()
        print("Closing database...")

def save_to_db(query):
    conn = connect()
    cur = conn.cursor()
    cur.execute(query)
    cur.close()
    conn.commit()

def fetch_all_from_db(query):
    conn = connect()
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    return rows

def fetch_one_from_db(query):
    conn = connect()
    cur = conn.cursor()
    cur.execute(query)
    row = cur.fetchone()
    return row

def drop_test_tables():
    pass
