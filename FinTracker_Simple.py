import csv

def main():
    """Definition of the main function.
        Opens a CSV and calls other functions to format list

    :return:void
    :rtype: void

    """
    capitalCSV = open("../test.csv")
    capitalReader = csv.reader(capitalCSV)

    monthlyTotal = 0;

    for row in capitalReader:
        print(str(capitalReader.line_num) + ' ' + str(row))       


main()
