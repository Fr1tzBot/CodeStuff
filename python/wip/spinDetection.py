# pseudo code to detect when the wheel is free spinning

from enum import Enum

class SpinType(Enum):
    IDLE = 0
    OVER_ACCELERATION = 1 #off the line and spinning
    WRONG_DIRECTION = 2 #module aimed the wrong direction/sudden change in direction
    OVER_DECELERATION = 3 #slowing down abruptly
    NO_SPIN = 4 #no spin detected

class constants:
    WHEEL_DIAMETER = 4 #inches
    THETA_TOLERANCE = 10 #degrees
    SPEED_TOLERANGE = 1 #ft/s
    MAX_SPEED = 16.3 #ft/s


class sensors:
    theta = 0 #degrees
    v = 11 #ft/s

class module:
    driveDir = 0 #degrees
    speed = 15 #ft/s
    spinType = SpinType.IDLE


def toleranceCheck(value1: float, value2: float, tolerance: float) -> bool:
    return abs(value1-value2) <= tolerance

def getSpinning() -> bool:
    return (not toleranceCheck(
        sensors.theta, 
        module.driveDir, 
        constants.THETA_TOLERANCE)) or (
    not toleranceCheck(
        sensors.v, module.speed, 
        constants.SPEED_TOLERANGE)
    )

def getSpinType() -> SpinType:
    if getSpinning():
        if  not toleranceCheck(sensors.theta, module.driveDir, constants.THETA_TOLERANCE):
            return SpinType.WRONG_DIRECTION
        elif not toleranceCheck(sensors.v, module.speed, constants.SPEED_TOLERANGE) and sensors.v < module.speed:
            return SpinType.OVER_ACCELERATION
        else:
            return SpinType.OVER_DECELERATION
    else:
        if toleranceCheck(sensors.v, 0, constants.SPEED_TOLERANGE):
            return SpinType.IDLE
        return SpinType.NO_SPIN

def getPercentRumble() -> float:
    if getSpinning():
        gap = abs(sensors.v - module.speed)
        return gap / (constants.MAX_SPEED*2)
    else:
        return 0

def percent(num: float) -> str:
    num = round(num*100, 2)
    return str(num) + "%"
print(getSpinning())
print(percent(getPercentRumble()))
print(getSpinType())