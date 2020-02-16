import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "andrew",
    passwd = "andrew",
    database = "testdb"
    )

users = [("Andrew", "andy", "12345", "andy@gmail.com"),
        ("Bob", "bobby", "22222", "bob@gmail.com"),
        ("Sally", "sal", "33333", "sal@gmail.com")]

user_score = [(100, 20),
             (20, 45),
             (34, 50)]

mycursor = db.cursor()

# creates user table string
# Q1 = "CREATE TABLE users (id int PRIMARY KEY AUTO_INCREMENT,\
#                        name VARCHAR(50), passwd VARCHAR(50))"
Q2 = "CREATE TABLE scores (user_id int PRIMARY KEY, FOREIGN KEY(user_id)\
                          REFERENCES users(id), game1 int DEFAULT 0,\
                          game2 int DEFAULT 0)"
mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)
