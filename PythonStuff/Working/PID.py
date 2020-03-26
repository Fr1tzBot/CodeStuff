# template for pid for moving x inches on a robot
import math

#below: variables to change
wheelR = 0.15915494309 #inches
Kp = 1 #proportional pid value
Kf = 0 #feed forward value

#below: variables not to change
wheelD = wheelR * 2
wheelC = math.pi*wheelD

#below: self explanitory functions
def resetEncoder():
    #set the encoder's value to 0
def readEncoder
def getvelocity():
    #TODO: get encoder command
    return 0 # return the encoder RPM
def setPWR(pwr):
    #set the power to a value from -1 to 1
    if pwr > 1:
        pwr = 1
    elif pwr < -1:
        pwr = -1
    #TODO: set power command
def inchesToFeet(inches):
    return inches/12
def feetToInches(feet):
    return feet*12
def rpmToIPS(rpm):
    rps = rpm * 60 #one RPM unit is equivalent to 60 rps units
    IPS = rps*wheelC
    return IPS
def rpmToFPS(rpm):
    FPS = inchesToFeet(rpmToIPS(rpm))
    return FPS
def PID_RPM(targetRPM):
    global Kp
    global Kf
    while True:
        error = getvelocity()-targetRPM
        setPWR(Kp*error)
def PID_Inches
