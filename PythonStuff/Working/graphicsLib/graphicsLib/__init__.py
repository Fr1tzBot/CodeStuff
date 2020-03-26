#from pygame import Surface, i
from pygame import gfxdraw
import pygame
from time import sleep

#Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
GRAY = (128, 128, 128)
BROWN = (139,69,19)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
INDIGO = (75, 0, 130)
VIOLET = (128, 0, 128)
PURPLE = (128, 0, 128)

#Default Variable Values
window = None
windowSurface = None
windowSize = width, height = (0, 0)
defaultBackground = r, g, b = (0, 0, 0)

def refresh():
    pygame.display.flip()

def setDefaultBackgound(color):
    global defaultBackground
    defaultBackground = color

def fillScreen(color):
    window.fill(color)
    refresh()

def displayImage(path):
    image = pygame.image.load(path).convert()
    refresh()

def setSize(width, height):
    global windowSize
    windowSize = [width, height]

def start():
    global window
    global windowSurface
    window = pygame.display.set_mode(windowSize)
    windowSurface = pygame.Surface(windowSize)
    pygame.init()

def stop():
    refresh()
    pygame.display.quit()
    pygame.quit()
    exit()

def clearPixel(x, y, debug):
    global defaultBackground
    global windowSize
    global windowSurface
    if x > windowSize[0]:
        print("Fatal Error: clearPixel X Out of Range")
        if debug:
            exit()
    if y > windowSize[1]:
        print("Fatal Error: clearPixel Y Out of Range")
    elif debug:
        s = pygame.Surface((1,1))   # the object surface 1 x 1 pixel (a point!)
        s.fill(defaultBackground)               # color as (r,g,b); e.g. (100,20,30)
        # now get an object 'rectangle' from the object surface and place it at position x,y
        r,r.x,r.y = s.get_rect(),x,y    
        window.blit(s,r)
        print("Successfully cleared pixel: " + str(x) + " , " + str(y))
    elif not debug:
        s = pygame.Surface((1,1))   # the object surface 1 x 1 pixel (a point!)
        s.fill(defaultBackground)               # color as (r,g,b); e.g. (100,20,30)
        # now get an object 'rectangle' from the object surface and place it at position x,y
        r,r.x,r.y = s.get_rect(),x,y    
        window.blit(s,r)
    refresh()

def paintPixel(x, y, color, debug):
    global windowSize
    global windowSurface
    
    if x > windowSize[0]:
        print("Fatal Error: drawPixel X Out of Range")

        if debug:
            exit()

    if y > windowSize[1]:
        print("Fatal Error: drawPixel Y Out of Range")

    elif debug:
        s = pygame.Surface((1,1))   # the object surface 1 x 1 pixel (a point!)
        s.fill(color)               # color as (r,g,b); e.g. (100,20,30)
        # now get an object 'rectangle' from the object surface and place it at position x,y
        r,r.x,r.y = s.get_rect(),x,y    
        window.blit(s,r)
        print("Successfully drew pixel: " + str(x) + " , " + str(y))

    elif not debug:
        s = pygame.Surface((1,1))   # the object surface 1 x 1 pixel (a point!)
        s.fill(color)               # color as (r,g,b); e.g. (100,20,30)
        # now get an object 'rectangle' from the object surface and place it at position x,y
        r,r.x,r.y = s.get_rect(),x,y    
        window.blit(s,r)
