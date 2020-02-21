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
# TABLE1 and TABLE2 have the following headers:
#   - Date
#   - Category
#   - Amount
#
# TABLE3 has the following headers
#   - Month
#   - Spent
#   - Income
#   - Saved
#
# Author: Andrew Ott

import pandas as pd
import mysql.connector
from datetime import datetime

# Table constansts
TABLE1 = "Withdrawals"
TABLE2 = "Deposits"
TABLE3 = "Totals"
TABLE1_Q = "CREATE TABLE " + TABLE1 + "IF NOT EXISTS (withd_id int PRIMARY KEY \
            AUTO_INCREMENT, Date datetime, Category VARCHAR(50), Amount int)"
TABLE2_Q = "CREATE TABLE " + TABLE2 + "IF NOT EXISTS (dep_id int PRIMARY KEY \
            AUTO_INCREMENT, Date datetime, Category VARCHAR(50), Amount int)"
TABLE3_Q = "CREATE TABLE " + TABLE3 + "IF NOT EXISTS (total_id int PRIMARY KEY \
            AUTO_INCREMENT, Month VARCHAR(50), Spent int, Income int, Saved int)"

def main():
    """Main function

    :return: Void
    :rtype: void

    """
    data_prompt()

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

    mycursor =


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


def data_prompt():
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
        file_prompt()

    elif reply == "MANUAL":
        manual_data_prompt()

def file_prompt():
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
    """Opens csv file with Pandas and processes file

    :param type fn: filename to open, input from user.
    :return: Description of returned object.
    :rtype: type

    """
    transactions = pd.read_csv(fn, index_col='Transaction Date',
                    usecols = ['Transaction Date', 'Category', 'Debit'])
    transactions = transactions.dropna(subset=['Debit'])


def manual_data_prompt():
    """Short summary.

    :return: Description of returned object.
    :rtype: type

    """
    print("---------------------------------------------")
    print("Manual Data Input Menu")
    print("---------------------------------------------")

main()
