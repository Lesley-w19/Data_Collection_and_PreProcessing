import sys
sys.path.append("../src") 

import psycopg2
from config import connection

# create a database conncetion
class create_connection:
    def __init__(self, config_path):
        self.config_path = config_path
        
    def connection():
        conn_str = connection
        
        try:
            conn = psycopg2.connect(conn_str)
            print("Connected to the datbase succesffully")
            return conn
        
        except Exception as e:
            return print("Error in creating a connection:", e)