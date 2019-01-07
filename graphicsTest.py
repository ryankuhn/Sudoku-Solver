import pygame
pygame.init()

def placeNum(val, location,color,screenData):
    
    SPACE = screenData[0]
    screen = screenData[1]
    clock = screenData[2]
    font = screenData[3]

    text = font.render(str(val),True,color)
    xdist = int(location[0])*SPACE + SPACE/4
    ydist = int(location[1])*SPACE + SPACE/4

    screen.blit(text, [xdist,ydist])


def boardSetup():
    import pygame

    pygame.init()

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




