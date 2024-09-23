
from time import sleep

groundSpeed = 12
moduleSpeed = 14
engageTolerance = 0.4 #ft/s
disengageTolerance = 0.4
rampDownRate = 0.01 #percent/0.02 seconds

def setPower(pwr: float) -> None:
    pass

def getPower() -> float:
    return 0

#main loop
while True:
    if abs(moduleSpeed-groundSpeed) > engageTolerance:
        #TCS ENGAGED
        #here you can either brake:
        while moduleSpeed-groundSpeed > disengageTolerance:
            setPower(0)
        #or slowly ramp down power
        while moduleSpeed-groundSpeed > disengageTolerance:
            sleep(0.02) #rio refresh rate
            setPower(getPower()-(rampDownRate))
    else:
        #TCS DISENGAGED
        continue
