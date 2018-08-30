import psycopg2
import os
from app.table_models import create_table
from psycopg2.extras import RealDictCursor

'''environment variables for development'''
if os.getenv('CONFIG') == 'development':
    conn_string = os.getenv("DATABASE")
    '''environment variables for testing'''
elif os.getenv('CONFIG') == 'testing':
    conn_string = os.getenv("TEST_DATABASE")

'''opening a connection to our database'''
conn = psycopg2.connect(conn_string)
'''creating a cursor'''
cur = conn.cursor(cursor_factory=RealDictCursor)

def create_tables():
    for table in create_table():
        cur.execute(table)
        conn.commit()
        print('table created  successfully')
        
    return 'tables created'
  

def drop_tables():
    
    drop_users = "DROP TABLE IF EXISTS users CASCADE"

    drop_questions = "DROP TABLE IF EXISTS questions CASCADE"

    drop_answers = "DROP TABLE IF EXISTS answers CASCADE"

    drop_token = "DROP TABLE IF EXISTS token"

    table_list= [drop_users , drop_questions , drop_answers, drop_token]
        
    try:
        
        for table in table_list:
            
            cur.execute(table)
        
            ''' commit and save changes'''
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


