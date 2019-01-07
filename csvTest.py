# Testing how to use csv open functions in Python 3
import csv
filename = 'sudoku_easy.csv'

def importBoard (filename):
    results = []
    with open(filename) as inputfile:
        for row in csv.reader(inputfile):
            results.append(row)
    return results 

importBoard(filename)
    