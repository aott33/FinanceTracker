import csv

def main():
    """Definition of the main function.
        Opens a CSV and calls other functions to format list

    :return:void
    :rtype: void

    """
    capitalCSV = open("../test.csv")
    capitalReader = csv.DictReader(capitalCSV, delimiter = ',')

    monthlyTotal = 0.0;

    for row in capitalReader:
        if (row['Debit']== ''):
            continue
        else:
            monthlyTotal += float(row['Debit'])

    print(str(monthlyTotal))

main()
