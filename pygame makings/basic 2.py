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
#set of the window with 3 parameters , window dim. , 
setDisplay = pygame.display.set_mode((400,300))
#the window's title above
pygame.display.set_caption('my game')
#the basic main infinite loop of game's life
while True:
    for event in pygame.event.get():
        print event
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update() 
