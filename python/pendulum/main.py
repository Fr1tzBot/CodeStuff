import pygame
import sys
from physobject import physline
from Vector import Vector2d

# Initialize Pygame
pygame.init()

#constants
WINDOW_LENGTH = 800
WINDOW_WIDTH = 800

FRICTION = 0
GRAVITY = 10

LENGTH_1 = Vector2d(100, 100)
MASS_1 = 0.001
COLOR_1 = (255, 0, 0)

LENGTH_2 = Vector2d(-66, 66)
MASS_2 = MASS_1 * 2/3
COLOR_2 = (0, 0, 255)

LENGTH_3 = Vector2d(-33,-33)
MASS_3 = MASS_1 * 1/3
COLOR_3 = (0, 255, 0)

# Set up the display
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
carryforce = Vector2d()

#basic setup
CENTER = Vector2d(WINDOW_LENGTH/2, WINDOW_WIDTH/2)
END_1 = CENTER - LENGTH_1
END_2 = END_1 - LENGTH_2
END_3 = END_2 - LENGTH_3

line1 = physline(MASS_1, CENTER, END_1)
line2 = physline(MASS_2, END_1, END_2)
line3 = physline(MASS_3, END_2, END_3)

trail = []

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear screen
    screen.fill((0, 0, 0))

    line3.fixtoPoint(line2.point2)
    carryforce = line3.applyGravity(GRAVITY)
    line3.applyFriction(FRICTION)
    line3.update(clock.get_time() / 1000)
    line3.drawself(screen, COLOR_3)

    line2.fixtoPoint(line1.point2)
    carryforce = line2.applyForce(carryforce + line2.getGravity(GRAVITY) + line3.getGravity(GRAVITY))
    line2.applyFriction(FRICTION)
    line2.update(clock.get_time() / 1000)
    line2.drawself(screen, COLOR_2)

    line1.applyForce(carryforce + line1.getGravity(GRAVITY) + line2.getGravity(GRAVITY) + line3.getGravity(GRAVITY))
    line1.applyFriction(FRICTION)
    line1.update(clock.get_time() / 1000)
    line1.drawself(screen, COLOR_1)

    # print("Total Kinetic Energy: ", line1.getKineticEnergy() + line2.getKineticEnergy() + line3.getKineticEnergy())

    trail.append(line3.point2)
    for i in trail:
        pygame.draw.circle(screen, (0, 255, 0), (int(i.x), int(i.y)), 1)

    pygame.display.flip()
    # Cap the frame rate
    clock.tick(60)
