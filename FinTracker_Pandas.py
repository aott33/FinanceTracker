import pandas

transactions = pandas.read_csv('../test.csv', index_col='Transaction Date',
                usecols = ['Transaction Date', 'Category', 'Debit', 'Credit'])

print(transactions)
