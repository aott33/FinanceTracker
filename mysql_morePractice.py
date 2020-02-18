# Working through the Python MySQL Tutorial - Foreign Keys & Relating Tables
# From Tech With Tim YouTube Channel
# Link: https://www.youtube.com/watch?v=f7oYCzKuv-w&t=630s

import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "andrew",
    passwd = "andrew",
    database = "testdb"
    )

users_info = [("Andrew", "andy"),
        ("Bob", "bobby"),
        ("Sally", "sal")]

user_score = [(100, 20),
             (20, 45),
             (34, 50)]

mycursor = db.cursor()

# user table string
# Q1 = "CREATE TABLE users (id int PRIMARY KEY AUTO_INCREMENT,\
#                         name VARCHAR(50), passwd VARCHAR(50))"

# user scores string
# Q2 = "CREATE TABLE scores (user_id int PRIMARY KEY, FOREIGN KEY(user_id)\
#                           REFERENCES users(id), game1 int DEFAULT 0,\
#                           game2 int DEFAULT 0)"

# query string - inserts users into table
#Q3 = "INSERT INTO users (name, passwd) VALUES (%s, %s)"

# query string - inserts user scores into table
#Q4 = "INSERT INTO scores (user_id, game1, game2) VALUES (%s, %s,%s)"


#for x, user in enumerate(users_info):
#    mycursor.execute(Q3, user)
#    last_id = mycursor.lastrowid
#    mycursor.execute(Q4, (last_id,) + user_score[x])

#db.commit()

mycursor.execute("SELECT * FROM users")
for x in mycursor:
    print(x)

mycursor.execute("SELECT * FROM scores")
for x in mycursor:
    print(x)
