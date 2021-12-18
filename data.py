# data.py interfaces with the back-end of the application to
# retrieve date from the relational database and access the wirrten SQL queries and functions.

import mysql.connector


def getConnector() -> mysql.connector:
    """Description
    Returns a sql connection object
    """
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Renard",
        database="bookstore"
    )


def sql_execute_command(connector: mysql.connector, query: str) -> list:
    """Function that given a connector and query returns the result

    Args:
        connector (mysql.connector): connector to the SQL database
        query (str): Query to be executed

    Returns:
        list: Results of the query
    """
    mycursor = connector.cursor()
    mycursor.execute(query)

    return mycursor.fetchall()
