#Important :-
  ## variables is your own names , but values which contains (dots) and you assain
   # are fixed , so make your variables free rational names
#importing modules
import pygame
import sys
from pygame.locals import *
#initialization
pygame.init()
#defining colors and custom colors in RGB mode
white = (255,255,255)
black = (0,0,0)
#backgroud
bg = black
#frames per sec.
fps = 30
dispwidth = 800
dispheight = 600
cellsize = 10 #the Cell size (instead of pixils when we have sprites)
#defining directions
UP = 'up'
DOWN = 'down'
RIGHT = 'right'
LEFT = 'left'
#the function for running game [contains the main loop]
def runGame():
    startx = 3
    starty = 3
    coords = [{'x':startx,'y':starty}]
    direction = RIGHT

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit() 
       #cooresponding with user's clicks
            elif event.type == KEYDOWN:
                #when user clicks on left arraw
                if event.key == K_LEFT:
                    direction = LEFT
                #when user clicks on right arraw
                elif event.key == K_RIGHT:
                    direction = RIGHT
                #when user clicks on down arraw
                elif event.key == K_DOWN:
                    direction = DOWN
                #when user clicks on up arraw
                elif event.key == K_UP:
                    direction = UP
        if direction == UP:
            newcell = {'x':coords[0]['x'],'y':coords[0]['y']-1}
        elif direction == DOWN:
            newcell = {'x':coords[0]['x'],'y':coords[0]['y']+1}
        elif direction == LEFT:
            newcell = {'x':coords[0]['x']-1,'y':coords[0]['y']}
        elif direction == RIGHT:
            newcell = {'x':coords[0]['x']+1,'y':coords[0]['y']}

        del coords[-1]    

        coords.insert(0,newcell)
        setDisplay.fill(bg)
        drawCell(coords)
        pygame.display.update()
        fpsTime.tick(fps)


def drawCell(coords):
    for coord in coords:
        x = coord['x']*cellsize
        y = coord['y']*cellsize
        makecell = pygame.Rect(x,y,cellsize,cellsize)
        pygame.draw.rect(setDisplay,white, makecell)


while True:
    global fpsTime
    global setDisplay

    fpsTime = pygame.time.Clock()
    setDisplay = pygame.display.set_mode((dispwidth,dispheight))
    pygame.display.set_caption('controlling')
    runGame()
