import mysql.connector

cnx = mysql.connector.connect(
    host="localhost",
    user="andrew",
    passwd="andrew",
    database="testdb"
    )

mycursor = cnx.cursor()


#mycursor.execute("CREATE TABLE Person(name VARCHAR(50), age SMALLINT UNSIGNED,\
#                personID int PRIMARY KEY AUTO_INCREMENT)")

mycursor.execute("INSERT INTO Person (name, age) VALUES(%s, %s)", ("Bob", 20))
cnx.commit()

mycursor.execute("SELECT * FROM Person")

for x in mycursor:
    print(x)
