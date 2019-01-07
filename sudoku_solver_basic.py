import numpy
import array as arr
import pprint
import csv

from SudokuFunctions import * 
#printBoard, printLayer, receiveBoard, importBoard, makeBoardValid, identPossibleRowCal, identPossibleBox, eliminateTaken, findZero, methodOne, checkComplete

#filename = 'SudokuBoard2.csv'
filename = 'sudoku_easy.csv'

board = numpy.zeros(shape=(9,9,10), dtype=int)
printOrder = []

board = makeBoardValid(importBoard(filename),board) #imports board from csv file

#printLayer(board, 'row', 0)

printBoard(board,0)
iteration = 1

while checkComplete(board) == 0:
    print("Iteration ", iteration)
    startSum = sum(sum(board[0:9,0:9,0]))

    printBoard(board,0)
    printBoard(board,5)
    printBoard(board,8)

    identPossibleRowCol(board)     # Places 1's for each square in the nth place
    identPossibleBox(board)
    eliminateTaken(board)

    methodOne(board,printOrder)

    endSum = sum(sum(board[0:9,0:9,0]))
    if startSum == endSum:
        print("No more moves")
        break
    iteration = iteration + 1
    
printBoard(board,0)

print("Correct? ", checkCorrect(board))



