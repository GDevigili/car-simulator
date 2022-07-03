from unicodedata import name
from pygame import Cursor
import mysql.connector

from GLOBAL_VARIABLES import DB_DATABASE, DB_HOST, DB_USER, DB_PASSWORD

def create_connection(host, database, user, passwd):
    try:
        return mysql.connector.connect(
            host = host,
            database = database,
            user = user,
            passwd = passwd
        )
    except mysql.connector.Error as error:
        print("Error: {}".format(error))
        return None

def connect():
    return create_connection(DB_HOST, DB_DATABASE, DB_USER, DB_PASSWORD)

def close_connection(conn):
    conn.close()