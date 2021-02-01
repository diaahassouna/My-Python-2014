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
setDisplay = pygame.display.set_mode((750,750))
#the window's title above
pygame.display.set_caption('my game')
#loading the image
img = pygame.image.load('C:/Users/Asus/Desktop/hell 3.jpg')
imgx = 10 #x coordiante of the image
imgy = 10 #y coordinate of the image
#the basic main infinite loop of game's life
while True:
    setDisplay.blit(img,(imgx,imgy))
    for event in pygame.event.get():
        print event
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update() 
