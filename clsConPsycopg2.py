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

    # define a function that handles and parses psycopg2 exceptions
    
    def print_psycopg2_exception(err):
    # get details about the exception
        err_type, err_obj, traceback = sys.exc_info()
 
    # get the line number when exception occured
        line_num = traceback.tb_lineno
 
    # print the connect() error
        print ("\npsycopg2 ERROR:", err, "on line number:", line_num)
        print ("psycopg2 traceback:", traceback, "-- type:", err_type)
 
    # psycopg2 extensions.Diagnostics object attribute
        print ("\nextensions.Diagnostics:", err.diag)
 
    # print the pgcode and pgerror exceptions
        print ("pgerror:", err.pgerror)
        print ("pgcode:", err.pgcode, "\n")
















    

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
