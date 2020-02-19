# FinTracker.py
#
# Prompts user for mysql user, passwd, database
# Database has two tables:
# Expenses and Deposits
# Prompts user to import file or input data
#   - Promts user for filename and location, or
#   - Prompts user for data
# Imports data as tuple
# Inserts Transactions into request table
# Returns total spent and total saved
#
# Two types of tables for this finance tracking database
#   - Withdrawals (TABLE1)
#   - Deposits (TABLE2)
#
# Both of tables have the following headers:
#   - Date
#   - Category
#   - Amount
#
# Author: Andrew Ott

import pandas
import mysql.connector

TABLE1 = "Withdrawals"
TABLE2 = "Deposits"
COL_HEADERS = ('Date', 'Category', 'Amount')

def main():
    """Short summary.

    :return: Description of returned object.
    :rtype: type

    """

    reply = initial_prompt()

    if reply == "N":
        create_db_prompt()

    mysql_info = open_db_prompt()

    db = mysql.connector.connect(
         host = mysql_info[0],
         user = mysql_info[1],
         passwd = mysql_info[2],
         database = mysql_info[3]
         )


def initial_prompt():
    """Asks user if they have an existing database

    :return: a reply (y or n)
    :rtype: string

    """
    """Short summary.

    :return: Description of returned object.
    :rtype: type

    """
    print("---------------------------------------------")
    print("Welcome to the Finance Tracker")
    print("---------------------------------------------")

    reply = " "

    # prompts until user enters a valid response
    while (reply != "Y" and reply != "N"):
        reply = input("Do you have an existing database(Y on N)? ")
        reply = reply.upper()

    return reply


def create_db_prompt():
    """Creates a new database.

    :return: void
    :rtype: void

    """
    print("---------------------------------------------")
    print("Create Database")
    print("---------------------------------------------")
    host = input("Enter hostname: ")
    user = input("Enter username: ")
    passwd = input("Enter passwd: databases")
    new_db = input("Enter new database name: ")

    db = mysql.connector.connect(
         host = host,
         user = user,
         passwd = passwd,
         )

    mycursor = db.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS " + new_db)
    print("---------------------------------------------")
    print("Database Created\n")
    print("---------------------------------------------")


def open_db_prompt():
    """Prompts user for mysql user, passwd, database name

    :return: Returns a tuple with user information
    :rtype: tuple

    """
    print("---------------------------------------------")
    print("Enter login information to access databases")
    print("---------------------------------------------")
    host = input("Enter hostname: ")
    user = input("Enter username: ")
    passwd = input("Enter passwd: ")
    db = input("Enter database: ")

    return host, user, passwd, db


main()
