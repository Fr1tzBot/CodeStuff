import pygame
#define colors, screen size, and screen
size = [700, 500]
RED = (255, 0, 0)
ORANGE = (255, 100, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (100, 0, 100)
PINK = (255, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
screen = pygame.display.set_mode(size)
def update():
	pygame.display.flip()
def backround (c):
	c = c.lower() #make the string in "c" lowercase
	if c == "red":
		screen.fill(RED)
	if c == "orange":
		screen.fill(ORANGE)
	if c == "yellow":
		screen.fill(YELLOW)
	if c == "green":
		screen.fill(GREEN)
	if c == "blue":
		screen.fill(BLUE)
	if c == "purple":
		screen.fill(PURPLE)
	if c == "black":
		screen.fill(BLACK)
	if c == "white":
		screen.fill(WHITE)
	if c == "pink":
		screen.fill(PINK)
def windowtitle (c):
	pygame.display.set_caption(c)
def eventproccess():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
# examples of uses:
#eventproccess()
#backround("red")
#windowtitle("this is the color red.")
#update()
