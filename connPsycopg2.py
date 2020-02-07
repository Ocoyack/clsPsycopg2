#connPsycopg2.py
""" Clase base conexiones psycopg2"""
# para obtener información detallada de la excepción
import sys
# biblioteca para la conexión psycopg2 y Manejar excepciones del tipo:
from psycopg2 import connect, OperationalError, errorcodes, errors

class Database:
    def __init__(self, name):
        self._conn = psycopg2.connect(database="postgres", user='postgres', password='docker', host="localhost", port=5432)
        self._cursor = self._conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.commit()
        self.connection.close()

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self.connection.commit()

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()

###########################################################################
#                                                                         #
#                                                                         #
###########################################################################
