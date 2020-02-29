Finance Tracker - Takes a CSV file and uploads it to a database

Description of Programs:

FinTracker_Simple.py
- Opens CSV file using CSV Library
- Calculates total Transactions on the credit card bill

FinTracker_Pandas.py
- Opens CSV file using Pandas module
- Processes file with Pandas methods

mysql_pract1.py, mysql_pract2.py, mysql_pract3.py
- Tutorial from Tech with Tim
- Practicing using MySQL

FinTracker.py
- Asks for mysql user, passwd, and database
- Creates Database if user requests new database
- Asks user to import file or input data
- Import csv
- Make csv a tuple
- Adds Transactions
- Allows manual input of data
- Returns total spent and total saved

To Do:
- ~~Create function that creates database if users requests~~
- ~~Create function that creates tables if they do not exist~~
- ~~Add items from csv file to database~~ I used sqlalchemy to create an engine
- ~~Fix attribute error in manual_data_prompt()~~
- Create functions to add data manually
  - ~~Create get_date() to get date from user~~
  - Create get_txn_type() to get transaction type, withdrawal or deposit
  - Create get_category()
  - Create get_description()
  - Create get_amount()
- **Update DocBlocks**
- Sort database by date and category (Can you sort by two criteria in MySQL?)
