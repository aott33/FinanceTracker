# FinTracker.py
#
# Two types of tables for this finance tracking database
#   - Withdrawals (TABLE1)
#   - Deposits (TABLE2)
#
# Both of the following headers:
#   - Date
#   - Category
#   - Amount
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
# Author: Andrew Ott

TABLE1 = "Withdrawals"
TABLE2 = "Deposits"
COL_HEADERS = ('Date', 'Category', 'Amount')

def main():
    mysql_info = initial_prompt()


def initial_prompt():
    """Prompts user for mysql user, passwd, database name

    :return: Returns a tuple with user information
    :rtype: tuple

    """
    print("Welcome to the Finance Tracker")
    host = input("Enter hostname: ")
    user = input("Enter username: ")
    passwd = input("Enter passwd: ")
    db = input("Enter database name: ")

    return host, user, passwd, db


main()
