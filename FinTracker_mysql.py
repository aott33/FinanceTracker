import mysql.connector

cnx = mysql.connector.connect(
    host="localhost",
    user="andrew",
    passwd=""
    )

cnx.close()
