# FinTracker.py
#
# Prompts user for mysql user, passwd, database
# Database has three tables:
#   - Withdrawals, with the following Col Headers:
#       - Date
#       - Description
#       - Category
#       - Amount
#   - Deposits, with the following Col Headers:
#       - Date
#       - Description
#       - Category
#       - Amount
#   - Totals, with the following Col Headers:
#       - Month
#       - Spent
#       - Income
#       - Saved
# Prompts user to import file or input data manually
#   - Promts user for filename and location, or
#   - Prompts user for data
# Imports data as DataFrame with Pandas Module
# Inserts Transactions into appropriate table
# Processes tables and calculates:
#   - Total Spent
#   - Total Deposited
#   - Total Saved
#
# Author: Andrew Ott

import pandas as pd
import mysql.connector
from datetime import datetime
from sqlalchemy import create_engine

# Table constants
TABLE1_Q = "CREATE TABLE IF NOT EXISTS Withdrawals\
            (\
            with_id int PRIMARY KEY AUTO_INCREMENT,\
            Date datetime,\
            Description VARCHAR(50),\
            Category VARCHAR(50),\
            Amount DECIMAL(13,2)\
            )"
TABLE2_Q = "CREATE TABLE IF NOT EXISTS Deposits\
            (\
            dep_id int PRIMARY KEY AUTO_INCREMENT,\
            Date datetime,\
            Description VARCHAR(50),\
            Category VARCHAR(50),\
            Amount DECIMAL(13,2)\
            )"
TABLE3_Q = "CREATE TABLE IF NOT EXISTS Totals\
            (\
            total_id int PRIMARY KEY AUTO_INCREMENT,\
            Month VARCHAR(50),\
            Spent int,\
            Income int,\
            Saved int\
            )"

def main():
    """Main function

    :return: Void
    :rtype: void

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

    mycursor = db.cursor()

    create_tables(mycursor)

    more_data = "Y"

    while more_data == "Y":
        data_prompt(db)

        more_data = input("Would you like to add more data(Y or N)?")
        more_data = more_data.upper()

        while more_data != "Y" and more_data != "N":
            more_data = input("Would you like to add more data(Y or N)?")
            more_data = more_data.upper()

    print("Have a great day")


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


def create_tables(db_cursor):
    """Short summary.

    :param type db_cursor: Description of parameter `db_cursor`.
    :return: Description of returned object.
    :rtype: type

    """
    db_cursor.execute(TABLE1_Q)
    db_cursor.execute(TABLE2_Q)
    db_cursor.execute(TABLE3_Q)


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


def data_prompt(db):
    """Prompts user how they would like to input data

    :return: Void.
    :rtype: void

    """
    print("---------------------------------------------")
    print("Input Data Menu")
    print('''Type:
    'MANUAL' to enter data manually or
    'FILE' to upload a csv file''')
    print("---------------------------------------------")

    reply = ""

    while (reply != "MANUAL" and reply != "FILE"):
        reply = input ("Would you like to input data manually or from a file?\n")
        reply = reply.upper()

    if reply == "FILE":
        file_prompt(db)

    elif reply == "MANUAL":
        manual_data_prompt(db)


def file_prompt(db):
    """Prompts user for filename and location.

    :return: Description of returned object.
    :rtype: type

    """
    print("---------------------------------------------")
    print("File Input Menu")
    print("---------------------------------------------")

    filename = input("Enter filename/relative location:\n")

    process_file(filename)


def process_file(fn):
    """Opens csv file with Pandas, processes file, and calls insert_df()

    :param type fn: filename to open, input from user.
    :return: Description of returned object.
    :rtype: type

    """
    # reads certain columns from the csv file
    transactions = pd.read_csv(fn, usecols = ['Transaction Date', 'Description',
                                             'Category', 'Debit'])
    # drops any rows where debit column has no data
    transactions = transactions.dropna(subset=['Debit'])
    # renames columns to match table columns in database
    transactions = transactions.rename(columns = {'Transaction Date': 'Date',
                                                 'Debit': 'Amount'})
    # converts date string to datetime object
    transactions['Date'] = pd.to_datetime(transactions['Date'])
    insert_df(transactions)


def insert_df(df):
    """Short summary.

    :param type df: Description of parameter `df`.
    :return: Description of returned object.
    :rtype: type

    """
    engine = create_engine('mysql+mysqlconnector://andrew:andrew@localhost/testdb')

    df.to_sql(name='Withdrawals',con=engine,if_exists='append',index=False)

def manual_data_prompt():
    """Short summary.

    :return: Description of returned object.
    :rtype: type

    """
    print("---------------------------------------------")
    print("Manual Data Input Menu")
    print("---------------------------------------------")

main()
