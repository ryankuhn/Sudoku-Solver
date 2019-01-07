import numpy
import array as arr
import pprint
import csv
import pygame
from graphicsTest import boardSetup, placeNum
from SudokuFunctions import *
import time
pygame.init()


board = numpy.zeros(shape=(9,9,10), dtype=int)
INITIALBOARD = numpy.zeros(shape=(9,9), dtype=int)
printOrder = []


#receiveBoard(board)    # Receive board by typing in each value
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

SPACE = 70
size = (SPACE*9, SPACE*9)
screen = pygame.display.set_mode(size)
    
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', SPACE, True, False)
done = False

screenData = [SPACE, screen, clock, font]

def placeNum(val, location,color,screenData):
    
    SPACE = screenData[0]
    screen = screenData[1]
    clock = screenData[2]
    font = screenData[3]

    text = font.render(str(val),True,color)
    xdist = int(location[1])*SPACE + SPACE/4
    ydist = int(location[0])*SPACE + SPACE/4

    screen.blit(text, [xdist,ydist])

filename = 'sudoku_easy.csv'
board = makeBoardValid(importBoard(filename),board) #imports board from csv file
#INITIALBOARD = list(board[0:9,0:9,0])
for i in range(len(board)):
    for j in range(len(board[0])):
        INITIALBOARD[i,j] = board[i,j,0]

printBoard(board,0)
iteration = 1

# Solve the Board
while checkComplete(board) == 0:
    print("Iteration ", iteration)
    startSum = sum(sum(board[0:9,0:9,0]))

    printBoard(board,0)

    identPossibleRowCol(board)     # Places 1's for each square in the nth place
    identPossibleBox(board)
    eliminateTaken(board)

    printBoard(board,8)
    methodOne(board,printOrder)
    
    endSum = sum(sum(board[0:9,0:9,0]))
    if startSum == endSum:
        print("No more moves")
        break
    iteration = iteration + 1 
printBoard(board,0)
print("Correct? ", checkCorrect(board))

placeTo = 0
while not done:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop

    screen.fill(WHITE)   
    pygame.display.set_caption("Sudoku solver")
    
    for lineNum in range(1,10):
        width = 1
        if lineNum%3 == 0:
            width = 3
        pygame.draw.line(screen, BLACK, (SPACE*lineNum,0), (SPACE*lineNum,630), width)
        pygame.draw.line(screen, BLACK, (0,SPACE*lineNum), (630,SPACE*lineNum), width)
    
    # Print the initial board
    for i in range(len(INITIALBOARD)):
        for j in range(len(INITIALBOARD[0])):
            if INITIALBOARD[i][j] != 0:
                placeNum(INITIALBOARD[i][j],[i,j],BLACK,screenData)
            else:
                pass

    # Print each solved number
    for i in range(placeTo):
    #while place < 10:#len(placeNum):
        placeNum(printOrder[i][2],[printOrder[i][0],printOrder[i][1]],BLUE,screenData)
        
    if placeTo < len(printOrder):
        placeTo = placeTo + 1   

    pygame.display.flip()

    clock.tick(2)

pygame.quit()

printBoard(board,0)