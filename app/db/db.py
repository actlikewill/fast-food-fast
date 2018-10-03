import psycopg2
from instance.config import DevelopmentConfig
from .queries import queries

db_url = DevelopmentConfig().DATABASE_URL

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
