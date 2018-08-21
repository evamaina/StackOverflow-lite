import psycopg2
import os
from app.app.table_models import create_table
from psycopg2.extras import RealDictCursor

class Database():
    '''constructor to set up database'''
    def __init__(self):
        self.database = os.getenv('DATABASE')
        self.user = os.getenv('USER')
        self.password = os.getenv('PASSWORD') 
        self.host = os.getenv('HOST')
        self.connection = psycopg2.connect(database=self.database, user=self.user,host=self.host,password=self.password)



    