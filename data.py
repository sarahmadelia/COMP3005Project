""" 
Acts as the model 
data.py interfaces with the back-end of the application to retrieve data from the 
relational database and access the written SQL queries and functions. 
"""

import mysql.connector


def getConnector() -> mysql.connector:
    """Initializes the connector between MySQL and the user interfaces 
    Returns:
        mysql.connector: SQL Connection Object 
    """
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Renard",
        database="bookstore"
    )


def sql_execute_command(connector: mysql.connector, query: str) -> list:
    """Function that is passed the connector and query and returns the result of the query
    Args:
        connector (mysql.connector): connector to the SQL database
        query (str): Query to be executed

    Returns:
        list: Results of the query
    """
    mycursor = connector.cursor()
    mycursor.execute(query)

    return mycursor.fetchall()
