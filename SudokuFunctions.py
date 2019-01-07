# Functions for Sudoku solver
import csv
import matplotlib.pyplot as plt
import numpy
import array as arr
import pygame


def printBoard (board, layer):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j][layer], end=" ") # print(board), in python 2.7
        print('')
    print()    


def printLayer (board,rowCol,layerNum):
    if str(rowCol) == 'row':
        for k in range(len(board[layerNum][0])):
            for j in range(len(board[layerNum])):
                print(board[layerNum][j][k], end=" ")
            print('')
    elif str(rowCol) == 'col':
        for i in range(len(board)):
            for k in range(len(board[i][layerNum])):
                print(board[i][layerNum][k], end=" ")
            print('')
    print()        

def receiveBoard (board):
    print("Enter each value in the board row by row, left to right")
    for i in range(len(board)):     # Each row of the board
        for j in range(len(board[i])):      # Each column of the board
            val = str(raw_input())          # Take the raw input and turn to string to allow for empy inputs
            valid = 0                       # Simple true or false if the input is valid
            while not valid:
                if not val:     # If the input is empty place a zero in the board
                    board[i][j] = 0
                    print("empty")
                    valid = 1
                elif int(val) <= 0 or int(val) > 9:         # If the input is beyond [1 9] request a new value
                    val = str(raw_input("Try again [1 9]: "))
                    valid = 0
                else:
                    board[i][j] = val
                    valid = 1


def importBoard (filename):
    results = []
    with open(filename) as inputfile:
        for row in csv.reader(inputfile):
            results.append(row)
    return results     
    
def makeBoardValid (results,board):
    for i in range(len(results)):     # Each row of the board
        for j in range(len(results[i])):
            valid = 1
            if not str(results[i][j]):
                print("Board not valid")
                break
            elif int(results[i][j]) < 0 and int(results[i][j]) > 9:
                print("Board not valid")
                break
            else:
                board[i][j][0] = results[i][j]
    return board  


def identPossibleRowCol(board):
    rows = [[0 for col in range(10)] for row in range(9)] # makes a 9x10 array of zeros for the rows
    cols = [[0 for col in range(9)] for row in range(10)] # makes a 9x9 array of zeros for the columns
    for i in range(len(board)):     # Step through each row
        for j in range(len(board[i])):  # Step through each col
            rows[i][int(board[i][j][0])] = 1  
            cols[int(board[i][j][0])][j] = 1     # Assigns a 1      

    for i in range(len(board)):     # Step through each row
        for j in range(len(board[i])):  # Step through each col
            for k in range(1,len(board[i][j])):
                if rows[i][k] == 1:
                    board[i][j][k] = 1
                if cols[k][j] == 1:
                    board[i][j][k] = 1

def identPossibleBox(board):
    for i in range(int(len(board)/3)):
        for j in range(int(len(board[i])/3)):
            taken = [0 for col in range(10)]
            for boxi in range(3):
                for boxj in range(3):
                    taken[board[i*3+boxi][j*3+boxj][0]] = 1
            for k in range(1,len(taken)):  
                if taken[k] == 1:
                    board[i*3:i*3+3,j*3:j*3+3,k] = 1

def eliminateTaken(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i,j,0] != 0:
                board[i,j,1:len(board[i][j])] = 1


def findZero(board,i,j,z):
    for boxi in range(3):
        for boxj in range(3):
            if board[i*3+boxi][j*3+boxj][z] == 0:
                return [i*3+boxi,j*3+boxj,z]

def methodOne(board,printOrder):
    sqSize = 3
    # Nest for loops steps through each quadrant of the board
    for i in range(int(len(board)/3)):   # steps 0, 1, 2
        for j in range(int(len(board[i])/3)): # steps 0, 1, 2
            for z in range(1,len(board[0][0])): # Steps through the depth of board
                total = sum(sum(board[i*3:i*3+3,j*3:j*3+3,z]))
                if total == 8:
                    loc = findZero(board,i,j,z)
                    print("Find zero ", loc)
                    printOrder.append(loc)

                    if board[loc[0],loc[1],0] != 0:
                        raise Exception("Already value")
                    else:
                        board[loc[0],loc[1],0] = z


def checkComplete(board):
    complete = 1
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j][0] == 0:
                complete = 0
                return complete

def checkCorrect(board):
    correct = True
    for i in range(len(board)):
        un, counts = numpy.unique(board[i,:,0],return_counts=True)   
        dict(zip(un, counts))
        if counts.max() != 1 or counts.min() !=1:
            return not correct
    for j in range(len(board[0])):
        un, counts = numpy.unique(board[i,:,0],return_counts=True)   
        dict(zip(un, counts))
        if counts.max() != 1 or counts.min() != 1:
            return not correct
    for i in range(int(len(board)/3)):
        for j in range(int(len(board[i])/3)):
            un, counts = numpy.unique(board[i*3:i*3+3,j*3:j*3+3,0],return_counts=True)   
            dict(zip(un, counts))
            if counts.max() != 1 or counts.min() != 1:
                return not correct

    return correct            
            
def method2(board):
    return board
                      

