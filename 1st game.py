#the importing of the modules
import pygame
import sys
from pygame.locals import *
#initialization of the main method
pygame.init()
#definition of the standard colors
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
yellow=(255,255,0)
cyan=(0,255,255)
magenta=(255,0,255)
#definition of the window and its contents
setDisplay=pygame.display.set_mode((400,300))
#the title 
pygame.display.set_caption('1st game')
#filling the background of the main picture
setDisplay.fill(cyan)
#difinition of putting pixels
singlePixil=pygame.PixelArray(setDisplay)
#putting a colored pixel
singlePixil[3][3]=magenta
#drawing some static shapes
pygame.draw.line(setDisplay,blue,(389,200),(300,70),4)
pygame.draw.circle(setDisplay,blue,(50,50),20,1)
pygame.draw.rect(setDisplay,magenta,(100,100,200,100))
pygame.draw.polygon(setDisplay,green,((50,20),(30,40),(60,100)))
#the main loop to run the program
while True:
    for event in pygame.event.get():
        print event
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    #updating the screen        
    pygame.display.update()        
