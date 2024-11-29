# © 2024 Ayça Kaygusuz

import psycopg2
from config import DATABASE_DEFAULT_CONFIG

class Database:
    def __init__(self, dbname = None, user = None, password = None, host = 'localhost', port = '5432'):
        # Use default values from config if not provided
        self.conn = psycopg2.connect(
            dbname = dbname or DATABASE_DEFAULT_CONFIG['dbname'],
            user = user or DATABASE_DEFAULT_CONFIG['user'],
            password = password or DATABASE_DEFAULT_CONFIG['password'],
            host = host or DATABASE_DEFAULT_CONFIG['host'],
            port = port or DATABASE_DEFAULT_CONFIG['port']
        )

    def execute(self, query, params = None):
        with self.conn.cursor() as cursor:
            cursor.execute(query, params)
            self.conn.commit()

    def fetchone(self, query, params = None):
        with self.conn.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchone()

    def fetchall(self, query, params = None):
        with self.conn.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchall()

    def close(self):
        self.conn.close()