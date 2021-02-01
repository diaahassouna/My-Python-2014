#importing modules
import pygame
import sys
from pygame.locals import *
#initialization
pygame.init()
#set of the window with 3 parameters
setDisplay = pygame.display.set_mode((400,300))
#the window's title above
pygame.display.set_caption('my game')
#the basic main infinite loop of game's life
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()        
