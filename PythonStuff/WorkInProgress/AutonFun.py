# VEX V5 Python Project with Competition Template
import sys
import vex
from vex import *
import math

# Creates a competition object that allows access to Competition methods.
competition = vex.Competition()

def pre_auton():
    # All activities that occur before competition start
    # Example: setting initial positions
    pass

def autonomous():
    # Place autonomous code here
    
    #below: variables to change
    wheelR = 0.15915494309 #inches
    Kp = 1 #proportional pid value
    Kf = 0 #feed forward value

    #below: variables not to change
    wheelD = wheelR * 2
    wheelC = math.pi*wheelD
    
    #below: self explanitory functions
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
            

def drivercontrol():
    # Place drive control code here, inside the loop
    while True:
        # This is the main loop for the driver control.
        # Each time through the loop you should update motor
        # movements based on input from the controller.
        pass

# Do not adjust the lines below

# Set up (but don't start) callbacks for autonomous and driver control periods.
competition.autonomous(autonomous)
competition.drivercontrol(drivercontrol)

# Run the pre-autonomous function.
pre_auton()

# Robot Mesh Studio runtime continues to run until all threads and
# competition callbacks are finished.
