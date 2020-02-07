#clsConPsycopg2.py
""" Clase base conexiones psycopg2 """

# Para obtener información detallada de la excepción
import sys
# Biblioteca para la conexión psycopg2
from psycopg2 import connect
# Bibliotecas para manejar errores de tipo: OperationalError errorcodes errors
from psycopg2 import OperationalError, errorcodes, errors

from datetime import datetime, timedelta
# Biblioteca para acceder al cursor, commit and close
import psycopg2.extensions

class DataBase():
    
    def __init__(self):
        self._my_connection = psycopg2.connect(database="public", user="public",
                                  password="general", host="127.0.0.1",
                                  port="5432")
        self._my_cursor = self._my_connection.cursor()

    @property
    def connection(self):
        return self._my_connection
    
    @property
    def cursor(self):
        return self._my_cursor

    
















    

    def query_database(self, sql_statement, *args):
        return self.my_cursor.execute(sql_statement, *args)

    def commit_query(self):
        return self.my_connection.commit()

    def fetch_one(self, sql_statement, *args):
        result = self.query_database(sql_statement, *args)
        if result is None:
            return False
        return result.fetchone()

    def fetch_all(self, sql_statement, *args):
        result = self.query_database(sql_statement, *args)
        if result is None:
            return False
        return result.fetchall()

    def __del__(self):
        self.my_cursor.close()
        self.my_connection.close()

























##################################################################################################
#                                                                                                #
#                                                                                                #
##################################################################################################