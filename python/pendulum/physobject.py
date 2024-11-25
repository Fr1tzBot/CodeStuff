import pygame
from Vector import Vector2d
from Util import *

class physline:
    mass = float()

    #linear variables
    point1 = Vector2d()
    point2 = Vector2d()

    velocity = Vector2d()

    acceleration = Vector2d()

    #angular variables (angle cant be set directly)
    angular_velocity = float()

    angular_acceleration = float()

    def __init__(self, mass, point1, point2):
        self.mass = mass
        self.point1 = point1
        self.point2 = point2

    #update function - should be called once per specified time interval
    def update(self, time: float = 1) -> None:
        timev = Vector2d(time, time) # time is really a 1d vector
        self.velocity += self.acceleration * timev
        self.point1 += self.velocity * timev
        self.point2 += self.velocity * timev

        self.angular_velocity += self.angular_acceleration * time
        self.setAngle(self.getAngle() + (self.angular_velocity * time))

    #set angle, rotating about point1
    def setAngle(self, angle: float) -> None:
        self.point2 = Vector2d(self.point1.x + math.cos(angle) * self.getLength(), self.point1.y + math.sin(angle)*self.getLength())
        
    def getAngle(self) -> float:
        return getAngle(self.point1, self.point2)
    
    def getLength(self) -> float:
        return getDistance(self.point1, self.point2)

    def drawself(self, screen, color=(255, 255, 255), width=3):
        pygame.draw.line(screen, color, (self.point1.x, self.point1.y), (self.point2.x, self.point2.y), width)

    def getMOI(self) -> float:
        return (1/3) * self.mass * self.getLength()**2

    #apply a force at point2, causing a torque
    #return force remaining after torque (force applied to point1)
    def applyForce(self, force: Vector2d) -> Vector2d:
        fsin = force.getMagnitude() * math.sin(force.getAngle() - self.getAngle())
        torque = self.getLength() * fsin
        self.angular_acceleration = torque / self.getMOI()
        
        #return force that is transmitted through the line
        fcos = force.getMagnitude() * math.cos(force.getAngle() - self.getAngle())
        fx = fcos * math.cos(self.getAngle())
        fy = fcos * math.sin(self.getAngle())
        return Vector2d(fx, fy)
        
    def getGravity(self, gravity) -> Vector2d:
        return Vector2d(0, gravity) * Vector2d(self.mass, self.mass)

    def applyGravity(self, gravity) -> Vector2d:
        return self.applyForce(self.getGravity(gravity))

    def applyFriction(self, friction: float) -> None:
        self.angular_acceleration -= self.angular_velocity * friction

    #fix point1 to a point, moving point2 accordingly
    def fixtoPoint(self, point: Vector2d) -> None:
        offset = point - self.point1
        self.point1 = point
        self.point2 += offset
    
    def getLinearKineticEnergy(self) -> float:
        return 0.5 * self.mass * self.velocity.getMagnitude()**2
    
    def getAngularKineticEnergy(self) -> float:
        return 0.5 * self.getMOI() * self.angular_velocity**2
    
    def getKineticEnergy(self) -> float:
        return self.getLinearKineticEnergy() + self.getAngularKineticEnergy()