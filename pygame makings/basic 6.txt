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
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
cyan = (0,255,255)
magenta = (255,0,255)
#set variable of the window with 3 parameters , window dimentions , 
setDisplay = pygame.display.set_mode((750,400))
#the window's title above
pygame.display.set_caption('my game')
#loading the image
img = pygame.image.load('C:/Users/Asus/Desktop/hell 3.jpg')
FPS = 30 #frame per second
imgx = 10 #x coordiante of the upper left of the image
imgy = 10 #y coordinate of the upper left of the image
pixmove = 5 #pixil move each time
movement = 'down' #movement down [default movement]
fpsTime = pygame.time.Clock() #time variable
#the basic main infinite loop of game's life
while True:
    setDisplay.fill(black)
    if movement == 'down':
        imgy += pixmove
        if imgy > 200:
            img = pygame.transform.rotate(img,90) #rotating image counterclockwise
            movement = 'right'
    elif movement == 'right':
        imgx += pixmove
        if imgx > 200:
            img = pygame.transform.rotate(img,90) #rotating image counterclockwise            
            movement = 'up'
    elif movement == 'up':
        imgy -= pixmove
        if imgy < 30:
            img = pygame.transform.rotate(img,90) #rotating image counterclockwise            
            movement = 'left'
    elif movement == 'left':
        imgx -= pixmove
        if imgx < 30:
            img = pygame.transform.rotate(img,90) #rotating image counterclockwise            
            movement = 'down'
    setDisplay.blit(img,(imgx,imgy))
    for event in pygame.event.get():
        print event
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsTime.tick(FPS)
