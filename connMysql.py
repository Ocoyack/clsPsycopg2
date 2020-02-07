#connMysql.py
""" Clase base conexiones psycopg2"""
# para obtener información detallada de la excepción
import sys
# biblioteca para la conexión psycopg2
from psycopg2 import connect

# import the error handling libraries for psycopg2
from psycopg2 import OperationalError, errorcodes, errors

class Database:

    def __init__(self, name):
    self._conn = sqlite3.connect(name)
    self._cursor = self._conn.cursor()




















############################################################
#                                                          #
#                                                          #
############################################################