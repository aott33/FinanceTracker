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

# Select columns from table to print
# mycursor.execute("SELECT name, gender FROM Test WHERE gender='F' ORDER BY id DESC")

# Alter table - add an additional column
# mycursor.execute("ALTER TABLE Test ADD COLUMN food VARCHAR(50) NOT NULL")

# Alter table - remove a column
# mycursor.execute("ALTER TABLE Test DROP food")

# Alter table - change name of column
# mycursor.execute("ALTER TABLE Test CHANGE name first_name VARCHAR(50)")

mycursor.execute("DESCRIBE Test")

print(mycursor.fetchone())

for x in mycursor:
    print(x)
