import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host = "localhost",
    user = "andrew",
    passwd = "andrew",
    database = "testdb"
    )

mycursor = db.cursor()

# mycursor.execute("CREATE TABLE Test(name VARCHAR(50) NOT NULL,\
#                created datetime NOT NULL, gender ENUM('M', 'F', 'O') NOT NULL,\
#                id INT PRIMARY KEY NOT NULL AUTO_INCREMENT)")

# mycursor.execute("INSERT INTO Test (name, created, gender) VALUES (%s,%s,%s)",
#                ("Mary", datetime.now(), "F"))

mycursor.execute("SELECT * FROM Test WHERE gender='M' ORDER BY id DESC")

for x in mycursor:
    print(x)
