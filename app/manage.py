import psycopg2
import os
from app.table_models import create_table
from psycopg2.extras import RealDictCursor

DATABASE_URL = os.environ['DATABASE_URL']


class Database():
    '''constructor to set up database'''
    def __init__(self):
        self.connection = psycopg2.connect(DATABASE_URL, sslmode='require')

    def create_tables(self):
        cur = self.connection.cursor()
        for table in create_table():
            cur.execute(table)
            self.connection.commit()
            print('table created  successfully')
            
        return 'tables created'
      

    def drop_tables(self):
        ''' deletes the existing tables from the database'''
        query = (
        	'DROP TABLE IF EXISTS users CASCADE;',
            'DROP TABLE IF EXISTS questions CASCADE;',
            'DROP TABLE IF EXISTS answers CASCADE;',
            'DROP TABLE IF EXISTS tokens;'
        )
        
        cur = self.connection.cursor()
        for drop_table in query:
            cur.execute(drop_table)
            print('table dropped')
            self.commit()
        
            
        return 'tables dropped successfully'

    def cursor(self):
        '''cursor method for executing queries'''
        cur = self.connection.cursor(cursor_factory=RealDictCursor)
        return cur
    
    def commit(self):
        '''save changes to db'''
        self.connection.commit()

    