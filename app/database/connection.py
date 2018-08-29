import psycopg2
import os

if os.getenv('CONFIG') == 'testing':
	conn_string = os.getenv("TEST_DATABASE")
elif os.getenv('CONFIG') == 'development':
	conn_string = os.getenv("DATABASE")