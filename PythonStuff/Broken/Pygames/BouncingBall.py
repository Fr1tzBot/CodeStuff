import pygame
from time import sleep


pygame.init() #initialises the imported modules

size = width, height = 960,720
speed= [0.1,0.1]
black= 0,0,0 #set the background colour

screen = pygame.display.set_mode(size) 

ball = pygame.image.load("ball.png").convert()
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            exit()

    ballrect=ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right>width:
        speed[0]=-speed[0]
    if ballrect.top <0 or ballrect.bottom > height:
        speed[1] =-speed[1]

        screen.fill(black)
        screen.blit(ball,ballrect)
        pygame.display.flip()
        #sleep(1)
    
        
