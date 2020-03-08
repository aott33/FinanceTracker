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

    while True:
        try:
            mysql_info = open_db_prompt()

            db = mysql.connector.connect(
                 host = mysql_info[0],
                 user = mysql_info[1],
                 passwd = mysql_info[2],
                 database = mysql_info[3]
                 )
        except mysql.connector.Error:
            print("Login information is incorrect, try again")
            continue
        else:
            break

    manual_data_prompt(db)

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
        reply = input("Do you have an existing database(Y on N)?\n")
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

    while True:
        try:
            host = input("Enter hostname: ")
            user = input("Enter username: ")
            passwd = input("Enter passwd: databases")
            new_db = input("Enter new database name: ")

            db = mysql.connector.connect(
                 host = host,
                 user = user,
                 passwd = passwd,
                 )
        except mysql.connector.Error:
            print("Login information is incorrect, try again")
            continue
        else:
            break

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
        reply = input ("Enter data manually or from a file?\n")
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


def manual_data_prompt(db):
    """Prompts user for the transaction data. If data is valid, adds it to table

    :return: void
    :rtype: Void

    """
    print("---------------------------------------------")
    print("Manual Data Input Menu")
    print("---------------------------------------------")

    txn_type = get_txn_type()
    txn_date = get_txn_date()
    txn_desc = get_txn_desc()
    txn_cat = get_txn_cat()
    txn_amnt = get_txn_amnt()

    txn_list = (txn_date, txn_desc, txn_cat, txn_amnt)

    mycursor = db.cursor()

    data_q= "INSERT INTO " + txn_type + " (Date, Description, Category, Amount)"\
            + " VALUES(%s, %s, %s, %s)"

    mycursor.execute(data_q, txn_list)

    #temp - prints the table that user inputs data into
    mycursor.execute("SELECT * FROM " + txn_type)
    for x in mycursor:
        print(x)


def get_txn_type():
    """Prompts user for transaction type.

    :return: The transaction type to match table (Withdrawals or Deposits).
    :rtype: string

    """
    print("Transaction type:")

    reply = ""

    while (reply != "W" and reply != "D"):
        reply = input("W - Withdrawal, D - Deposit: ")
        reply = reply.upper()

    if reply == "W":
        reply = "Withdrawals"

    elif reply == "D":
        repy = "Deposits"

    return reply

def get_txn_cat():
    """Prompts user for transaction category (ex. Groceries).

    :return: The transaction category.
    :rtype: string

    """
    txn_cat = input("Transaction Category(ex. Groceries):\n")
    txn_cat = txn_cat.upper()

    return txn_cat


def get_txn_desc():
    """Prompts user for a brief transaction description (ex. Location).

    :return: The transaction description.
    :rtype: string

    """
    desc_len = 16

    while desc_len > 15:
        txn_desc = input("Transaction description/location (max 15 characters):\n")
        txn_desc = txn_desc.upper()
        desc_len = len(txn_desc)

        if(desc_len > 15):
            print("*ERROR: String length too long.*")

    return txn_desc

def get_txn_amnt():
    """Prompts user for transaction amount and it must be greater than 0.0.

    :return: Transaction amount with precision of 2 decimal places.
    :rtype: float

    """
    amnt = 0.0

    while amnt <= 0.0:
        try:
            print("Enter transaction amount (greater than 0)")
            amnt = float(input("Amount: "))
        except ValueError:
            print("Enter valid monetary value")
            continue

    amnt = '%.2f' % amnt

    return amnt


def get_txn_date():
    """Prompts user for transaction date, keeps looping until the user
    enters the correct format and correct requested date.

    :return: datetime object for database.
    :rtype: datetime.datetime

    """
    requestedDate = "N"
    isValidDate = False
    txn_date = ""

    # Loops until the user confirms that the date entered is what is requested
    while requestedDate == "N":
        requestedDate = ""
        isValidDate = False

        # Loops until user enters a valid date in format 'dd-mm-yyyy'
        while not isValidDate:

            purch_date_ip = input("Transaction date in format 'dd-mm-yyyy' : ")

            # Trys converting user input to a datetime object
            try:
                txn_date = datetime.strptime(purch_date_ip, "%d-%m-%Y")
                isValidDate = True

            # catches the exception and prints message for user
            except ValueError:
                print("Wrong format, please enter the correct format.")

        # Loops until user enters either "y", "Y", "n", or "N"
        while requestedDate != "Y" and requestedDate != "N":
            print("Date entered: ", txn_date)
            requestedDate = input("Correct date (Y or N)? ")
            requestedDate = requestedDate.upper()

    return txn_date

main()
