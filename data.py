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
        list: Restults of the query
    """
    mycursor = connector.cursor()
    mycursor.execute(query)

    return mycursor.fetchall()


# def print_all_data(connector: mysql.connector):
#     """Descr

#     Args:
#         connector (mysql.connector): connection to the database
#     """
#     mycursor = connector.cursor()
#     mycursor.execute("SELECT * FROM BookStore")

#     myresult = mycursor.fetchall()
#     for x in myresult:
#         print(x[0], x[1])

    myresult = mycursor.fetchall()
    for x in myresult:
        print(x[0], x[1])

# l = sql_execute_command(getConnector(), "SELECT * FROM BookStore")

# for i in l:
#     print(i)
# mycursor.execute(
#     "CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
# mycursor = mydb.cursor()

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)

# mydb.commit()
