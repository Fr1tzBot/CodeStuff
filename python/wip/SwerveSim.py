#!/usr/bin/env python3
"""SwerveSim.py: a simplistic swerve drivetrain simulator for testing new control schemes"""
import math
import enum
import sys
import pygame

class Constants:
    scale = 18 #scale is in pixels/foot, non-integer scales will cause strange results
    xres = 27*scale
    yres = 54*scale
    fps = 60
    bgColor = (60, 60, 60) #actual field color
    title = "Swerve Simulator"
    botWidth = 2.5*scale # 30 in square robot
    botHeight = 2.5*scale # 30 in square robot
    realMaxSpeed = 16.2 #max speed, in ft/s
    maxSpeed = (realMaxSpeed*scale)/fps #maxspeed is in pixels/frame
    wheelbase = 38.75 #diagonal distance from wheel center to wheel center
    #maxRot = ((360/((math.pi*wheelbase)/realMaxSpeed))) #maxRot is in degrees/frame. (this is roughly translated from max speed based on wheelbase of howitzer)
    maxRot = 6 #TODO: fix above formula and rotation oscilating
    maxAccel = (10*scale)/(fps**2) #stepSize is speed increase/frame
    slowFactor = 1.0 #multiplier that controls how quickly the bot slows down. relative to maxAccel
    joystickID = 0
    deadZone = 0.1
    delay = math.ceil(1000/fps)
    fileName = "botSprite.png"
    #speed tests:
    #horiz: 1.66666 seconds
    #vert:  3.33333 seconds
    #0-16.2: 1.62 seconds


class Bot:
    class AccelStates(enum.Enum):
        idle = 0
        accelerating = 1
        decelerating = 2
        redlining = 3
    x = 0 #robot's x position, in pixels
    y = 0 #robot's y position, in pixels
    xDelta = 0 #robot's x speed, in pixels/frame
    yDelta = 0 #robot's y speed, in pixels/frame
    theta = 0 #robot's actual angle, in degrees
    thetaDelta = 0 #robot's angular speed, in degrees/frame
    thetaTarget = 0 #robot's desired angle, in degrees
    bot = None #used to store active bot surface
    image = None #used to store unmodified bot surface
    accelState = None
    def getSpeed(self) -> float:
        return math.sqrt(self.xDelta**2 + self.yDelta**2)

class JoystickMap:
    class axis:
        class leftStick:
            x = 0 #left is negative x
            y = 1 #up is negative y
        leftTrigger = 2 #starts at -1, goes to 1
        class rightStick:
            x = 3 #left is negative x
            y = 4 #up is negative y
        rightTrigger = 5 #starts at -1, goes to 1

    class button:
        a = 0
        b = 1
        x = 2
        y = 3
        lb = 4
        rb = 5
        select = 6
        start = 7
        xbox = 8
        leftStick = 9
        rightStick = 10

    class dpad: #hat values are returned as a tuple
        x = 0 #down is negative y
        y = 1  #left is negative x

def xyToTheta(x: float, y: float) -> float:
    vec = pygame.math.Vector2(x, y)
    theta = vec.as_polar()[1]-90 #offset rotation by 90 degrees
    if theta != -90: #prevent resetting to 0 degrees when x and y are 0
        return theta

def xyToMagnitude(x: float, y: float) -> float:
    return math.sqrt(x**2 + y**2)

def signum(num: float) -> float:
    return math.copysign(1.0, num)

def constrainAngle(angle: float) -> float:
    if angle > 180:
        angle %= 180
        angle -=180

    if angle < -180:
        angle %= -180
        angle += 180

    return angle

def applyDeadzone(value: float, constants: Constants) -> float:
    return 0 if abs(value) < constants.deadZone else value

def getRot(bot: Bot, joystick: pygame.joystick.Joystick, joystickMap: JoystickMap, constants: Constants):
    x = applyDeadzone(joystick.get_axis(joystickMap.axis.rightStick.x), constants)
    y = -applyDeadzone(joystick.get_axis(joystickMap.axis.rightStick.y), constants)
    lt = applyDeadzone((joystick.get_axis(joystickMap.axis.leftTrigger)+1)/2, constants)
    rt = applyDeadzone((joystick.get_axis(joystickMap.axis.rightTrigger)+1)/2, constants)
    rotSpeed = lt-rt
    theta = xyToTheta(x, y)

    if theta is not None:
        bot.thetaTarget = xyToTheta(x, y)

    if rotSpeed != 0:
        print(rotSpeed)
        bot.thetaTarget = bot.theta
        bot.thetaDelta = constants.maxRot*rotSpeed

