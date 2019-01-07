import numpy
import array as arr
import pygame
pygame.init()

clock = pygame.time.Clock()
done = False

SPACE = 70
size = (SPACE*9, SPACE*9)
screen = pygame.display.set_mode(size)
WHITE    = ( 255, 255, 255)
BLACK    = (   0,   0,   0)


screen.fill(WHITE)   
pygame.display.set_caption("Sudoku solver")

pygame.draw.line(screen, BLACK, (SPACE,0), (SPACE,630), 2)

pygame.display.flip()

clock.tick(60)


while not done:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop

pygame.quit()


