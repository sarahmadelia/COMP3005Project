import mysql.connector


def getConnector() -> mysql.connector:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Renard",
        database="mydatabase"
    )
    return mydb


def print_all_data(connector: mysql.connector):
    mycursor = connector.cursor()
    mycursor.execute("SELECT * FROM customers")

    myresult = mycursor.fetchall()
    for x in myresult:
        print(x[0], x[1])


# mycursor.execute(
#     "CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
# mycursor = mydb.cursor()

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)

# mydb.commit()