def getXY(bot: Bot, joystick: pygame.joystick.Joystick, joystickMap: JoystickMap, constants: Constants):
    x = applyDeadzone(joystick.get_axis(joystickMap.axis.leftStick.x), constants)
    y = applyDeadzone(joystick.get_axis(joystickMap.axis.leftStick.y), constants)
    if joystick.get_button(joystickMap.button.leftStick):
        x *= 0.5
        y *= 0.5
    bot.accelState = bot.AccelStates.accelerating

    #acceleration rate is proportional to joystick magnitude
    bot.yDelta += constants.maxAccel * y
    bot.xDelta += constants.maxAccel * x


    if (y == 0 and bot.yDelta != 0):
        #apply breaking force
        if abs(bot.yDelta) < constants.maxAccel*constants.slowFactor: #prevents oscilating when robot can't step to 0
            bot.yDelta = 0
        bot.accelState = bot.AccelStates.decelerating
        bot.yDelta += -math.copysign(constants.maxAccel*constants.slowFactor, bot.yDelta)

    if (x == 0 and bot.xDelta != 0):
        #apply breaking force
        if abs(bot.xDelta) < constants.maxAccel*constants.slowFactor: #prevents oscilating when robot can't step to 0
            bot.xDelta = 0
        bot.accelState = bot.AccelStates.decelerating
        bot.xDelta += -math.copysign(constants.maxAccel*constants.slowFactor, bot.xDelta)

    # cap robot's velocity to whatever % the joystick is outputting and cap overall speed
    if bot.getSpeed() > constants.maxSpeed * xyToMagnitude(x, y) and bot.accelState == bot.AccelStates.accelerating:
        scaleFactor = (constants.maxSpeed*xyToMagnitude(x, y))/bot.getSpeed()
        bot.xDelta *= scaleFactor
        bot.yDelta *= scaleFactor
        bot.accelState = bot.AccelStates.redlining

    #set to idle when speed is 0
    if bot.getSpeed() == 0:
        bot.accelState = bot.AccelStates.idle

    bot.x += bot.xDelta
    bot.y += bot.yDelta

def rotate(bot: Bot, constants: Constants):
    if bot.theta != bot.thetaTarget:
        error = bot.thetaTarget - bot.theta
        #make sure we don't overshoot the angle, leading to oscilation
        if abs(error) < constants.maxRot:
            bot.thetaDelta = error
        else:
            bot.thetaDelta = math.copysign(constants.maxRot, error)
        bot.theta += bot.thetaDelta

def limitBot(bot: Bot, constants: Constants):
    if bot.x > constants.xres - constants.botWidth:
        bot.x = constants.xres - constants.botWidth
        bot.xDelta = 0

    if bot.x < 0:
        bot.x = 0
        bot.xDelta = 0

    if bot.y > constants.yres - constants.botHeight:
        bot.y = constants.yres - constants.botHeight
        bot.yDelta = 0

    if bot.y < 0:
        bot.y = 0
        bot.yDelta = 0

    if abs(bot.thetaDelta) > constants.maxRot:
        bot.thetaDelta = math.copysign(constants.maxRot, bot.thetaDelta)

    bot.theta = constrainAngle(bot.theta)

    bot.thetaTarget = constrainAngle(bot.thetaTarget)

constants = Constants()
joystickMap = JoystickMap()
bot = Bot()

#pygame setup
pygame.init()
pygame.joystick.init()
bg = pygame.display.set_mode((constants.xres, constants.yres))
pygame.display.set_caption(constants.title)
bot.image = pygame.image.load(constants.fileName)
bot.image = pygame.transform.scale(bot.image, (constants.botWidth, constants.botHeight))
joystick = pygame.joystick.Joystick(constants.joystickID)
joystick.init()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
    bg.fill(constants.bgColor)
    getXY(bot, joystick, joystickMap, constants)
    getRot(bot, joystick, joystickMap, constants)
    rotate(bot, constants)
    limitBot(bot, constants)
    print(bot.theta, bot.thetaDelta, bot.thetaTarget)

    bot.bot = pygame.transform.rotate(bot.image, bot.theta)
    bg.blit(bot.bot, (bot.x, bot.y))
    pygame.display.flip()

    pygame.time.delay(constants.delay)
