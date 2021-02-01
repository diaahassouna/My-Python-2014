#importing modules
import pygame
import sys
from pygame.locals import *
#initialization
pygame.init()
#defining colors and custom colors in RGB mode
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
cyan = (0,255,255)
magenta = (255,0,255)
#set variable of the window with 3 parameters , window dimentions , 
setDisplay = pygame.display.set_mode((400,300))
#the window's title above
pygame.display.set_caption('my game')
#set the background fill
setDisplay.fill(cyan)
#drawing pixils [1st coordinate] [2nd coordinate]
singlePixil = pygame.PixelArray(setDisplay)
singlePixil[3][3] = yellow
#drawing lines (surface,color,1st position,2nd position,thickness[optional])
pygame.draw.line(setDisplay,blue,(389,200),(300,70),4)
#drawing circles(surface,color,center position,raduis,thickness[optional])
pygame.draw.circle(setDisplay,red,(50,50),20) #closed donate
pygame.draw.circle(setDisplay,red,(100,50),20,4) #open donate
#drawing rectangles(surface,color,(top left coordinates,Horizontal move,Vertical move),thickness[optinal])
pygame.draw.rect(setDisplay,magenta,(150,150,50,100))
#drawing polygons(surface,color,list points,thickness[optional])
pygame.draw.polygon(setDisplay,green,((50,20),(30,40),(60,100)))
#the basic main infinite loop of game's life
while True:
    for event in pygame.event.get():
        print event
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update() 
