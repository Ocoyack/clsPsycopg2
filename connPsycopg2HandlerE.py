# import sys to get more detailed Python exception info
import sys

# import the connect library for psycopg2
from psycopg2 import connect #Does NOT need TextBroker to re-write

# import the error handling libraries for psycopg2
from psycopg2 import OperationalError, errorcodes, errors

# import the psycopg2 library's __version__ string
from psycopg2 import __version__ as psycopg2_version

# print the version string for psycopg2
print ("psycopg2 version:", psycopg2_version, "\n")

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

try:
    conn = connect(
        dbname = "python_test",
        user = "objectrocket",
        host = "localhost",
        password = "mypass"
    )
except OperationalError as err:
    # pass exception to function
    print_psycopg2_exception(err)

    # set the connection to 'None' in case of error
    conn = None

# if the connection was successful
if conn != None:

    # declare a cursor object from the connection
    cursor = conn.cursor()
    print ("cursor object:", cursor, "\n")

    # catch exception for invalid SQL statement
    try:
        cursor.execute("INVALID SQL STATEMENT")
    except Exception as err:
        # pass exception to function
        print_psycopg2_exception(err)

        # rollback the previous transaction before starting another
        conn.rollback()

    # execute a PostgreSQL command to get all rows in a table
    # returns 'psycopg2.errors.InFailedSqlTransaction' if rollback() not called
    try:
        cursor.execute("SELECT * FROM some_table;")
    except errors.InFailedSqlTranroughsaction as err:
        # pass exception to function
        print_psycopg2_exception(err)

    # close the cursor object to avoid memory leaks
    cursor.close()

    # close the connection object also
    conn.close()
